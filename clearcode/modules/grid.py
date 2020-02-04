class Grid():
	def __init__(self, size):
		self.size = size+2
		self.grid = []
		self.pieces = (
			('00000','00000','00100','00000','00000'), # 0  : Unity block
			('00000','00000','00110','00000','00000'), # 1  : 2 line
			('00000','00000','01110','00000','00000'), # 2  : 3 line
			('00000','00000','01100','00100','00000'), # 3  : Comma
			('00000','00110','00110','00000','00000'), # 4  : 2x2 block
			('00000','00000','11110','00000','00000'), # 5  : 4 line
			('00000','00000','11111','00000','00000'), # 6  : 5 line
			('00000','01110','01110','01110','00000'), # 7  : 3x3 block
			('00000','00000','11100','00100','00100'), # 8  : Big comma
			('00000','00000','01100','00100','00100'), # 9  : Logical not figure
			('00000','00000','01100','00110','00000'), # 10 : Snake look alike
			('00000','00000','01110','00100','00000'),  # 11 : T figure
		)

		self.linesCompleted = []

	def init(self):
		for i in range(self.size):
			self.grid.append([])
			for j in range(self.size):
				self.grid[i].append(0)

	def printGridState(self):
		for i in self.grid:
			print(i)

	def definePhysicalLimits(self):
		for i in range(self.size):
			self.grid[i][0] = 1
			self.grid[0][i] = 1
			self.grid[self.size-1][i] = 1
			self.grid[i][self.size-1] = 1

	def isPiecePlaceable(self, x, y, piece, orientation):
		x -= 2
		y -= 2
		err = 0
		for i in range(5):
			for j in range(5):
					if orientation == 0 and not lg.nand(self.grid[x+i][y+j],int(self.pieces[figure][i][j])):
						err += 1
					elif orientation == 1 and not lg.nand(self.grid[x+i][y+j],int(self.pieces[figure][j][i])):
						err += 1
					elif orientation == 2 and not lg.nand(self.grid[x+i][y+j],int(self.pieces[figure][-i][-j])):
						err += 1
					elif orientation == 3 and not lg.nand(self.grid[x+i][y+j],int(self.pieces[figure][-j][-i])):
						err += 1
		if err:
			return False
		else:
			return True

	def putPiece(self, x, y, piece, orientation):
		x -= 2
		y -= 2
		for i in range(5):
			for j in range(5):
				if orientation == 0:
					try:
						self.grid[x+i][y+j] += int(self.pieces[piece][i][j])
					except:
						print("Block outside array's range")
				elif orientation == 1:
					try:
						self.grid[x+i][y+j] += int(self.pieces[piece][j][i])
					except:
						print("Block outside array's range")
				elif orientation == 2:
					try:
						self.grid[x+i][y+j] += int(self.pieces[piece][-i][-j])
					except:
						print("Block outside array's range")
				elif orientation == 3:
					try:
						self.grid[x+i][y+j] += int(self.pieces[piece][-j][-i])
					except:
						print("Block outside array's range")

	def isThereAlignement(self):
		pass




grid = Grid(10)
grid.init()
grid.definePhysicalLimits()
grid.printGridState()
for i in range(10):
	grid.putPiece(i+1,5,0,0)
grid.printGridState()
grid.isThereAlignement()
print(grid.linesCompleted)



			
