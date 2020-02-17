import pygame as pg

BACKGROUNDCOLOR = (150, 211, 255)
BOARDCOLOR = (102, 174, 232)
CREAM = (240, 247, 244)
REDPINK = (255, 143, 137, 200)
GREEN = (34,199,139)
BLACK = (0,0,0)

margin = 2

pg.font.init()
font = pg.font.Font('assets/BebasNeue-Regular.ttf', 20)
mediumFont = pg.font.Font('assets/BebasNeue-Regular.ttf', 70)
bigFont = pg.font.Font('assets/BebasNeue-Regular.ttf', 100)
bigMediumFont = pg.font.Font('assets/BebasNeue-Regular.ttf', 50)

quit = mediumFont.render("Quit", True, BLACK)
restart = mediumFont.render("Restart", True, BLACK)
gameover = bigFont.render("GAME OVER", True, BLACK)

pypuzzle = bigFont.render("PyPuzzle", True, CREAM)
soloText = mediumFont.render("SOLO", True, CREAM)
multiText = mediumFont.render("MULTI", True, CREAM)
quitText = mediumFont.render("QUIT", True, CREAM)

multiplayerText = mediumFont.render("MULTIPLAYER", True, CREAM)
iaText = bigMediumFont.render("PLAYER vs IA", True, CREAM)
localText = bigMediumFont.render("PLAYER 1 vs PLAYER 2 (LOCAL)", True, CREAM)
onlineText = bigMediumFont.render("PLAYER 1 vs PLAYER 2 (ONLINE)", True, CREAM)
returnText = bigMediumFont.render("RETURN", True, CREAM)

hostText = mediumFont.render("HOST GAME", True, CREAM)
joinText = mediumFont.render("JOIN GAME", True, CREAM)

def displayMenu(win):
	pass

def displayMulti(win):
	win.fill(BACKGROUNDCOLOR)
	win.blit(multiplayerText, (65,50))
	win.blit(iaText, (25,220))
	win.blit(localText, (25,300))
	win.blit(onlineText, (25, 380))
	win.blit(returnText, (150, 460))

def displayOnlineMulti(win):
	win.fill(BACKGROUNDCOLOR)
	win.blit(multiplayerText, (65,50))
	win.blit(hostText, (160,220))
	win.blit(joinText, (150,300))

def displayBoard(win, blitCoord, grid):
	boxWidth = 30
	win.fill(BACKGROUNDCOLOR)
	for i in range(0,grid.size-2):
		for j in range(0,grid.size-2):
			if grid.grid[1+i][1+j]:
				pg.draw.rect(win, CREAM, (blitCoord[0]+(margin+boxWidth)*i+margin,blitCoord[1]+(margin+boxWidth)*j+margin, boxWidth, boxWidth))
			else:
				pg.draw.rect(win, BOARDCOLOR, (blitCoord[0]+(margin+boxWidth)*i+margin,blitCoord[1]+(margin+boxWidth)*j+margin, boxWidth, boxWidth))


def displayDrawPieces(Player): #Changer le titre (la position de la fonction ?)
	j = 0
	for i in Player.draw:
		if not i.dragged:
			i.x = j
			i.y = 400
			j+=150

def displayTexts(win, Player):
	score = font.render("Score: "+str(Player.points), True, CREAM)
	win.blit(score, (10,10))
	currentPlayer = font.render("Current player: "+str(Player.id+1), True, CREAM)
	win.blit(currentPlayer, (310,10))		

def displayGameOverSolo(win, Player):
	win.fill(REDPINK)
	score = mediumFont.render("Score: "+str(Player.points), True, BLACK)
	win.blit(score, (125, 90))
	win.blit(gameover, (50, 200))
	win.blit(restart, (125, 335))
	win.blit(quit, (175, 410))
					

