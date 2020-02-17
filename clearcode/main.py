import pygame as pg
import modules.grid as gd
import modules.display as dsp
import modules.player as player
import modules.pieces as pcs
import modules.multiplayer as multi
import random as rnd

def updates():
	pieces.update(players)
	for i in players:
		i.update(pieces)
		for j in i.draw:
			j.update(screen)
	grid.isThereAlignement()
	player1.points += len(grid.linesCompleted)*100
	grid.eraseAlignement()

def isOnGrid(pos):
	if pos[0] > boardX and pos[0] < boardX+320 and pos[1] > boardY and pos[1] < boardY+320:
		return True
	else:
		return False

def quitGame():
	doContinue = False
	pg.display.quit()
	quit()

def firstPlayerToPlay():
	return rnd.randint(0,1)

def initGameSolo():
	global currentlyDragging, pieces, grid, player1, players
	currentlyDragging = False
	pieces = pcs.Pieces()

	grid = gd.Grid(10, pieces)
	grid1 = gd.Grid(10, pieces)
	grids = [grid, grid1]
	for i in grids:
		i.init()
		i.definePhysicalLimits()

	player1 = player.Player()
	players = [player1]

def initGameMulti():
	global currentlyDragging, pieces, grid, grid1, grids, player1, player2, players, firstPlayerToPlay
	currentlyDragging = False
	pieces = pcs.Pieces()

	firstPlayerToPlay = rnd.randint(0,1)

	grid = gd.Grid(10, pieces)
	grid1 = gd.Grid(10, pieces)
	grids = [grid, grid1]
	for i in grids:
		i.init()
		i.definePhysicalLimits()

	player1 = player.Player()
	player2 = player.Player(1)
	players = [player1, player2]

SCREENHEIGHT = 650
SCREENWIDTH = 440
screensize = (SCREENWIDTH, SCREENHEIGHT)

pg.init()

screen = pg.display.set_mode(screensize)
pg.display.set_caption("PyPuzzle")

# MENU RECTS

soloButtonRect = pg.Rect(165, 330, 120, 45)
multiButtonRect = pg.Rect(165, 400, 120, 45)
quitButtonRect = pg.Rect(165, 470, 120, 45)
returnButtonRect = pg.Rect(165, 470, 120, 45)

# GAMEOVER RECTS

#restartButtonRect = pg.Rect()
#quitButtonRectGO = pg.Rect()

# =======

# TESTS
boardX = 50
boardY = 50
boardCoord = (boardX, boardY)

currentDisplay = 'menu'

#===================

doContinue = True

while doContinue:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			quitGame()

		elif event.type == pg.MOUSEBUTTONDOWN:
			if currentDisplay == 'solo' or currentDisplay == 'multi':
				for j in player1.draw:
					if j.rect.collidepoint(event.pos) and not currentlyDragging:
						currentlyDragging = True
						j.dragged = True

		elif event.type == pg.MOUSEBUTTONUP:
			if currentDisplay == 'solo' or currentDisplay == 'multi':
				if currentlyDragging:
					for j in player1.draw:
						if j.rect.collidepoint(event.pos):
							currentlyDragging = False
							j.dragged = False
							if isOnGrid(event.pos):
								gridPos = ((event.pos[0]-boardX)/32+1,(event.pos[1]-boardY)/32+1)
								if grid.isPiecePlaceable(int(gridPos[0]), int(gridPos[1]), j.figureNumber):
									grid.putPiece(int(gridPos[0]), int(gridPos[1]), j.figureNumber)
									player1.draw.remove(j)
<<<<<<< HEAD
				
=======

>>>>>>> bbccc9965c525fb34d416059288f6f57eb26ba1f
			elif currentDisplay == 'menu':
				if soloButtonRect.collidepoint(event.pos):
					currentDisplay = 'solo'
				elif multiButtonRect.collidepoint(event.pos):
					currentDisplay = 'gameMultiLocal'
				elif quitButtonRect.collidepoint(event.pos):
					quitGame() 
				


	#INSTRUCTIONS ===
	if currentDisplay == 'menu':
		dsp.displayMenu(screen)
		nbRound = 0

	elif currentDisplay == 'multiMenu':
		dsp.displayMulti(screen)

	elif currentDisplay == 'onlineMultiMenu':
		dsp.displayOnlineMulti(screen)

	elif currentDisplay == 'solo':
		pass

	elif currentDisplay == 'gameMultiLocal':
		if nbRound == 0:
			initGameMulti()
		if multiView == 'Player1':
			pass
		elif multiView == 'Player2':
			pass



		nbRound+=1

	elif currentDisplay == 'gameover':
		dsp.displayGameOverSolo(screen, player1)

	#================

	pg.display.flip()




