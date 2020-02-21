import pygame as pg
import modules.display as dsp
import modules.functions as fnc
import modules.pieces as pcs
import modules.player as player
import modules.grid as gd
import random as rnd


SCREENHEIGHT = 650
SCREENWIDTH = 440
screensize = (SCREENWIDTH, SCREENHEIGHT)

pg.init()

screen = pg.display.set_mode(screensize)
pg.display.set_caption("PyPuzzle")

# MENU RECTS ========

soloButtonRect = pg.Rect(165, 330, 120, 45)
multiButtonRect = pg.Rect(165, 400, 120, 45)
quitButtonRect = pg.Rect(165, 470, 120, 45)
restartButtonRect = pg.Rect(165, 470, 120, 45)

# ===================

# GAME RECTS ========

quitButtonRect = pg.Rect(165, 470, 120, 45)
restartButtonRect = pg.Rect(165, 470, 120, 45)

# ===================

# BOARD COORDINATES =

boardX = 50
boardY = 50

# ===================


def menu():
	"""
	This function displays the menu of PyPuzzle game
	"""
	currentDisplay = 'menu'
	print("ok")
	doContinue = True

	while doContinue:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				fnc.quitGame()
				quit()
			elif event.type == pg.MOUSEBUTTONUP:
				if currentDisplay == 'menu':
					if soloButtonRect.collidepoint(event.pos):
						solo()
						doContinue = False
					elif multiButtonRect.collidepoint(event.pos):
						multiLocal()
						doContinue = False
					elif quitButtonRect.collidepoint(event.pos):
						fnc.quitGame()
						quit()

		# INSTRUCTIONS ====

		if currentDisplay == 'menu':
			dsp.displayMenu(screen)
		elif currentDisplay == 'multiMenu':
			dsp.displayMulti(screen)
		elif currentDisplay == 'onlineMultiMenu':
			dsp.displayOnlineMulti(screen)
		# ================

		pg.display.flip()


def updatesSolo(pieces, players, grid, screen):  # Update player draw and check if grid has alignements
	"""
	updates() updates the different components of solo function.
	:param grid:
	:param pieces: Pieces object
	:param players: Players objects list
	:param grids: Grids objects list
	:param screen: Current window to display game on
	:param currentPlayer: Number of current player
	"""
	pieces.update(players)
	players[0].update(pieces)
	print("solo update")
	for piece in players[0].draw:
		piece.update(screen)
		piece.drawPiece(screen)
	grid.isThereAlignement()
	players[0].points += len(grid.linesCompleted) * 100
	grid.eraseAlignement()


def solo():
	pg.display.set_caption("PyPuzzle")

	currentlyDragging = False
	pieces = pcs.Pieces()
	grid = gd.Grid(10, pieces)
	grid.init()
	grid.definePhysicalLimits()
	player1 = player.Player()
	players = [player1]

	currentDisplay = 'game'

	dosolo = True

	while dosolo:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				fnc.quitGame()
				quit()
			elif event.type == pg.MOUSEBUTTONDOWN:
				if currentDisplay == 'game':
					for j in player1.draw:
						if j.rect.collidepoint(event.pos) and not currentlyDragging:
							currentlyDragging = True
							j.dragged = True
			elif event.type == pg.MOUSEBUTTONUP:
				if currentDisplay == 'game':
					for j in player1.draw:
						if j.rect.collidepoint(event.pos) and currentlyDragging:
							currentlyDragging = True
							j.dragged = False
							if fnc.isOnGrid(event.pos):
								gridPos = ((event.pos[0]-boardX)/32+1,(event.pos[1]-boardY)/32+1)
								if grid.isPiecePlaceable(int(gridPos[0]), int(gridPos[1]), j.figureNumber):
									grid.putPiece(int(gridPos[0]), int(gridPos[1]), j.figureNumber)
									player1.points += 50
									player1.draw.remove(j)
				elif currentDisplay == 'gameover':
					if quitButtonRect.collidepoint(event.pos):
						fnc.quitGame()
						quit()
					elif restartButtonRect.collidepoint(event.pos):
						fnc.quitGame()
		if currentDisplay == 'game':
			dsp.displayBoard(screen, (boardX, boardY), grid)
			updatesSolo(pieces, players, grid, screen)
			dsp.displayDrawPieces(player1)
			dsp.displayTexts(screen, player1)
			if not grid.isDrawPlaceable(player1):
				currentDisplay = 'gameover'
		elif currentDisplay == 'gameover':
			dsp.displayGameOverSolo(screen, player1)

		pg.display.flip()


def updatesMultiLocal(pieces, players, grids, screen, currentPlayer):  # Update player draw and check if grid has alignements
	"""
	updates() updates the different components of multilocal function.
	:param pieces: Pieces object
	:param players: Players objects list
	:param grids: Grids objects list
	:param screen: Current window to display game on
	:param currentPlayer: Number of current player
	"""
	pieces.update(players)
	for player in players:
		player.update(pieces)
		for piece in player.draw:
			piece.update(screen)
			if player == players[currentPlayer%2]:
				piece.drawPiece(screen)
	grids[currentPlayer % 2].isThereAlignement()
	players[currentPlayer % 2].points += len(grids[currentPlayer % 2].linesCompleted) * 100
	grids[currentPlayer % 2].eraseAlignement()


def multiLocal():
	"""
	multiLocal() handles the local multiplayer: player versus player. Both players's board are displayed one after
	the other on a 650x440 wide window. Creates a new window.
	"""
	players = []
	grids = []
	pieces = pcs.Pieces()

	currentDisplay = 'game'

	for i in range(2):
		players.append(player.Player(i))
		grids.append(gd.Grid(10, pieces))
		grids[i].init()
		grids[i].definePhysicalLimits()

	currentPlayer = rnd.randint(0, 1)
	currentlyDragging = False



	stop = False
	while not stop:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				fnc.quitGame()
				quit()
			elif event.type == pg.MOUSEBUTTONDOWN:
				for piece in players[currentPlayer % 2].draw:
					if piece.rect.collidepoint(event.pos) and not currentlyDragging:
						currentlyDragging = True
						piece.dragged = True

			elif event.type == pg.MOUSEBUTTONUP:
				if currentDisplay == 'game':
					if currentlyDragging:
						for piece in players[currentPlayer % 2].draw:
							if piece.rect.collidepoint(event.pos):
								currentlyDragging = False
								piece.dragged = False
								if fnc.isOnGrid(event.pos):
									gridPos = ((event.pos[0] - boardX) / 32 + 1, (event.pos[1] - boardY) / 32 + 1)
									if grids[currentPlayer % 2].isPiecePlaceable(int(gridPos[0]), int(gridPos[1]), piece.figureNumber):
										grids[currentPlayer % 2].putPiece(int(gridPos[0]), int(gridPos[1]), piece.figureNumber)
										players[currentPlayer % 2].draw.remove(piece)
										players[currentPlayer % 2].points += 50
										currentPlayer += 1
				elif currentDisplay == 'gameover':
					if restartButtonRect.collidepoint(event.pos):
						quit()
						menu()
					elif quitButtonRect.collidepoint(event.pos):
						pg.display.quit()
						quit()

		# INSTRUCTIONS OF LOOP ===
		if currentDisplay == 'game':
			dsp.displayBoard(screen, (boardX, boardY), grids[currentPlayer % 2])
			updatesMultiLocal(pieces, players, grids, screen, currentPlayer)
			dsp.displayDrawPieces(players[currentPlayer % 2])
			dsp.displayTexts(screen, players[currentPlayer % 2])
			if not grids[currentPlayer % 2].isDrawPlaceable(players[currentPlayer % 2]):
				currentDisplay = 'gameover'
		elif currentDisplay == 'gameover':
			dsp.displayGameOverMulti(screen, players[currentPlayer%2])

		pg.display.flip()
		# ========================

menu()




