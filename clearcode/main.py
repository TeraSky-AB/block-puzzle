import pygame as pg
import modules.grid
import modules.logicalgate as lg


SCREENHEIGHT = 700
SCREENWIDTH = 650
screensize = (SCREENHEIGHT, SCREENWIDTH)

pg.init()

screen = pg.display.set_mode(screensize)
currentDisplay = "menu"

doContinue = True

while doContinue:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			doContinue = False
			pg.display.quit()
			quit()

	





	pg.display.flip()




