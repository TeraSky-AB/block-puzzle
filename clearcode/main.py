import pygame as pg
import random as rnd
import modules.grid as gd
import modules.display as dsp
import modules.player as player
import modules.functions as fnc
import modules.pieces as pcs


SCREENHEIGHT = 700
SCREENWIDTH = 450
screensize = (SCREENWIDTH, SCREENHEIGHT)

boardX = 65
boardY = 65

BACKGROUNDCOLOR = (125, 201, 255)
BOARDCOLOR = (91, 137, 194)
CREAM = (240, 247, 244)
REDPINK = (255, 143, 137, 200)
GREEN = (69, 222, 130)
NAVY = (7, 51, 92)
YELLOW = (255, 207, 74)
GRAY = (41, 41, 41)
RED = (219, 109, 103)

mediumFont = pg.font.Font('assets/BebasNeue-Regular.ttf', 40)
smallFont = pg.font.Font('assets/BebasNeue-Regular.ttf', 25)
soloText = mediumFont.render("SOLO", True, NAVY)
multiText = mediumFont.render("MULTI", True, NAVY)
quitText = mediumFont.render("QUIT", True, NAVY)
returnText = mediumFont.render("RETURN", True, NAVY)
quitText1 = mediumFont.render("Quit", True, GRAY)
restart = mediumFont.render("Restart", True, GRAY)
returnMenuText = smallFont.render("RETURN", True, NAVY)
returnMenuText1 = smallFont.render("RETURN", True, CREAM)
# MENU RECTS

soloButtonRect = pg.Rect(150, 318, 150, 50)
multiButtonRect = pg.Rect(150, 383, 150, 50)
quitButtonRect = pg.Rect(150, 448, 150, 45)

returnButtonRect = pg.Rect(150, 448, 150, 45)
restartButtonRect = pg.Rect(150, 405, 150, 50)
returnMenuButtonRect = pg.Rect(340, 645, 85, 30)

multiLocalButtonRect = pg.Rect(50,230,330,50)

pg.init()

screen = pg.display.set_mode(screensize)
pg.display.set_caption("PyPuzzle")

def updates(players, pieces, grid):
	pieces.update(players)
	for i in players:
		i.update(pieces)
		for j in i.draw:
			j.update(screen)
			j.drawPiece(screen)
	grid.isThereAlignement()
	players[0].points += len(grid.linesCompleted)*100
	grid.eraseAlignement()


def updatesMultiLocal(pieces, players, grids, screen, currentPlayer):
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


def menu():
	doContinue = True
	while doContinue:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				fnc.quitGame()
			elif event.type == pg.MOUSEBUTTONDOWN:
				if soloButtonRect.collidepoint(event.pos):
					solo()
				if multiButtonRect.collidepoint(event.pos):
					multiMenu()
				if quitButtonRect.collidepoint(event.pos):
					fnc.quitGame()
		dsp.displayMenu(screen)
		# HOVER
		pos = pg.mouse.get_pos()
		# SOLO
		if 150+150 > pos[0] > 150 and 318+45 > pos[1] > 318:
			pg.draw.rect(screen, YELLOW, (150, 318, 150, 45))
			screen.blit(soloText, (195,320))
		else:
			pg.draw.rect(screen, CREAM, (150, 318, 150, 45))
			screen.blit(soloText, (195,320))
		# MULTI
		if 150+150 > pos[0] > 150 and 383+45 > pos[1] > 383:
			pg.draw.rect(screen, YELLOW, (150, 383, 150, 45))
			screen.blit(multiText, (191,384))
		else:
			pg.draw.rect(screen, GREEN, (150, 383, 150, 45))
			screen.blit(multiText, (191,384))
		# QUIT
		if 150+150 > pos[0] > 150 and 448+45 > pos[1] > 448:
			pg.draw.rect(screen, YELLOW, (150, 448, 150, 45))
			screen.blit(quitText, (200, 448))
		else:
			pg.draw.rect(screen, REDPINK, (150, 448, 150, 45))
			screen.blit(quitText, (200, 448))
		pg.display.flip()

def multiMenu():
	dsp.displayMulti(screen)
	doContinue = True
	while doContinue:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				fnc.quitGame()
			elif event.type == pg.MOUSEBUTTONDOWN:
				if returnButtonRect.collidepoint(event.pos):
					menu()
				elif multiLocalButtonRect.collidepoint(event.pos):
					multiLocal()
		# HOVER
		pos = pg.mouse.get_pos()	
		if 150+150 > pos[0] > 150 and 448+45 > pos[1] > 448:
			pg.draw.rect(screen, YELLOW, (150, 448, 150, 45))
			screen.blit(returnText, (179, 448))
		else:
			pg.draw.rect(screen, REDPINK, (150, 448, 150, 45))
			screen.blit(returnText, (179, 448))
		pg.display.flip()

def gameOverSolo(player1):
	dsp.displayGameOverSolo(screen, player1)
	doContinue = True
	while doContinue:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				fnc.quitGame()
			elif event.type == pg.MOUSEBUTTONDOWN:
				if restartButtonRect.collidepoint(event.pos):
					menu()
				if quitButtonRect.collidepoint(event.pos):
					fnc.quitGame()
		# HOVER			
		pos = pg.mouse.get_pos()	
		if 150+150 > pos[0] > 150 and 383+45 > pos[1] > 383:
			pg.draw.rect(screen, CREAM, (150, 383, 150, 45))
			screen.blit(restart, (174, 385))
		else:
			pg.draw.rect(screen, BACKGROUNDCOLOR, (150, 383, 150, 45))
			screen.blit(restart, (174, 385))

		if 150+150 > pos[0] > 150 and 448+45 > pos[1] > 448:
			pg.draw.rect(screen, CREAM, (150, 448, 150, 45))
			screen.blit(quitText1, (200, 448))
		else:
			pg.draw.rect(screen, YELLOW, (150, 448, 150, 45))
			screen.blit(quitText1, (200, 448))
		pg.display.flip()

def onlineMultiMenu():
	dsp.displayOnlineMulti(screen)

def solo():
	pieces = pcs.Pieces()
	grid = gd.Grid(10, pieces)
	grid.init()
	grid.definePhysicalLimits()
	player1 = player.Player()
	players = [player1]

	currentDisplay = 'solo'
	currentlyDragging = False
	doContinue = True
	while doContinue:
		
		for event in pg.event.get():
			if event.type == pg.QUIT:
				fnc.quitGame()
			elif event.type == pg.MOUSEBUTTONDOWN:
				if currentDisplay == 'solo':
					for j in player1.draw:
						if j.rect.collidepoint(event.pos) and not currentlyDragging:
							currentlyDragging = True
							j.dragged = True
				if returnMenuButtonRect.collidepoint(event.pos):
					menu()

			elif event.type == pg.MOUSEBUTTONUP:
				if currentDisplay == 'solo':
					if currentlyDragging:
						for j in player1.draw:
							if j.rect.collidepoint(event.pos):
								currentlyDragging = False
								j.dragged = False
								if fnc.isOnGrid(event.pos):
									gridPos = ((event.pos[0]-boardX)/32+1,(event.pos[1]-boardY)/32+1)
									if grid.isPiecePlaceable(int(gridPos[0]), int(gridPos[1]), j.figureNumber):
										grid.putPiece(int(gridPos[0]), int(gridPos[1]), j.figureNumber)
										players[0].points += 30
										player1.draw.remove(j)
		if currentDisplay == 'solo':
			dsp.displayBoard(screen, (boardX, boardY), grid)
			updates(players, pieces, grid)
			dsp.displayDrawPieces(player1)
			dsp.displayTexts(screen, player1)
			if not grid.isDrawPlaceable(player1):
				gameOverSolo(player1)
		
		# HOVER
		pos = pg.mouse.get_pos()
		if 340+85 > pos[0] > 340 and 645+30 > pos[1] > 645:
			pg.draw.rect(screen, YELLOW, (340, 645, 85, 30))
			screen.blit(returnMenuText, (354, 647))
		else:
			pg.draw.rect(screen, GRAY, (340, 645, 85, 30))
			screen.blit(returnMenuText1, (354, 647))
		pg.display.flip()

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
										players[currentPlayer % 2].points += 30
										currentPlayer += 1
					if returnMenuButtonRect.collidepoint(event.pos):
						menu()
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

			# HOVER
		pos = pg.mouse.get_pos()
		if 340 + 85 > pos[0] > 340 and 645 + 30 > pos[1] > 645:
			pg.draw.rect(screen, YELLOW, (340, 645, 85, 30))
			screen.blit(returnMenuText, (354, 647))
		else:
			pg.draw.rect(screen, GRAY, (340, 645, 85, 30))
			screen.blit(returnMenuText1, (354, 647))
		pg.display.flip()

if __name__ == '__main__':
	menu()


