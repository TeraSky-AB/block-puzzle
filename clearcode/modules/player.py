import random as rd

class Player():
	def __init__(self, id=0):
		self.id = id
		self.points = 0
		self.draw = []

	def update(self, pieces):
		if len(self.draw) == 0:
			for i in range(3):
				self.draw.append(pieces.histories[self.id][0])
				pieces.histories[self.id].remove(pieces.histories[self.id][0])