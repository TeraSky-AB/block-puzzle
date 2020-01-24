import pygame as pg
import sys
from pygame.locals import *     #pygame.locals has the constants like QUIT, MOUSEBUTTON, and K_ESCAPE


# settings
windowWidth = 450
windowHeight = 640
boardWidth = 20
boardHeight = 14
margin = 2
gridSize = 30


# color
bgColor = (150, 211, 255)
boardColor = (82, 153, 211)
boxColor1 = (240, 247, 244)
boxColor2 = (255, 143, 137)

# blocks

L = ['..0',
     '000',
     '...']

O = ['000',
     '000',
     '000']

shape = [L, O]
shapeColors = [boxColor1, boxColor2]

# ------


pg.init()
fpsClock = pg.time.Clock()     #make sure program runs at most at a certain fps

windowDisplay = pg.display.set_mode((windowWidth, windowHeight), RESIZABLE)     #create window
pg.display.set_caption("Block Puzzle")      #window title


# ------

# class Block(pg.sprite.Sprite) :
#     def __init__(self, color, width, height):
#         super().__init__()
#         self.image = pg.Surface([width, height])
#         self.image.fill(color)
#         self.rect = self.image.get_rect()
    
#     def resetPos(self):
#         self.rect.y = random.randrang(-300, -20)
#         self.rect.x = random.randrange(0, windowWidth)

#     def update(self):
#         self.rect.y += 1
#         if self.rect.y > 450:
#             self.resetPos()

# class Player(Block):
#     def update(self):
#         pos = pg.mouse.get_pos()
#         self.rect.x = pos[0]
#         self.rect.y = pos[1]

# blockList = pg.sprite.Group()
# allSpritesList = pg.sprite.Group()


# class Key(pg.sprite.Sprite):
#     def __init__(self, xpos, ypos, id):
#         super(Key, self).__init__()
#         self.image = pg.draw.rect(windowDisplay, boxColor2, 
#                     (10, 10, gridSize, gridSize))
#         self.clicked = False
#         self.rect = self.image.get_rect()
#         self.rect.x = xpos
#         self.rect.y = ypos
#         self.id = id
#         self.linkReady = False
#         self.links = []
        
# ------

# player = Player(boxColor1, 30, 30)
# keyList = pg.sprite.Group()
# block = pg.draw.rect(windowDisplay, boxColor1, (10, 10, 30, 30))

# ------

grid = []
for row in range (20):
    grid.append([])
    for column in range (14):
        grid[row].append(0)

draggingToken = False
tokenx, tokeny = None, None

# main program loop
while True:

    mouseX, mouseY = pg.mouse.get_pos()
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
                    
        if event.type == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()
            column = pos[0] // (gridSize + margin)
            row = pos[1] // (gridSize + margin)

            grid[row][column] = 1
            print("click ", pos, "grid coordinates: ", row, column)

        #     if event.button == 3:
        #         keyList.add(Key(x, y, len(keyList) + 1))
        #     elif event.button == 1:
        #         for key in keyList:
        #             if key.rect.collidepoint(pos):
        #                 key.clicked = True
        #     elif event.button == 2:
        #         for key in keyList:
        #             if key.rect.collidepoint(pos):
        #                 key.linkReady = True
        #                 count = 0
        #                 links = []
        #                 for key in keyList:
        #                     if key.linkReady == True:
        #                         count += 1
        #                         links.append(key.id)
        #                 if count == 2:
        #                     for key in keyList:
        #                         if key.linkReady == True:
        #                             key.linkReady = False
        #                             count += 1
        #                             key.links += links

        # if event.type == pg.MOUSEBUTTONUP:
        #     for key in keyList:
        #         key.clicked = False
        #     drag_id = 0





    # allSpritesList.update()
    # blocksHitLists = pg.sprite.spritecollide(player, blockList, False)
    
    # for key in keyList:
    #     if key.clicked == True:
    #         pos = pg.mouse.get_pos()
    #         key.rect.x = pos[0] - (key.rect.windowWidth/2)
    #         key.rect.y = pos[1] - (key.rect.windowHeight/2)

    # keyList.draw(windowDisplay)

    
    windowDisplay.fill(bgColor)

    for row in range (3, 13):
        for column in range (2, 12):
            color = boardColor
            if grid[row][column] == 1:
                color = boxColor1
            pg.draw.rect(windowDisplay, color, 
            ((margin + gridSize)*column + margin, 
            (margin + gridSize)*row + margin, 
            gridSize, 
            gridSize))

    for row in range (14,15):
        for column in range (2,12):
            pg.draw.rect(windowDisplay, boxColor2, 
            ((margin + gridSize)*column + margin, 
            (margin + gridSize)*row + margin, 
            gridSize, 
            gridSize))


    pg.display.flip()




