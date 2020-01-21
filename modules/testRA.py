import pygame as pg
import sys
import blocks

pg.init()

HEIGHT = 500
WIDTH = 500

size = (HEIGHT, WIDTH)

test = blocks.Block()

screen = pg.display.set_mode(size)
continuer = 1

screen.blit(test.surface, (250,250))
pg.display.flip()

while continuer:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            continuer = 0

    screen.blit(test.surface,(250,250))
    pg.display.flip()

    
    

    
    
