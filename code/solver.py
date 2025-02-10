
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
        return "Method not implemented yet"

class SolverEmpty(Solver):
    def run(self):
        pass


class SolverGreedy(Solver):
    """Greedy solver for the grid pairing problem."""

    def __init__(self, grid):
        super().__init__(grid)
        self.selected_pairs = []  # Store selected pairs

    def run(self):
        """
        Implements a greedy algorithm to select the best pairs minimizing cost.
        """
        all_pairs = self.grid.all_pairs()  # Get all valid pairs
        all_pairs.sort(key=self.grid.cost)  # Sort pairs by increasing cost

        used_cells = set()
        for pair in all_pairs:
            (i1, j1), (i2, j2) = pair
            if (i1, j1) not in used_cells and (i2, j2) not in used_cells:
                self.selected_pairs.append(pair)
                used_cells.add((i1, j1))
                used_cells.add((i2, j2))

    def score(self):
        """Computes the total cost of the selected pairs."""
        total_cost = sum(self.grid.cost(pair) for pair in self.selected_pairs)
        used_cells = set(cell for pair in self.selected_pairs for cell in pair)

        # Add unpaired cell values except for black cells
        for i in range(self.grid.n):
            for j in range(self.grid.m):
                if (i, j) not in used_cells and not self.grid.is_forbidden(i, j):
                    total_cost += self.grid.value[i][j]

        return total_cost
