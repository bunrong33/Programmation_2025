# # -------------------------------------------
# class Graph_Ford_Fulkerson:
#     def __init__(self, n):
#         self.n = n
#         self.adjacency = [[0] * n for _ in range(n)]  # Adjacency matrix representation of the graph

#     def set_edge(self, u, v, capacity):
#         self.adjacency[u][v] = capacity

#     def bfs(self, source, sink, parent):
#         visited = [False] * self.n
#         queue = [source]  # Use a standard list as a queue
#         visited[source] = True

#         while queue:
#             u = queue.pop(0)  # Dequeue the first element
#             for v in range(self.n):
#                 if not visited[v] and self.adjacency[u][v] > 0:
#                     queue.append(v)  # Enqueue the node
#                     visited[v] = True
#                     parent[v] = u
#                     if v == sink:
#                         return True
#         return False
#     def ford_fulkerson(self, source, sink):
#         parent = [-1] * self.n
#         max_flow = 0
#         pairs = []

#         while self.bfs(source, sink, parent):
#             # Find the minimum residual capacity of the edges along the path
#             path_flow = float('Inf')
#             s = sink
#             while s != source:
#                 u = parent[s]
#                 path_flow = min(path_flow, self.adjacency[u][s])
#                 s = u

#             # Update residual capacities of the edges and reverse edges
#             s = sink
#             while s != source:
#                 u = parent[s]
#                 self.adjacency[u][s] -= path_flow
#                 self.adjacency[s][u] += path_flow
#                 s = u

#             # Add path flow to total flow
#             max_flow += path_flow

#             # Extract the pair (u, v) from the path
#             v = sink
#             while v != source:
#                 u = parent[v]
#                 if u != source and v != sink:
#                     pairs.append((u, v))
#                 v = u

#         return max_flow, pairs


# def node_index(i, j, cols):
#     return i * cols + j + 1


# def is_color_matching(color1, color2):
#     if color1 == 4 or color2 == 4:  # Black cells cannot be paired
#         return False
#     if color1 == 0:  # White can pair with any color except black
#         return True
#     if color2 == 0:  # White can pair with any color except black
#         return True
#     if color1 == 1:  # Red can pair with white, red, or blue
#         return color2 in {0, 1, 2}
#     if color1 == 2:  # Blue can pair with white, red, or blue
#         return color2 in {0, 1, 2}
#     if color1 == 3:  # Green can only pair with green or white
#         return color2 in {0, 3}
#     return False

# def build_flow(grid):
#     """
#     Build a bipartite graph from the grid.

#     Parameters:
#     -----------
#     grid: Grid
#         The grid object.

#     Returns:
#     --------
#     graph: Graph
#         The bipartite graph.
#     source: int
#         Source node.
#     sink: int
#         Sink node.
#     """
#     rows, cols = grid.n, grid.m
#     total_nodes = rows * cols + 2  # Include source and sink
#     source, sink = 0, total_nodes - 1
#     graph = Graph_Ford_Fulkerson(total_nodes)

#     # Iterate over all cells in the grid
#     for i in range(rows):
#         for j in range(cols):
#             if (i + j) % 2 == 0:
#                 # Cell is in set A (even)
#                 node_a = node_index(i, j, cols)
#                 graph.set_edge(source, node_a, 1)  # Connect source to node A

#                 # Check adjacent cells (set B)
#                 for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#                     ni, nj = i + di, j + dj
#                     if 0 <= ni < rows and 0 <= nj < cols:
#                         node_b = node_index(ni, nj, cols)
#                         if is_color_matching(grid.color[i][j], grid.color[ni][nj]):
#                             graph.set_edge(node_a, node_b, 1)  # Connect node A to node B
#             else:
#                 # Cell is in set B (odd)
#                 node_b = node_index(i, j, cols)
#                 graph.set_edge(node_b, sink, 1)  # Connect node B to sink

#     return graph, source, sink

# def calculate_score(pairs, grid):
#     """
#     Calculate the score based on the pairs and the grid.

#     Parameters:
#     -----------
#     pairs: list[tuple[int, int]]
#         List of pairs of matched nodes.
#     grid: Grid
#         The grid object.

#     Returns:
#     --------
#     score: int
#         The total score.
#     """
    
#     rows, cols = grid.n, grid.m
#     paired_cells = set()  # To store cells that are part of a pair
#     score = 0

#     # Calculate the cost of pairs
#     for pair in pairs:
#         u, v = pair
#         i1, j1 = (u - 1) // cols, (u - 1) % cols  # Convert node index to (i, j)
#         i2, j2 = (v - 1) // cols, (v - 1) % cols
#         paired_cells.add((i1, j1))
#         paired_cells.add((i2, j2))
#         score += abs(grid.value[i1][j1] - grid.value[i2][j2])  

#     # Calculate the cost of unpaired cells (excluding black cells)
#     for i in range(rows):
#         for j in range(cols):
#             if (i, j) not in paired_cells and grid.color[i][j] != 4:  
#                 score += grid.value[i][j]  

#     return score
# ------------------------------------------------------------
# ==========================================


class Graph:
    def __init__(self, n):
        """
        Initialize the graph with n nodes
        """
        self.n = n
        self.capacity = [[0] * n for _ in range(n)]
        self.cost = [[0] * n for _ in range(n)]
        self.adj = [[] for _ in range(n)]

    def set_edge(self, u, v, cap, cost):
        # Forward edge
        self.capacity[u][v] = cap
        self.cost[u][v] = cost
        # Reverse edge
        self.capacity[v][u] = 0
        self.cost[v][u] = -cost
        if v not in self.adj[u]:
            self.adj[u].append(v)
        if u not in self.adj[v]:
            self.adj[v].append(u)

    def min_cost_flow(self, source, sink):
        """
        Compute min-cost max-flow with Bellman-ford Algorithm(Shortest path faster algorithms)

        """
        INF = float('inf')
        total_flow = 0
        total_cost = 0

        while True:
            dist = [INF] * self.n
            dist[source] = 0
            parent = [-1] * self.n
            in_queue = [False] * self.n

            queue = [source]
            in_queue[source] = True

            while queue:
                u = queue.pop(0)   
                in_queue[u] = False
                for v in self.adj[u]:
                    if self.capacity[u][v] > 0 and dist[v] > dist[u] + self.cost[u][v]:
                        dist[v] = dist[u] + self.cost[u][v]
                        parent[v] = u
                        if not in_queue[v]:
                            queue.append(v)
                            in_queue[v] = True

            if dist[sink] == INF:
                # If no more paths
                break

            # Find minimum residual capacity on the path
            path_flow = INF
            v = sink
            while v != source:
                u = parent[v]
                path_flow = min(path_flow, self.capacity[u][v])
                v = u

            # Augment flow and update costs
            v = sink
            while v != source:
                u = parent[v]
                self.capacity[u][v] -= path_flow
                self.capacity[v][u] += path_flow
                total_cost += path_flow * self.cost[u][v]
                v = u
            total_flow += path_flow
            print(total_cost)
        return total_flow, total_cost

def node_index(i, j, cols):
    return i * cols + j + 1

def is_color_matching(color1, color2):
    if color1 == 4 or color2 == 4:
        return False
    if color1 == 0 or color2 == 0:
        return True
    if color1 in {1, 2}:
        return color2 in {0, 1, 2}
    if color1 == 3:
        return color2 in {0, 3}
    return False

def build_flow(grid):
    rows, cols = grid.n, grid.m
    total_nodes = rows * cols + 2  # source and sink
    source, sink = 0, total_nodes - 1
    graph = Graph(total_nodes)

    for i in range(rows):
        for j in range(cols):
            if (i + j) % 2 == 0:
                node_a = node_index(i, j, cols)
                graph.set_edge(source, node_a, 1, 0)  # Edge from source to cell
                
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols:
                        if is_color_matching(grid.color[i][j], grid.color[ni][nj]):
                            # weight = abs(grid.value[i][j]-grid.value[ni][nj])
                            weight = (grid.value[i][j] + grid.value[ni][nj]) - abs(grid.value[i][j] - grid.value[ni][nj])
                            # weight = 2 * max(grid.value[i][j], grid.value[ni][nj])
                            edge_cost = -weight
                            node_b = node_index(ni, nj, cols)
                            graph.set_edge(node_a, node_b, 1, edge_cost)

            else:
                node_b = node_index(i, j, cols)
                graph.set_edge(node_b, sink, 1, 0)  # Edge from cell to sink

    return graph, source, sink

def extract_matching(graph, grid):
    rows, cols = grid.n, grid.m
    pairs = []
    for i in range(rows):
        for j in range(cols):
            if (i + j) % 2 == 0:
                node_a = node_index(i, j, cols)
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols:
                        node_b = node_index(ni, nj, cols)
                        if graph.capacity[node_b][node_a] > 0 and graph.capacity[node_a][node_b] == 0:
                            pairs.append(((i, j), (ni, nj)))
    return pairs

class Solver:
    def __init__(self, grid):
        self.grid = grid
        self.pairs = []
        self.score = 0

    def run(self):
        # Build flow network from grid
        graph, source, sink = build_flow(self.grid)
        # Run min-cost flow
        flow, total_cost = graph.min_cost_flow(source, sink)
        self.pairs = extract_matching(graph, self.grid)
        self.score = self.calculate_score()

    def get_pairs(self):
        return self.pairs
    
    def calculate_score(self):
        rows, cols = self.grid.n, self.grid.m
        paired_cells = set()
        total_score = 0

        for pair in self.pairs:
            (i1, j1), (i2, j2) = pair
            paired_cells.add((i1, j1))
            paired_cells.add((i2, j2))
            total_score += abs(self.grid.value[i1][j1] - self.grid.value[i2][j2])
        
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in paired_cells and self.grid.color[i][j] != 4:
                    total_score += self.grid.value[i][j]
        return total_score