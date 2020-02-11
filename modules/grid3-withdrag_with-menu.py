import pygame as pg
import sys
from pygame.locals import *
import random
import time

pg.init()
# settings
windowWidth = 450
windowHeight = 640
boardWidth = 20
boardHeight = 14
margin = 2
boxSize = 30
#create
windowDisplay = pg.display.set_mode((windowWidth, windowHeight), RESIZABLE)


# color
bgColor = (150, 211, 255)
boardColor = (82, 153, 211)
cream = (240, 247, 244)
redpink = (255, 143, 137)
green = (34,199,139)
blue = (0,0,255)

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

def clickRange(x, y):
    if x < 65 or x > 386 or y < 96 or y > 416:
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

#<<<<<<< HEAD

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

#=======

pts=0
def points(pts):
    white = 255, 255, 255
    police = pg.font.SysFont('arial', 20)
    texte = police.render('Score : '+ str(pts), False, white)
    windowDisplay.blit(texte, (10, 10))
        
#=======

grid = []
for row in range (20):
    grid.append([])
    for column in range (14):
        grid[row].append(0)
limits()
printGrid()

def drawPieces(figure, x, y):
    figure = random.randint(0,11)
    block = pieces[figure]
    rect1 = []
    for row in range (5):
        for column in range (5):
            if block[row][column] == '1':
                rect1.append(pg.Rect((margin + boxSize)*column + 20 + x, (margin + boxSize)*row + 430 + y, boxSize, boxSize))
    print(rect1)
    return rect1

def drawPieces1(figure, x, y):
    figure = random.randint(0,11)
    block = pieces[figure]
    rect2 = []
    for row in range (5):
        for column in range (5):
            if block[row][column] == '1':
                rect2.append(pg.Rect((margin + boxSize)*column + 120 + x, (margin + boxSize)*row + 430 + y, boxSize, boxSize))
    
    return rect2

def drawPieces2(figure, x, y):
    
    block = pieces[figure]
    rect3 = []
    for row in range (5):
        for column in range (5):
            if block[row][column] == '1':
                rect3.append(pg.Rect((margin + boxSize)*column + 220 + x, (margin + boxSize)*row + 430 + y, boxSize, boxSize))
    
    return rect3
        
def menu():
    imageM = pg.image.load('fond.jpg').convert() 
    windowDisplay.blit(imageM,(0,0))                               
    pg.display.update                                   
    boutonjouer = pg.rect.Rect((165,216,135,43))        
    boutonquitter = pg.rect.Rect((165,284,135,45))
    run = True                                              
    while run:                                              
        windowDisplay.blit(imageM,(0,0))                         
        for event in pg.event.get():                    
            
            if event.type == pg.QUIT:                   
                run = False                          
                pg.display.quit()                       
            if event.type == pg.MOUSEBUTTONDOWN:
                possour = event.pos
                if boutonjouer.collidepoint(possour):     
                    main()
                elif boutonquitter.collidepoint(possour):
                    run = False
                    pg.display.quit()
        pg.display.flip()                              
        
def main():
    pg.init()

    # make sure program runs at most at a certain fps
    fpsClock = pg.time.Clock()

    # window title
    pg.display.set_caption("Block Puzzle")
    figure1 = random.randint(0,11)
    figure2 = random.randint(0,11)
    figure3 = random.randint(0,11)

    # block sample
    rect_list1 = drawPieces(figure1,0, 0)
    rect_list2 = drawPieces1(figure2,0, 0)
    rect_list3 = drawPieces2(figure3,0, 0)
    rect = pg.Rect(65,450,30,30)
    rect2 = pg.Rect(145, 450, 30, 30)
    rect3 = pg.Rect(205, 450, 30, 30)

    drag = None
    # main program loop
    Lerec = None
    while True:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return     #using espace key to exit

            elif event.type == MOUSEBUTTONDOWN:
                mouseX, mouseY = event.pos
                if rect.collidepoint(event.pos):
                    myX, myY = rect.topleft
                    Lerec = 1
                    drag = mouseX - myX, mouseY - myY
                    
                elif rect2.collidepoint(event.pos):
                    myX, myY = rect2.topleft
                    Lerec = 2
                    drag = mouseX - myX, mouseY - myY
                    
                elif rect3.collidepoint(event.pos):
                    myX, myY = rect3.topleft
                    Lerec = 3
                    drag = mouseX - myX, mouseY - myY

            if event.type == MOUSEBUTTONUP:
                mouseX, mouseY = event.pos
                if rect.collidepoint(event.pos):
                    column = mouseX // (boxSize + margin)
                    row = mouseY // (boxSize + margin)
                    if clickRange(mouseX, mouseY) and isPiecePlaceable(row-1,column-1,figure1,2):
                        placePiece(row-1,column-1,figure1,2)
                        isAligned()
                    
                elif rect2.collidepoint(event.pos):
                    column = mouseX // (boxSize + margin)
                    row = mouseY // (boxSize + margin)
                    if clickRange(mouseX, mouseY) and isPiecePlaceable(row-1,column-1,figure2,2):
                        placePiece(row-1,column-1,figure2,2)
                        isAligned()
                elif rect3.collidepoint(event.pos):
                    column = mouseX // (boxSize + margin)
                    row = mouseY // (boxSize + margin)
                    if clickRange(mouseX, mouseY) and isPiecePlaceable(row-1,column-1,figure3,2):
                        placePiece(row-1,column-1,figure3,2)
                        isAligned()

                # block test
                rect = pg.Rect(65, 450, 30, 30)
                rect = pg.Rect(65, 450, 30, 30)
                drag = None


                rect2 = pg.Rect(145, 450, 30, 30)
                rect2 = pg.Rect(145, 450, 30, 30)
                drag = None

                rect3 = pg.Rect(205, 450, 30, 30)
                rect3 = pg.Rect(205, 450, 30, 30)
                drag = None
                
            elif event.type == MOUSEMOTION:
                if Lerec == 1:
                    if drag:
                        for rect1 in rect_list1:
                            rect1.x += event.rel[0]
                            rect1.y += event.rel[1]
                        mouseX, mouseY = pg.mouse.get_pos()
                        offX, offY = drag
                        rect.topleft = mouseX - offX, mouseY - offY
                elif Lerec == 2:
                    if drag:
                        for rect2 in rect_list2:
                            rect2.x += event.rel[0]
                            rect2.y += event.rel[1]
                        mouseX, mouseY = pg.mouse.get_pos()
                        offX, offY = drag
                        rect2.topleft = mouseX - offX, mouseY - offY
                elif  Lerec == 3:
                    if drag:
                        for rect3 in rect_list3:
                            rect3.x += event.rel[0]
                            rect3.y += event.rel[1]
                        mouseX, mouseY = pg.mouse.get_pos()
                        offX, offY = drag
                        rect3.topleft = mouseX - offX, mouseY - offY
        

        windowDisplay.fill(bgColor)
        for rect in rect_list1:
            pg.draw.rect(windowDisplay,redpink, rect)
        for rect2 in rect_list2:
            pg.draw.rect(windowDisplay,green, rect2)
        for rect3 in rect_list3:
            pg.draw.rect(windowDisplay,blue, rect3)
        points(pts)
        

        for row in range (3, 13):
            for column in range (2, 12):
                color = boardColor
                if grid[row][column] == 1:
                    color = redpink
                pg.draw.rect(windowDisplay, color, 
                ((margin + boxSize)*column + margin, 
                (margin + boxSize)*row + margin, 
                boxSize, 
                boxSize))
        for rect1 in rect_list1:
            pg.draw.rect(windowDisplay, green, rect)
        pg.display.flip()

if __name__ == '__main__':
    menu()


