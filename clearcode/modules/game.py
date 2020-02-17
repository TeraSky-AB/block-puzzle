import modules.grid as grd
import modules.pieces as pcs
import modules.player as player
import modules.display as dsp
import random as rnd

class Game:
	def __init__(self, nbPlayer, win):
		self.nbPlayer = nbPlayer

		self.win = win

		self.pieces = pcs.Pieces()

		self.currentPlayer = rnd.randint(0,1)

		self.players = []
		self.grids = []

	def round():
		pass

	def init():
		for i in range(self.nbPlayer):
			self.players.append(grd.Grid(10))
			self.grid.append(player.Player(i))
		for i in self.grids:
			i.init()
			i.definePhysicalLimits()

	def update():
		self.pieces.update(players)
		for i in self.players:
			i.update(self.pieces)
			for j in i.draw:
				j.update(self.win)
		self.grids[self.currentPlayer%2].isThereAlignement()
		self.players[self.currentPlayer%2].points += len(self.grids[self.currentPlayer%2].linesCompleted)*100
		self.grids[self.currentPlayer%2].eraseAlignement()