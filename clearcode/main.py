import pygame as pg
import modules.grid as gd
import modules.display as dsp
import modules.player as player
import modules.pieces as pcs

SCREENHEIGHT = 700
SCREENWIDTH = 450
screensize = (SCREENWIDTH, SCREENHEIGHT)

boardX = 65
boardY = 65
currentDisplay = None
pieces = pcs.Pieces()
grid = gd.Grid(10, pieces)
grid.init()
grid.definePhysicalLimits()
player1 = player.Player()
players = [player1]

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

pg.init()

screen = pg.display.set_mode(screensize)
pg.display.set_caption("PyPuzzle")

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

def menu():
	dsp.displayMenu(screen)
	doContinue = True
	while doContinue:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				quitGame()
			elif event.type == pg.MOUSEBUTTONDOWN:
				if soloButtonRect.collidepoint(event.pos):
					main()
				if multiButtonRect.collidepoint(event.pos):
					multiMenu()
				if quitButtonRect.collidepoint(event.pos):
					quitGame()
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
				quitGame()
			elif event.type == pg.MOUSEBUTTONDOWN:
				if returnButtonRect.collidepoint(event.pos):
					menu()
		# HOVER
		pos = pg.mouse.get_pos()	
		if 150+150 > pos[0] > 150 and 448+45 > pos[1] > 448:
			pg.draw.rect(screen, YELLOW, (150, 448, 150, 45))
			screen.blit(returnText, (179, 448))
		else:
			pg.draw.rect(screen, REDPINK, (150, 448, 150, 45))
			screen.blit(returnText, (179, 448))
		pg.display.flip()

def gameOver():
	dsp.displayGameOverSolo(screen, player1)
	doContinue = True
	while doContinue:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				quitGame()	
			elif event.type == pg.MOUSEBUTTONDOWN:
				if restartButtonRect.collidepoint(event.pos):
					main()
				if quitButtonRect.collidepoint(event.pos):
					quitGame()
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

def main():
	currentDisplay = 'solo'
	currentlyDragging = False
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
				if returnMenuButtonRect.collidepoint(event.pos):
					menu()

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
		if currentDisplay == 'solo':
			dsp.displayBoard(screen, (boardX, boardY), grid)
			updates()
			dsp.displayDrawPieces(player1)
			dsp.displayTexts(screen, player1)
			if not grid.isDrawPlaceable(player1):
				gameOver()
		
		# HOVER
		pos = pg.mouse.get_pos()
		if 340+85 > pos[0] > 340 and 645+30 > pos[1] > 645:
			pg.draw.rect(screen, YELLOW, (340, 645, 85, 30))
			screen.blit(returnMenuText, (354, 647))
		else:
			pg.draw.rect(screen, GRAY, (340, 645, 85, 30))
			screen.blit(returnMenuText1, (354, 647))



		pg.display.flip()

if __name__ == '__main__':
	menu()


