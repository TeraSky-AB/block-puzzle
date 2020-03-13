import pygame as pg

def isOnGrid(pos):
	if pos[0] > 65 and pos[0] < 65+320 and pos[1] > 65 and pos[1] < 65+320:
		return True
	else:
		return False

def quitGame():
	pg.display.quit()
	quit()

def maxWeight(list):
	max = list[0]
	maxIndex = (0,0)
	for i in range(len(list)):
		for j in range(1,len(list[i])):
			if list[i][j][0] > max[0][0]:
				max = list[i]
				maxIndex = (i,j)
	return (maxIndex)