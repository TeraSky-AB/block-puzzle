import pygame as pg

print("bib importée")

class Block():
    def __init__(self):
        print("Block créé")
        self.surface = pg.image.load("vais.jpg")
        