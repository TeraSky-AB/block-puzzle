grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def newGrid():
    row = []
    for i in range(10):
        row.append(0)
    for j in range(10):
        grid.append(row)

def affiche(grid):
    for i in grid:
        print(i)
        


    return grid

def placementJoueur(grid):
    x = int(input("possition en X"))
    y = int(input("possition en Y"))
    piece = input("quel forme ?")
    if piece == "simple":
        affiche(placePiece(grid,x,y))
    elif piece == "ligneH":
        affiche(placePieceLigneH(grid,x,y))
    elif piece == "LigneV":
        affiche(placePieceLigneV(grid,x,y))
    elif piece == "EnT":
        affiche(placePieceTn(grid,x,y))
    else:
        print("c'est pas encore une piece")


#si c'est une forme carré simple

def placePiece(grid,x,y):
    if grid[x][y] == 1:
        print("il y a deja une piece")
    else:
        grid[x][y] = 1
    return grid

def placePieceD(grid,x,y):
    if grid[x][y] == 1 or grid[x][y] == 1 or grid[x][y] == 1 or grid[x][y] == 1:
        print("il y a deja une piece  ici")
    else:
        grid[x][y] = 1
        grid[x][y+1] = 1
        grid[x][y] = 1
        grid[x][y] = 1
        

def placePieceT(grid,x,y):
    if grid[x][y] == 1 or grid[x][y] == 1 or grid[x][y] == 1 or grid[x][y] == 1 or grid[x][y] == 1 or grid[x][y] == 1 or grid[x][y] == 1 or grid[x][y] == 1 or grid[x][y] == 1:
        print("il y a deja une piece ici")
    else:
        grid[x][y] = 1
        grid[x][y] = 1
        grid[x][y] = 1
        grid[x][y] = 1
        grid[x][y] = 1
        grid[x][y] = 1
        grid[x][y] = 1
        grid[x][y] = 1
        grid[x][y] = 1
        

#si c'est une forme en ligne

def placePieceLigneH(grid,x,y):
    if grid[x][y] == 1 or grid[x][y-1] == 1 or grid[x][y+1] == 1:
        print("il y a deja une piece sur une des trois places")
    else:
        grid[x][y] = 1
        grid[x][y-1] = 1
        grid[x][y+1] = 1
    return grid

def placePieceLigneV(grid,x,y):
    if grid[x][y] == 1 or grid[x-1][y] == 1 or grid[x+1][y] == 1:
        print("il y a deja une piece sur une des trois places")
    else:
        grid[x][y] = 1
        grid[x-1][y] = 1
        grid[x+1][y] = 1
    return grid

#si c'est une forme en t

def placePieceTn(grid,x,y):
    if grid[x][y] == 1 or grid[x-1][y] == 1 or grid[x-2][y] == 1 or grid[x][y-1] == 1 or grid[x][y+1] == 1:
        print("il y a deja une piece sur une de ces cases")
    else:
        grid[x][y] = 1
        grid[x-1][y] = 1
        grid[x-2][y] = 1
        grid[x][y-1] = 1
        grid[x][y+1] = 1
    return grid

def placePieceTd(grid,x,y):
    if grid[x][y] == 1 or grid[x-1][y] == 1 or grid[x+1][y] == 1 or grid[x][y-1] == 1 or grid[x][y-2] == 1:
        print("il y a deja une piece sur une de ces cases")
    else:
        grid[x][y] = 1
        grid[x-1][y] = 1
        grid[x+1][y] = 1
        grid[x][y-1] = 1
        grid[x][y-2] = 1
    return grid

def placePieceTg(grid,x,y):
    if grid[x][y] == 1 or grid[x+1][y] == 1 or grid[x-1][y] == 1 or grid[x][y+1] == 1 or grid[x][y+2] == 1:
        print("il y a deja une piece sur une de ces cases")
    else:
        grid[x][y] = 1
        grid[x-1][y] = 1
        grid[x+1][y] = 1
        grid[x][y+1] = 1
        grid[x][y+2] = 1
    return grid

def placePieceTa(grid,x,y):
    if grid[x][y] == 1 or grid[x+1][y] == 1 or grid[x+2][y] == 1 or grid[x][y-1] == 1 or grid[x][y+1] == 1:
        print("il y a deja une piece sur une de ces cases")
    else:
        grid[x][y] = 1
        grid[x+1][y] = 1
        grid[x+2][y] = 1
        grid[x][y-1] = 1
        grid[x][y+1] = 1
    return grid

# si c'est une forme de petit angle

affiche(grid)
placementJoueur(grid)


