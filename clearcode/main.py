import pygame as pg
import modules.grid as gd
import modules.display as dsp
import modules.player as player
import modules.pieces as pcs

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

SCREENHEIGHT = 650
SCREENWIDTH = 440
screensize = (SCREENWIDTH, SCREENHEIGHT)

pg.init()

screen = pg.display.set_mode(screensize)
pg.display.set_caption("PyPuzzle")

# MENU RECTS

soloButtonRect = pg.Rect(160,220,130,70)
multiButtonRect = pg.Rect(150,300,140,70)
quitButtonRect = pg.Rect(155,380,125,70)

# GAMEOVER RECTS

#restartButtonRect = pg.Rect()
#quitButtonRectGO = pg.Rect()

# =======

# TESTS
boardX = 50
boardY = 50

currentDisplay = 'menu'

currentlyDragging = False
pieces = pcs.Pieces()
grid = gd.Grid(10, pieces)
grid.init()
grid.definePhysicalLimits()
player1 = player.Player()
players = [player1]

#==============

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
			elif currentDisplay == 'menu':
				if soloButtonRect.collidepoint(event.pos):
					currentDisplay = 'solo'
				elif multiButtonRect.collidepoint(event.pos):
					currentDisplay = 'multiMenu'
				elif quitButtonRect.collidepoint(event.pos):
					quitGame() 
				


	#INSTRUCTIONS ===
	if currentDisplay == 'menu':
		dsp.displayMenu(screen)

	elif currentDisplay == 'multiMenu':
		dsp.displayMulti(screen)

	elif currentDisplay == 'onlineMultiMenu':
		dsp.displayOnlineMulti(screen)

	elif currentDisplay == 'solo':
		dsp.displayBoard(screen, (boardX, boardY), grid)
		updates()
		dsp.displayDrawPieces(player1)
		dsp.displayTexts(screen, player1)
		if not grid.isDrawPlaceable(player1):
			currentDisplay = 'gameover'

	elif currentDisplay == 'gameover':
		dsp.displayGameOverSolo(screen, player1)

	#================

	pg.display.flip()




