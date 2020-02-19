import pygame as pg
import random as rnd
import modules.grid as gd
import modules.display as dsp
import modules.player as player
import modules.pieces as pcs
import modules.functions as fnc


def updates(pieces, players, grids, screen, currentPlayer):  # Update player draw and check if grid has alignements
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
    # WINDOW VARIABLES
    screenheight = 650
    screenwidth = 440
    screensize = (screenwidth, screenheight)

    pg.init()

    screen = pg.display.set_mode(screensize)
    pg.display.set_caption("PyPuzzle")
    # ================

    # MENU RECT ======

    restartRect = pg.Rect(179, 404, 140, 70)
    quitRect = pg.Rect(202, 474, 120, 70)

    # ================
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

    boardX = 50
    boardY = 50

    stop = False
    while not stop:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                fnc.quitGame()

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
                elif currentDisplay == 'gamover':
                    if restartRect.collidepoint(event.pos):
                        print("Restart")
                        multiLocal()
                    elif quitRect.collidepoint(event.pos):
                        print("Quit")
                        fnc.quitGame()

        # INSTRUCTIONS OF LOOP ===
        if currentDisplay == 'game':
            dsp.displayBoard(screen, (boardX, boardY), grids[currentPlayer % 2])
            updates(pieces, players, grids, screen, currentPlayer)
            dsp.displayDrawPieces(players[currentPlayer % 2])
            dsp.displayTexts(screen, players[currentPlayer % 2])
            if not grids[currentPlayer % 2].isDrawPlaceable(players[currentPlayer % 2]):
                currentDisplay = 'gameover'
        elif currentDisplay == 'gameover':
            dsp.displayGameOverMulti(screen, players[currentPlayer%2])

        pg.display.flip()
        # ========================


multiLocal()
