from Graph import build_flow
from Graph import Graph
class Solver:
    """
    A solver class. 

    Attributes: 
    -----------
    grid: Grid
        The grid
    pairs: list[tuple[tuple[int]]]
        A list of pairs, each being a tuple ((i1, j1), (i2, j2))
    """

    def __init__(self, grid):
        """
        Initializes the solver.

        Parameters: 
        -----------
        grid: Grid
            The grid
        """
        self.grid = grid
        self.pairs = list()

    def score(self):
        """
        Computes the score of the list of pairs in self.pairs
        """
        return

class SolverEmpty(Solver):
    def run(self):
        pass

class SolverGreedy(Solver):
    """
    Class inheritace by class Solver
    """
    def __init__(self, grid):
        super().__init__(grid)
        self.selected_pairs = []
    
    def run(self):
        """
        Greedy algorithms en trouvant le meilleure couple
        We select all pair that we will use into seleted_pairs
        """

        all_pairs = self.grid.all_pairs()
        
        used_cells = set() # Create the set of pairs if pair is already used in order to compare with non-matching pair.
        for pair in all_pairs:
            (i1,j1) , (i2,j2) = pair 
            if (i1,j1) not in used_cells and (i2,j2) not in used_cells:
                self.selected_pairs.append(pair)
                used_cells.add((i1,j1))
                used_cells.add((i2,j2))
    
    def score(self):
        """
        Sum of the cost of all seleted pair and also the cost of non-matching pair except the value which represents black
        """
        total_cost = sum(self.grid.cost(pair) for pair in self.selected_pairs)
        used_cells = set(cell for pair in self.selected_pairs for cell in pair)

        for i in range(self.grid.n):
            for j in range(self.grid.m):
                if (i,j) not in used_cells and not self.grid.is_forbidden(i,j): # If the pair is not already in used cell and is not black
                    total_cost += self.grid.value[i][j]
        return total_cost

