import pygame as pg
import sys
from pygame.locals import *


#fenetre

windowWidth = 300
windowHeight = 500


#couleur
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)


pg.init()
fenetre = pg.display.set_mode((windowWidth, windowHeight), RESIZABLE)
pg.display.set_caption("Block Puzzle")


while True:
    for event in pg.event.get():
        if event.type==QUIT:
            pg.quit()
            sys.exit()
        fenetre.fill(red)
        pg.display.update()
            

#----------

def grid():
    taille = int(input("entrez une valeur pour la taille de la grille: "))
    boxSize = 20
    gameGrid = boxSize * taille

def affiche(grid):
    for l in grid:
        for x in l:
            print(x, ' ', end="")
        print()


    

affiche(grid())
