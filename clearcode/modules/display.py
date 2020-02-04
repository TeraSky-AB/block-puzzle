import pygame as pg

bgColor = (150, 211, 255)
boardColor = (102, 174, 232)
cream = (240, 247, 244)
redpink = (255, 143, 137)
green = (34,199,139)

def initGameBoard(board, grid):
	boardRect = board.get_rect()
	boxWidth = 300
	boxSize = (boxWidth, boxWidth)
	boardRectList = []
	for k in range(grid.size-2):
		for v in range(grid.size-2):
			boardRectList.append(pg.Rect((k*boxWidth,v*boxWidth),boxSize))
	print(boardRectList[0], boardRectList[1])
	return boardRectList

def displayBoard(win, blitCoord, board, rectList, grid):
	k = 0
	v = 0
	for i in range(0,grid.size-2):
		for j in range(0,grid.size-2):
			if grid.grid[1+i][1+j]:
				pg.draw.rect(board, cream, rectList[i])
			else:
				pg.draw.rect(board, boardColor, rectList[i])
	win.blit(board, blitCoord)



