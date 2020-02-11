import modules.pieces as pc
import modules.grid as gd


pieces = pc.Pieces()
grid = gd.Grid(10, pieces)

for i in range(10):
    for j in range(10):
        grid.isPiecePlaceable(i, j, pc.pieces())
