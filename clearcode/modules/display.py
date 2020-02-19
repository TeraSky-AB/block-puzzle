import pygame as pg

BACKGROUNDCOLOR = (150, 211, 255)
BOARDCOLOR = (102, 174, 232)
CREAM = (240, 247, 244)
REDPINK = (255, 143, 137, 200)
GREEN = (34,199,139)
NAVY = (37,80,108)
YELLOW = (255, 207, 74)
GRAY = (41, 41, 41)
RED = (219, 109, 103)

margin = 2

pg.font.init()
font = pg.font.Font('assets/BebasNeue-Regular.ttf', 20)
mediumFont = pg.font.Font('assets/BebasNeue-Regular.ttf', 35)
bigFont = pg.font.Font('assets/BebasNeue-Regular.ttf', 100)
bigMediumFont = pg.font.Font('assets/BebasNeue-Regular.ttf', 60)

quit = mediumFont.render("Quit", True, GRAY)
restart = mediumFont.render("Restart", True, GRAY)
gameover = bigFont.render("GAME OVER", True, GRAY)
gameoverShadow = bigFont.render("GAME OVER", True, RED)


pypuzzle = bigFont.render("PyPuzzle", True, NAVY)
soloText = mediumFont.render("SOLO", True, NAVY)
multiText = mediumFont.render("MULTI", True, NAVY)
quitText = mediumFont.render("QUIT", True, NAVY)
pypuzzleShadow = bigFont.render("PyPuzzle", True, BOARDCOLOR)


multiplayerText = bigMediumFont.render("MULTIPLAYER", True, NAVY)
iaText = mediumFont.render("PLAYER vs IA", True, NAVY)
localText = mediumFont.render("PLAYER 1 vs PLAYER 2 (LOCAL)", True, NAVY)
onlineText = mediumFont.render("PLAYER 1 vs PLAYER 2 (ONLINE)", True, NAVY)
returnText = mediumFont.render("RETURN", True, NAVY)
multiplayerTextShadow = bigMediumFont.render("MULTIPLAYER", True, BOARDCOLOR)


hostText = mediumFont.render("HOST GAME", True, CREAM)
joinText = mediumFont.render("JOIN GAME", True, CREAM)



def displayMenu(win):
	win.fill(BACKGROUNDCOLOR)
	
	pg.draw.rect(win, BOARDCOLOR, (170, 335, 120, 45))
	pg.draw.rect(win, CREAM, (165, 330, 120, 45))

	pg.draw.rect(win, BOARDCOLOR, (170, 405, 120, 45))
	pg.draw.rect(win, GREEN, (165, 400, 120, 45))


	pg.draw.rect(win, BOARDCOLOR, (170, 475, 120, 45))
	pg.draw.rect(win, REDPINK, (165, 470, 120, 45))

	win.blit(pypuzzleShadow, (80,75))
	win.blit(pypuzzle, (75,70))
	win.blit(soloText, (199,334))
	win.blit(multiText, (192,404))
	win.blit(quitText, (202, 474))

def displayMulti(win):
	win.fill(BACKGROUNDCOLOR)
	win.blit(multiplayerTextShadow, (103,73))
	win.blit(multiplayerText, (100,70))

	win.blit(iaText, (50,180))
	win.blit(localText, (50,230))
	win.blit(onlineText, (50, 280))

	pg.draw.rect(win, BOARDCOLOR, (170, 475, 120, 45))
	pg.draw.rect(win, REDPINK, (165, 470, 120, 45))
	win.blit(returnText, (184, 474))

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
				pg.draw.rect(win, CREAM, (blitCoord[0]+(margin+boxWidth)*i+margin, blitCoord[1]+(margin+boxWidth)*j+margin, boxWidth, boxWidth))
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
	score = font.render("Score: "+str(Player.points), True, NAVY)
	win.blit(score, (10,10))
	currentPlayer = font.render("Current player: "+str(Player.id+1), True, NAVY)
	win.blit(currentPlayer, (310,10))		

def displayGameOverSolo(win, Player):
	win.fill(REDPINK)
	score = bigMediumFont.render("Score: "+str(Player.points), True, GRAY)
	win.blit(score, (120, 245))
	win.blit(gameoverShadow, (55, 75))
	win.blit(gameover, (50, 70))

	pg.draw.rect(win, RED, (170, 405, 120, 45))
	pg.draw.rect(win, BACKGROUNDCOLOR, (165, 400, 120, 45))
	win.blit(restart, (179, 404))

	pg.draw.rect(win, RED, (170, 475, 120, 45))
	pg.draw.rect(win, YELLOW, (165, 470, 120, 45))
	win.blit(quit, (202, 474))

def displayGameOverMulti(win, Player): # A modifier(Afficher les deux scores ainsi que le gagnant)
	win.fill(REDPINK)
	score = bigMediumFont.render("Score: " + str(Player.points), True, GRAY)
	win.blit(score, (120, 245))
	win.blit(gameoverShadow, (55, 75))
	win.blit(gameover, (50, 70))

	pg.draw.rect(win, RED, (170, 405, 120, 45))
	pg.draw.rect(win, BACKGROUNDCOLOR, (165, 400, 120, 45))
	win.blit(restart, (179, 404))

	pg.draw.rect(win, RED, (170, 475, 120, 45))
	pg.draw.rect(win, YELLOW, (165, 470, 120, 45))
	win.blit(quit, (202, 474))
					

