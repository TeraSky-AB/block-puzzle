import pygame as pg
import sys
from pygame.locals import *     #pygame.locals has the constants like QUIT, MOUSEBUTTON, and K_ESCAPE
import random
import time

#Pieces class

class Piece():
    def __init__(self):
        pass

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

#Blocks 2

pieces = (
    ('00000','00000','00100','00000','00000'), # 0  : Unity block
    ('00000','00000','00110','00000','00000'), # 1  : 2 line
    ('00000','00000','01110','00000','00000'), # 2  : 3 line
    ('00000','00000','01100','00100','00000'), # 3  : Comma
    ('00000','00000','01100','01100','00000'), # 9  : 2x2 block
    ('00000','00000','11110','00000','00000'), # 4  : 4 line
    ('00000','00000','11111','00000','00000'), # 5  : 5 line
    ('00000','01110','01110','01110','00000'), # 6  : 3x3 block
    ('00000','00000','11100','00100','00100'), # 7  : Big comma
    ('00000','00000','01100','00100','00100'), # 8  : Logical not figure
    ('00000','00000','01100','00110','00000'), # 10 : Snake look alike
    ('00000','00000','01110','00100','00000')  # 11 : T figure
)

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
def printGrid():
    for i in grid:
        print(i)

def limits():
    for i in range(11):
        grid[2][2+i] = 1
        grid[2+i][1] = 1
        grid[13][2+i] = 1
        grid[2+i][12] = 1

def clickRange(pos):
    if pos[0] < 65 or pos[0] > 386 or pos[1] < 96 or pos[1] > 416:
        print("Click is out of range")
        return False
    else:
        return True

def isAligned():
    linesCompleted = []
    for i in range(10):
        ln = 0
        clmn = 0
        for j in range(10):
            if grid[3+i][2+j]:
                ln += 1
            if grid[3+j][2+i]:
                clmn += 1
        if ln == 10:
            print("There is a line at", i)
            linesCompleted.append(['r', i+3])
        if clmn == 10:
            print("There is a column at", i)
            linesCompleted.append(['c', i+2])
    eraseAlignements(linesCompleted)

def eraseAlignements(lines):
    print(lines)
    for i in lines:
        if i[0] == 'r':
            for j in range(10):
                grid[i[1]][2+j] = 0

        elif i[0] == 'c':
            for j in range(10):
                grid[3+j][i[1]] = 0

def nand(a,b):
    if a == 1 and b == 1:
        return 0
    else:
        return 1

def isPiecePlaceable(x, y, figure, orientation):
    err = 0
    xi = x-2
    yi = y-2
    for i in range(5):
        for j in range(5):
            if orientation == 0:
                if not nand(grid[xi+i][yi+j],int(pieces[figure][i][j])):
                    err += 1
            elif orientation == 1:
                if  not nand(grid[xi+i][yi+j],int(pieces[figure][j][i])):
                    err+=1
            elif orientation == 2:
                if  not nand(grid[xi+i][yi+j],int(pieces[figure][-i][-j])):
                    err+=1
            elif orientation == 3:
                if not nand(grid[xi+i][yi+j],int(pieces[figure][-j][-i])):
                    err+=1
    if err:
        print("This piece cannot be placed here\terr:",err)
        return False
    else:
        return True
    

def placePiece(x, y, figure, orientation):
    xi = x-2
    yi = y-2
    for i in range(5):
        for j in range(5):
            if orientation == 0:
                grid[xi+i][yi+j] += int(pieces[figure][i][j])
            elif orientation == 1:
                grid[xi+i][yi+j] += int(pieces[figure][j][i])
            elif orientation == 2:
                grid[xi+i][yi+j] += int(pieces[figure][-i][-j])
            elif orientation == 3:
                grid[xi+i][yi+j] += int(pieces[figure][-j][-i])

grid = []
for row in range (19):
    grid.append([])
    for column in range (14):
        grid[row].append(0)
limits()
printGrid()


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
            ran = random.randint(0,11)
            pos = pg.mouse.get_pos()
            column = pos[0] // (gridSize + margin)
            row = pos[1] // (gridSize + margin)
            if clickRange(pos) and isPiecePlaceable(row,column,ran, ran%4):
                placePiece(row,column,ran, ran%4)
                printGrid()
                isAligned()
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