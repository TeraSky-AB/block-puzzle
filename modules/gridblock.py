import pygame as pg
import sys
from pygame.locals import *     #pygame.locals has the constants like QUIT, MOUSEBUTTON, and K_ESCAPE
import random
import time

# settings
windowWidth = 450
windowHeight = 640
boardWidth = 20
boardHeight = 14
margin = 2
boxSize = 30

# color
bgColor = (150, 211, 255)
boardColor = (102, 174, 232)
cream = (240, 247, 244)
redpink = (255, 143, 137)
green = (34,199,139)

# blocks
pieces = (
    ('00000','00000','00100','00000','00000'), # 0  : Unity block
    ('00000','00000','00110','00000','00000'), # 1  : 2 line
    ('00000','00000','01110','00000','00000'), # 2  : 3 line
    ('00000','00000','01100','00100','00000'), # 3  : Comma
    ('00000','00000','01100','01100','00000'), # 4  : 2x2 block
    ('00000','00000','11110','00000','00000'), # 5  : 4 line
    ('00000','00000','11111','00000','00000'), # 6  : 5 line
    ('00000','01110','01110','01110','00000'), # 7  : 3x3 block
    ('00000','00000','11100','00100','00100'), # 8  : Big comma
    ('00000','00000','01100','00100','00100'), # 9  : Logical not figure
    ('00000','00000','01100','00110','00000'), # 10 : Snake look alike
    ('00000','00000','01110','00100','00000')  # 11 : T figure
)


#create window
windowDisplay = pg.display.set_mode((windowWidth, windowHeight), RESIZABLE) 

# ------

def printGrid(grid):
    for i in grid:
        print(i)

def limits(grid):
    for i in range(11):
        grid[2][2+i] = 1
        grid[2+i][1] = 1
        grid[13][2+i] = 1
        grid[2+i][12] = 1

def clickRange(x, y):
    if x < 65 or x > 386 or y < 96 or y > 416:
        print("Click is out of range")
        return False
    else:
        return True

def isAligned(grid):
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
    eraseAlignements(grid, linesCompleted)

def eraseAlignements(grid, lines):
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

def isPiecePlaceable(grid, x, y, figure, orientation):
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

#<<<<<<< HEAD

def placePiece(grid, x, y, figure, orientation):
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

#=======

pts=0
def points(pts):
    white = 255, 255, 255
    police = pg.font.SysFont('arial', 20)
    texte = police.render('Score : '+ str(pts), False, white)
    windowDisplay.blit(texte, (10, 10))
        
#=======

def blankGrid():
    grid = []
    for row in range (20):
        grid.append([])
        for column in range (14):
            grid[row].append(0)
    return grid

def drawGrid(grid, customColor):
    for row in range (3, 13):
        for column in range (2, 12):
            color = boardColor
            if grid[row][column] == 1:
                color = customColor
            pg.draw.rect(windowDisplay, color, ((margin + boxSize)*column + margin, (margin + boxSize)*row + margin, boxSize, boxSize))

def drawPieces1(figure, x, y):
    
    block = pieces[figure]
    rect1 = []
    for row in range (5):
        for column in range (5):
            if block[row][column] == '1':
                rect1.append(pg.Rect((margin + boxSize)*column + 20 + x, (margin + boxSize)*row + 430 + y, boxSize, boxSize))
    return rect1

def drawPieces2(figure, x, y):
    block2 = pieces[figure]
    rect2 = []
    for row in range (5):
        for column in range (5):
            if block2[row][column] == '1':
                rect2.append(pg.Rect((margin + boxSize)*column + 120 + x, (margin + boxSize)*row +430 + y, boxSize, boxSize)) 
    return rect2

def drawPieces3(figure, x, y):
    block3 = pieces[figure]
    rect3 = []
    for row in range (5):
        for column in range (5):
            if block3[row][column] == '1':
                rect3.append(pg.Rect((margin + boxSize)*column + 220 + x, (margin + boxSize)*row +430 + y, boxSize, boxSize)) 
    return rect3


def main():
    pg.init()
    pts = 0
    # make sure program runs at most at a certain fps
    fpsClock = pg.time.Clock()
    figure = random.randint(0,11)
    # window title
    pg.display.set_caption("Block Puzzle")

    grid = blankGrid()
    rect_list1 = drawPieces1(figure, 0, 0)
    rect_list2 = drawPieces2(figure, 0, 0)
    rect_list3 = drawPieces3(figure, 0, 0)
    limits(grid)
    printGrid(grid)
    drag = None
    # main program loop
    while True:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return     #using espace key to exit

            elif event.type == MOUSEBUTTONDOWN:
                for rect1 in rect_list1:
                    if rect1.collidepoint(event.pos):
                        mouse1X, mouse1Y = event.pos
                        my1X, my1Y = rect1.topleft
                        drag = mouse1X - my1X, mouse1Y - my1Y
                for rect2 in rect_list2:
                    if rect2.collidepoint(event.pos):
                        mouse2X, mouse2Y = event.pos
                        my2X, my2Y = rect2.topleft
                        drag = mouse2X - my2X, mouse2Y - my2Y
                for rect3 in rect_list3:
                    if rect3.collidepoint(event.pos):
                        mouse3X, mouse3Y = event.pos
                        my3X, my3Y = rect3.topleft
                        drag = mouse3X - my3X, mouse3Y - my3Y
                    

            elif event.type == MOUSEBUTTONUP:
                column = mouseX // (boxSize + margin)
                row = mouseY // (boxSize + margin)
                if clickRange(mouseX, mouseY) and isPiecePlaceable(grid, row, column, figure, 0):
                    placePiece(grid, row, column, figure, 0)
                    pts = pts + 50
                    isAligned(grid)
                for rect1 in rect_list1:
                    rect1 = pg.Rect(mouse1X, mouse1Y, 0, 0)
                    rect1 = drawPieces1(figure)
                    drag = None
                for rect2 in rect_list2:
                    rect2 = pg.Rect(mouse2X, mouse2Y, 0, 0)
                    rect2 = drawPieces2(figure)
                    drag = None
                for rect3 in rect_list3:
                    rect3 = pg.Rect(mouse3X, mouse3Y, 0, 0)
                    rect3 = drawPieces3(figure)
                    drag = None

            elif event.type == MOUSEMOTION:
                if drag:
                    for rect1 in rect_list1:
                        rect1.x += event.rel[0]
                        rect1.y += event.rel[1]

                    for rect2 in rect_list2:
                        rect2.x += event.rel[0]
                        rect2.y += event.rel[1]

                    for rect3 in rect_list3:
                        rect3.x += event.rel[0]
                        rect3.y += event.rel[1]
                    mouse2X, mouse2Y = pg.mouse.get_pos()
                    off2X, off2Y = drag
                    rect2.topleft = mouse2X - off2X, mouse2Y - off2Y

                    mouseX, mouseY = pg.mouse.get_pos()
                    off1X, off1Y = drag
                    rect1.topleft = mouse1X - off1X, mouse1Y - off1Y

                    mouse3X, mouse3Y = pg.mouse.get_pos()
                    off3X, off3Y = drag
                    rect3.topleft = mouse3X - off3X, mouse3Y - off3Y
                    

       # if drag:
        #    for rect1 in rect_list1:
        #        mouseX, mouseY = pg.mouse.get_pos()
        #        offX, offY = drag
        #        rect1.topleft = mouseX - offX, mouseY - offY
        #        print("click ", mouseX, mouseY)

         #   for rect2 in rect_list2:
         #       mouseX, mouseY = pg.mouse.get_pos()
        #        offX, offY = drag
        #        rect2.topleft = mouseX - offX, mouseY - offY
         #       print("click ", mouseX, mouseY)

        #    for rect3 in rect_list3:
        #        mouseX, mouseY = pg.mouse.get_pos()
        #        offX, offY = drag
        #        rect3.topleft = mouseX - offX, mouseY - offY
        #        print("click ", mouseX, mouseY)

  

        windowDisplay.fill(bgColor)
        for rect1 in rect_list1:
            pg.draw.rect(windowDisplay, green, rect1)
        for rect2 in rect_list2:
            pg.draw.rect(windowDisplay, cream, rect2)
        for rect3 in rect_list3:
            pg.draw.rect(windowDisplay, redpink, rect3)
        points(pts)
        drawGrid(grid, green)
        drawPieces1(figure, 0, 0)
        drawPieces2(figure, 0, 0)
        drawPieces3(figure, 0, 0)

        pg.display.flip()

if __name__ == '__main__':
    main()


