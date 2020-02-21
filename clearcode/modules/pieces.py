import pygame as pg
import random as rd


class Pieces:
	"""
	Pieces object handles the draws and serves as reference for each piece representation on Grid object
	"""
	def __init__(self):
		self.pieces = (
			('00000','00000','00100','00000','00000'), # 0  : Unity block
			('00000','00000','00110','00000','00000'), # 1  : 2 line horizontal
			('00000','00100','00100','00000','00000'), # 2  : 2 line vertical
			('00000','00000','01110','00000','00000'), # 3  : 3 line horizontal
			('00000','00100','00100','00100','00000'), # 4  : 3 line vertical
			('00000','00000','01100','00100','00000'), # 5  : Comma normal
			('00000','00000','00110','00100','00000'), # 6  : Comma right
			('00000','00100','00110','00000','00000'), # 7  : Comma up right
			('00000','00100','01100','00000','00000'), # 8  : Comma up left
			('00000','00000','00110','00110','00000'), # 9  : 2x2 block
			('00000','01110','01110','01110','00000'), # 10  : 3x3 block
			('00000','00000','11110','00000','00000'), # 11  : 4 line horizontal
			('00000','00100','00100','00100','00100'), # 12  : 4 line vertical
			('00000','00000','11111','00000','00000'), # 13  : 5 line
			('00100','00100','00100','00100','00100'), # 14 : 5 line vertical
			('00000','00000','11100','00100','00100'), # 15  : Big comma normal
			('00100','00100','11100','00000','00000'), # 16  : Big comma up left
			('00000','00000','00111','00100','00100'), # 17  : Big comma normal right
			('00100','00100','00111','00000','00000'), # 18  : Big comma up right
			('00000','00000','01100','00100','00100'), # 19  : Logical not figure
			('00000','00000','00110','00100','00100'), # 20  : Logical not figure
			('00100','00100','01100','00000','00000'), # 21  : Logical not figure
			('00100','00100','00110','00000','00000'), # 22  : Logical not figure
			('00000','00000','01100','00110','00000'), # 23 : Snake look alike
			('00000','00000','01100','01100','00000'), # 24 : Snake look alike
			('00000','00100','00110','00010','00000'), # 25 : Snake look alike
			('00000','00010','01100','00100','00000'), # 26 : Snake look alike
			('00000','00000','01110','00100','00100'), # 27 : T figure
			('00100','00100','01110','00000','00000'), # 28 : T figure
			('00000','00100','00111','00100','00000'), # 29 : T figure
			('00000','00100','11100','00100','00000'), # 30 : T figure
		)

		self.piece_colors = (240,247,244) #cream

		self.level = 0
		self.stage = 200
		self.steps = [12,18,22,26,30]

		self.history = []
		self.history2 = []
		self.histories = [self.history, self.history2]

	def update(self, Players):
		"""
		update() updates Pieces object by checking if history property is empty so they can fulfill it and manage the
		draw difficulties.
		:param Players: Player object(needed to check Player points)
		"""
		if len(self.history) == 0 or len(self.history2) == 0:
			for i in range(3):
				randFigure = rd.randint(0, self.steps[self.level])
				self.history.append(Piece(randFigure, self.piece_colors))
				self.history2.append(Piece(randFigure, self.piece_colors))
		for j in Players:
			if j.points // self.stage > 5 and self.level < 4:
				self.level += 1
				self.stage *= 1.25


class Piece(Pieces):
	"""
	Piece object represent the piece inside and outside the game board.
	"""
	def __init__(self, figure, color):
		Pieces.__init__(self)
		self.x = -300
		self.y = 600
		self.figureNumber = figure
		self.figure = self.pieces[figure]
		self.color = color
		self.dragged = False
		self.rect = pg.Rect(self.x, self.y, 160, 160)

	def drawPiece(self, win):
		"""

		:param win:
		"""
		for i in range(5):
			for j in range(5):
				if int(self.figure[i][j]):
					pg.draw.rect(win, self.color, (self.x+(32)*i+2,self.y+(32)*j+2, 30, 30))

	def update(self, win):
		"""

		:param win:
		"""
		mousePos = pg.mouse.get_pos()
		if self.dragged:
			self.x = mousePos[0]-80
			self.y = mousePos[1]-80
		self.rect.x = self.x
		self.rect.y = self.y

