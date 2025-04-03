
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
        Computes the of the list of pairs in self.pairs
        """
        total_cost = 0
        n = self.grid.n
        m = self.grid.m
        mat1 = [[1 for _ in range(m)] for _ in range(n)]  # keep track of used cells

        # Sum the absolute differences of paired values
        for a in self.selected_pairs:
            total_cost += self.grid.cost(a)

            i1, j1 = a[0]
            i2, j2 = a[1]
            # Mark the cells as used
            mat1[i1][j1] = 0
            mat1[i2][j2] = 0

        # Sum the values of unmatched cells
        for i in range(n):
            for j in range(m):
                if mat1[i][j] and not self.grid.is_forbidden(i, j):  # If not black
                    total_cost += self.grid.value[i][j]

        return total_cost

class SolverEmpty(Solver):
    def run(self):
        pass


class SolverGreedy(Solver):
    """Greedy solver for the grid pairing problem."""

    def __init__(self, grid):
        super().__init__(grid)
        self.selected_pairs = []  

    def run(self):
        """
        Greedy algorithm en trouvant la meilleure couple
        """
        all_pairs = self.grid.all_pairs()  # Si la paire est valide
        all_pairs.sort(key = self.grid.cost)  

        used_cells = set()
        for pair in all_pairs:
            (i1, j1), (i2, j2) = pair
            if (i1, j1) not in used_cells and (i2, j2) not in used_cells:
                self.selected_pairs.append(pair)
                used_cells.add((i1, j1))
                used_cells.add((i2, j2))
                
    def selected_pairs(self):
        return self.selected_pairs
