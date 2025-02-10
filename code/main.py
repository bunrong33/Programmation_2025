from grid import Grid
from solver import *
from solver import SolverGreedy

grid = Grid(2, 3)
print(grid)

# data_path = ".../input/"
# data_path = "D:/Document_Ecole/Y1_ENSAE/Semestre_2/Programmation/ensae-prog25/input/"

# file_name = data_path + "grid01.in"
file_name = "D:/Document_Ecole/Y1_ENSAE/Semestre_2/Programmation/ensae-prog25/input/" + "grid19.in"

grid = Grid.grid_from_file(file_name)
print(grid)

# file_name = data_path + "grid01.in"
grid = Grid.grid_from_file(file_name, read_values=True)
print(grid)

# solver = SolverEmpty(grid)
# solver.run()
# print("The final score of SolverEmpty is:", solver.score())


solver = SolverGreedy(grid)  
solver.run()
print("The final score of SolverGreedy is:", solver.score())
grid.plot()