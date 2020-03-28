import pygame as pg
import random as rd
import modules.display as dsp


class Pieces:
    """
    Class used as reference for pieces and determine draws
    """
    def __init__(self):
        self.pieces = (
            ['00000', '00000', '00100', '00000', '00000'],  # 0  : Unity block
            ['00000', '00000', '00110', '00000', '00000'],  # 1  : 2 line horizontal
            ['00000', '00000', '00100', '00100', '00000'],  # 2  : 2 line vertical
            ['00000', '00000', '01110', '00000', '00000'],  # 3  : 3 line horizontal
            ['00000', '00100', '00100', '00100', '00000'],  # 4  : 3 line vertical
            ['00000', '00000', '01100', '00100', '00000'],  # 5  : Comma normal
            ['00000', '00000', '00110', '00100', '00000'],  # 6  : Comma right
            ['00000', '00000', '00100', '00110', '00000'],  # 7  : Comma up right
            ['00000', '00000', '00100', '01100', '00000'],  # 8  : Comma up left
            ['00000', '00000', '00110', '00110', '00000'],  # 9  : 2x2 block
            ['00000', '01110', '01110', '01110', '00000'],  # 10  : 3x3 block
            ['00000', '00000', '01111', '00000', '00000'],  # 11  : 4 line horizontal
            ['00000', '00100', '00100', '00100', '00100'],  # 12  : 4 line vertical
            ['00000', '00000', '11111', '00000', '00000'],  # 13  : 5 line
            ['00100', '00100', '00100', '00100', '00100'],  # 14 : 5 line vertical
            ['00000', '11100', '00100', '00100', '00000'],  # 15  : Big comma normal
            ['00000', '00100', '00100', '11100', '00000'],  # 16  : Big comma up left
            ['00000', '00111', '00100', '00100', '00000'],  # 17  : Big comma normal right
            ['00000', '00100', '00100', '00111', '00000'],  # 18  : Big comma up right
            ['00000', '01100', '00100', '00100', '00000'],  # 19  : Logical not figure
            ['00000', '00110', '00100', '00100', '00000'],  # 20  : Logical not figure
            ['00000', '00100', '00100', '01100', '00000'],  # 21  : Logical not figure
            ['00000', '00100', '00100', '00110', '00000'],  # 22  : Logical not figure
            ['00000', '00000', '01100', '00110', '00000'],  # 23 : Snake look alike
            ['00000', '00000', '01100', '01100', '00000'],  # 24 : Snake look alike
            ['00000', '00100', '00110', '00010', '00000'],  # 25 : Snake look alike
            ['00000', '00010', '00110', '00100', '00000'],  # 26 : Snake look alike
            ['00000', '01110', '00100', '00100', '00000'],  # 27 : T figure
            ['00000', '00100', '00100', '01110', '00000'],  # 28 : T figure
            ['00000', '00100', '00111', '00100', '00000'],  # 29 : T figure
            ['00000', '00100', '11100', '00100', '00000']  # 30 : T figure
        )

        self.probs = [[8.5, 22.5, 39, 55.5, 72, 84.5, 100, 200, 200, 200, 200, 200, 200, 200],
                      [8.5, 20.5, 33.5, 48, 63, 73, 83, 92, 100, 200, 200, 200, 200, 200],
                      [6.5, 17, 28.5, 41.5, 54, 63.5, 73, 80.5, 87, 93.5, 100, 200, 200, 200],
                      [5.5, 15, 27, 39.5, 51, 59.5, 68, 76.5, 83, 89.5, 95, 100, 200],
                      [5.5, 13, 24.5, 36, 46.5, 55, 63.5, 71, 77.5, 84, 89.5, 95, 100]]

        self.level = 0
        self.stage = 200
        self.steps = 0

        self.history = []
        self.history2 = []
        self.histories = [self.history, self.history2]

    def alea(self):
        """
        alea() function determine random piece.
        @return: Return the piece to add to the player's draw.
        """
        nb = rd.randint(0, 100)
        figure = 0
        for i in range(0, 12):
            if nb <= self.probs[self.steps][0]:
                figure = 1
            elif nb > self.probs[self.steps][i] and nb <= self.probs[self.steps][i + 1]:
                figure = i + 2
        return figure

    def update(self, Players):
        """
        update() method checks if history is empty in order to fulfill it and check if the level must be increased.
        @param Players: Players object list.
        """
        if len(self.history) == 0 or len(self.history2) == 0:
            for i in range(3):
                randFigure = self.alea()
                randColor = rd.randint(1, 7)
                self.history.append(Piece(randFigure, randColor))
                self.history2.append(Piece(randFigure, randColor))
        for j in Players:
            if j.points // self.stage > 5 and self.steps < 4:
                self.steps += 1
                self.stage *= 1.25


class Piece(Pieces):  # Piece to place on the grid
    """
    Single piece object.
    """
    def __init__(self, figure, color):
        Pieces.__init__(self)
        self.color = dsp.piecescolors[color]
        self.figureNumber = figure
        self.color = color
        self.figure = self.applyColor(figure)
        self.x = -500
        self.y = 500
        self.dragged = False
        self.rect = pg.Rect(self.x, self.y, 160, 160)

    def repair(self, string):
        """
        repair() method rebuild the string after applyColor call.
        @param string: string to repair
        @return: repaired string
        """
        stringLength = len(string)
        backup = string
        if stringLength != 5:
            string = '0'
            for i in range(4 - stringLength):
                string += '0'
            string += backup
        return string

    def applyColor(self, figure):
        """
        Change the value of the piece to define color on board.
        @param figure: Figure to change value on
        @return: figure with values changed
        """
        piece = self.pieces[figure]
        for i in range(5):
            piece[i] = int(piece[i])
            piece[i] *= self.color
            piece[i] = str(piece[i])
            piece[i] = self.repair(piece[i])
        return piece

    def drawPiece(self, win):
        """
        drawPiece() displays the piece on the screen.
        @param win: Pygame window surface.
        """
        for i in range(5):
            for j in range(5):
                if int(self.figure[i][j]) != 0:
                    pg.draw.rect(win, dsp.piecescolors[self.color], (self.x + 32 * i + 2, self.y + 32 * j + 2, 30, 30))

    def update(self, win):
        """
        update() method updates coordinates.
        @param win: Pygame window surface.
        """
        mousePos = pg.mouse.get_pos()
        if self.dragged:
            self.x = mousePos[0] - 80
            self.y = mousePos[1] - 80
        self.rect.x = self.x
        self.rect.y = self.y
