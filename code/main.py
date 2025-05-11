
from grid import Grid
from solver import *
from Graph import *
from game import *

# data_path = ".../input/"
# file_name = data_path + "grid00.in"
file_name = "D:/Document_Ecole/Y1_ENSAE/Semestre_2/Programmation/ensae-prog25/input/" + "grid00.in"
grid = Grid.grid_from_file(file_name)
# print(grid)
# file_name = data_path + "grid01.in"
grid = Grid.grid_from_file(file_name, read_values=True)
# print(grid)

#==================================== Score by Greedy ===============================

solver = SolverGreedy(grid)  
solver.run()
print(f"Score by Greedy: {solver.score()}")

#==============================       Score by using General Graph method     ====================================================

solver = Solver(grid)
solver.run()
pairs = solver.get_pairs()
score = solver.calculate_score()
# print("Matching pairs:", pairs)
print("Best score:", score)


# ================================      Plot       ===================================================

# grid.plot()

run_visualizer(grid)
