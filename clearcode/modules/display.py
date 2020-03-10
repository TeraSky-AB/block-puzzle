import pygame as pg

# piecescolors = (
#     (0, 0, 0),  # PREVENT A BUG
#     (254, 235, 201),  # CREAM
#     (255, 143, 137),  # REDPINK
#     (141, 232, 150),  # GREEN
#     (255, 250, 129),  # YELLOW
#     (255, 0, 0),  # RED
#     (192, 187, 153),  # GRAY
#     (165, 137, 193),  # NAVY
# )

piecescolors = (
    (0, 0, 0),  # PREVENT A BUG
    (255, 241, 171),  # PASTEL YELLOW
    (255, 196, 196),  # PASTEL RED
    (161, 255, 170),  # PASTEL GREEN
    (186, 238, 255),  # PASTEL BLUE
    (166, 255, 236),  # GREEN MINT
    (240, 247, 244),  # CREAM
    (255, 214, 239)  # PASTEL PINK
)

BACKGROUNDCOLOR = (125, 201, 255)
BOARDCOLOR = (77, 164, 227)
CREAM = (240, 247, 244)
REDPINK = (255, 143, 137)
GREEN = (141, 232, 150)
NAVY = (7, 51, 92)
YELLOW = (255, 207, 74)
GRAY = (41, 41, 41)
RED = (219, 109, 103)
PINK = (255, 214, 239)
BLUE = (85, 169, 237)
LIGHTBLUE = (186, 233, 255)

margin = 2

pg.font.init()
font = pg.font.Font('assets/BebasNeue-Regular.ttf', 25)
bigFont = pg.font.Font('assets/BebasNeue-Regular.ttf', 100)
bigMediumFont = pg.font.Font('assets/BebasNeue-Regular.ttf', 60)
mediumFont = pg.font.Font('assets/BebasNeue-Regular.ttf', 40)
smallFont = pg.font.Font('assets/BebasNeue-Regular.ttf', 25)

gameover = bigFont.render("YOUR SCORE", True, GRAY)
gameoverShadow = bigFont.render("YOUR SCORE", True, RED)

J1 = font.render("Joueur 1 : ", True, GRAY)
J2 = font.render("Joueur 2 : ", True, GRAY)
Winner = mediumFont.render("Winner : ", True, GRAY)

pypuzzle = bigFont.render("PyPuzzle", True, NAVY)
pypuzzleShadow = bigFont.render("PyPuzzle", True, BOARDCOLOR)

multiplayerText = bigMediumFont.render("MULTIPLAYER", True, NAVY)
iaText = mediumFont.render("PLAYER vs IA", True, NAVY)
localText = mediumFont.render("PLAYER 1 vs PLAYER 2 (LOCAL)", True, NAVY)
onlineText = mediumFont.render("PLAYER 1 vs PLAYER 2 (ONLINE)", True, NAVY)

iaTextHover = mediumFont.render("PLAYER vs IA", True, RED)
localTextHover = mediumFont.render("PLAYER 1 vs PLAYER 2 (LOCAL)", True, RED)
onlineTextHover = mediumFont.render("PLAYER 1 vs PLAYER 2 (ONLINE)", True, RED)
returnText = font.render("RETURN", True, NAVY)
multiplayerTextShadow = bigMediumFont.render("MULTIPLAYER", True, BOARDCOLOR)

hostText = mediumFont.render("HOST GAME", True, CREAM)
joinText = mediumFont.render("JOIN GAME", True, CREAM)

soloText = mediumFont.render("SOLO", True, NAVY)
multiText = mediumFont.render("MULTI", True, NAVY)
quitText = mediumFont.render("QUIT", True, NAVY)
returnText = mediumFont.render("RETURN", True, NAVY)
quitText1 = mediumFont.render("Quit", True, GRAY)
restart = mediumFont.render("Restart", True, GRAY)
returnMenuText = smallFont.render("RETURN", True, NAVY)
returnMenuText1 = smallFont.render("RETURN", True, CREAM)


def displayMenu(win):
    win.fill(BACKGROUNDCOLOR)
    pg.draw.rect(win, BOARDCOLOR, (155, 323, 150, 45))
    pg.draw.rect(win, BOARDCOLOR, (155, 388, 150, 45))
    pg.draw.rect(win, BOARDCOLOR, (155, 453, 150, 45))

    win.blit(pypuzzleShadow, (82, 170))
    win.blit(pypuzzle, (78, 165))

    pg.draw.rect(win, LIGHTBLUE, (0, 610, 450, 30))
    pg.draw.rect(win, BLUE, (0, 640, 450, 30))
    pg.draw.rect(win, NAVY, (0, 670, 450, 30))

def displayMulti(win):
    win.fill(BACKGROUNDCOLOR)
    win.blit(multiplayerTextShadow, (103, 73))
    win.blit(multiplayerText, (100, 70))
    pg.draw.rect(win, BOARDCOLOR, (155, 453, 150, 45))

    pg.draw.rect(win, LIGHTBLUE, (0, 610, 450, 30))
    pg.draw.rect(win, BLUE, (0, 640, 450, 30))
    pg.draw.rect(win, NAVY, (0, 670, 450, 30))

def displayOnlineMulti(win):
    win.fill(BACKGROUNDCOLOR)
    win.blit(multiplayerText, (65, 50))
    win.blit(hostText, (160, 220))
    win.blit(joinText, (150, 300))


def displayBoard(win, blitCoord, grid):
    boxWidth = 30
    win.fill(BACKGROUNDCOLOR)
    # grid.printGridState()
    for i in range(0, grid.size - 2):
        for j in range(0, grid.size - 2):
            cell = grid.grid[1 + i][1 + j]
            if cell != 0:
                pg.draw.rect(win, piecescolors[cell], (
                    blitCoord[0] + (margin + boxWidth) * i + margin, blitCoord[1] + (margin + boxWidth) * j + margin,
                    boxWidth, boxWidth))
            else:
                pg.draw.rect(win, BOARDCOLOR, (
                    blitCoord[0] + (margin + boxWidth) * i + margin, blitCoord[1] + (margin + boxWidth) * j + margin,
                    boxWidth, boxWidth))

    pg.draw.rect(win, NAVY, (0, 670, 450, 30))
    pg.draw.rect(win, BOARDCOLOR, (345, 620, 85, 30))


def displayDrawPieces(Player):  # Changer le titre (la position de la fonction ?)
    j = 0
    for i in Player.draw:
        if not i.dragged:
            i.x = j
            i.y = 400
            j += 140


def displayTexts(win, Player):
    score = font.render("Score: " + str(Player.points), True, NAVY)
    win.blit(score, (20, 20))
    currentPlayer = font.render("Current player: " + str(Player.id + 1), True, NAVY)
    win.blit(currentPlayer, (280, 20))

def displayGameOverSolo(win, Player):
    win.fill(REDPINK)
    score = bigMediumFont.render(str(Player.points), True, GRAY)
    win.blit(score, (180, 288))
    win.blit(gameoverShadow, (45, 170))
    win.blit(gameover, (40, 165))

    pg.draw.rect(win, RED, (155, 388, 150, 45))
    pg.draw.rect(win, RED, (155, 453, 150, 45))

def displayGameOverIA(win, Players):
    win.fill(REDPINK)
    score1 = font.render(str(Players.points), True, GRAY)
    win.blit(score1, (140, 253))
    win.blit(gameoverShadow, (45, 135))
    win.blit(gameover, (40, 130))
    
    win.blit(J1, (50, 253))
    win.blit(J2, (270, 253))
    score2 = bigMediumFont.render(str(Players2.points), True, GRAY)
    win.blit(score2, (350, 253))
    
    win.blit(Winner, (140, 300))
    
    pg.draw.rect(win, RED, (155, 388, 150, 45))
    pg.draw.rect(win, RED, (155, 453, 150, 45))
