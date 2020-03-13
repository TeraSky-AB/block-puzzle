import modules.logicalgate as lg


class Grid:
    def __init__(self, size, Pieces):  # Vérifier comment faire le lien entre le grille, les pièces et le joueur
        self.size = size + 2
        self.grid = []

        self.Pieces = Pieces

        self.linesCompleted = []

    def init(self):  # Create a new grid
        for i in range(self.size):
            self.grid.append([])
            for j in range(self.size):
                self.grid[i].append(0)

    def printGridState(self):  # To check the state of the grid on the console
        for i in self.grid:
            print(i)

    def definePhysicalLimits(self):  # Define limits of the board by placing 1s all around the grid
        for i in range(self.size):
            self.grid[i][0] = 1
            self.grid[0][i] = 1
            self.grid[self.size - 1][i] = 1
            self.grid[i][self.size - 1] = 1

    def isPiecePlaceable(self, x, y, figure):  # Check if piece is placeable
        x -= 2
        y -= 2
        err = 0
        for i in range(5):
            for j in range(5):
                try:
                    if not lg.nand(self.grid[x + i][y + j]//self.grid[x+i][y+j], int(self.Pieces.pieces[figure][i][j])):
                        err += 1
                except:
                    pass
        if err:
            return False
        else:
            return True

    def putPiece(self, x, y, Piece):  # Place the piece on the grid
        x -= 2
        y -= 2
        for i in range(5):
            for j in range(5):
                try:
                    self.grid[x + i][y + j] += int(Piece.figure[i][j])
                except:
                    pass

    def isThereAlignement(self):  # Check if there is an alignement on the grid object
        for i in range(self.size - 2):
            line = 0
            column = 0
            for j in range(self.size - 2):
                if self.grid[1 + i][1 + j]:
                    line += 1
                if self.grid[1 + j][1 + i]:
                    column += 1
            if line == self.size - 2:
                self.linesCompleted.append(['r', 1 + i])
            if column == self.size - 2:
                self.linesCompleted.append(['c', 1 + i])

    def eraseAlignement(self):  # Erase the alignements of the grid object
        for i in self.linesCompleted:
            if i[0] == 'c':
                for j in range(self.size - 2):
                    self.grid[1 + j][i[1]] = 0
            if i[0] == 'r':
                for j in range(self.size - 2):
                    self.grid[i[1]][1 + j] = 0
            self.linesCompleted.remove(i)

    def isDrawPlaceable(self, Player):
        err = 0
        for piece in Player.draw:
            for x in range(self.size - 2):
                for y in range(self.size - 2):
                    if not self.isPiecePlaceable(1 + x, 1 + y, piece.figureNumber):
                        err += 1
        if err == ((self.size - 2) ** 2) * len(Player.draw):
            return False
        else:
            return True
