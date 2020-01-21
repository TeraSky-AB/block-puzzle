import pygame as pg

class Block():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y

        self.color = color

class Grid():
    def __init__(self, size):
        self.grid = []
        self.gridSize = size
        self.pieces = (
            
        )
    
    def newGrid(self):
        self.row = []
        for i in range(self.gridSize):
            self.row.append(0)
        for j in range(self.gridSize):
            self.grid.append(self.row)

    def state(self):
        for i in self.grid:
            print(i)
    
    def placePiece(self, pieceNb):
        

def convertDcToBn(nb):
    bits = []
    while(nb != 0):
        r = nb%2
        bits.append(r)
        nb = (nb-r)//2
    return bits[::-1]

SCREENWIDTH = 800
SCREENHEIGHT = 600
screensize = (SCREENWIDTH,SCREENHEIGHT)

pg.init()
screen = pg.display.set_mode(screensize)

stop = False
while not stop:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            stop = True
