class Graph:
    def __init__(self, n):
        self.n = n
        self.adjacence = [[0] * n for _ in range(n)]  # Adjacency matrix

    def set_edge(self, i, j, capacity):
        """Set edge capacity from node i to node j."""
        self.adjacence[i][j] = capacity

    def bfs(self, source, sink, parent):
        """Find an augmenting path using BFS."""
        visited = [False] * self.n
        queue = [source]
        visited[source] = True

        while queue:
            u = queue.pop(0)
            for v in range(self.n):
                if not visited[v] and self.adjacence[u][v] > 0:  # Check residual capacity
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u

        return visited[sink]  # Returns True if sink is reachable

    def ford_fulkerson(self, source, sink):
        """Ford-Fulkerson algorithm to find max flow."""
        parent = [-1] * self.n
        max_flow = 0

        # While there exists an augmenting path
        while self.bfs(source, sink, parent):
            path_flow = float('inf')  # Initialize with infinity
            v = sink

            # Find the minimum residual capacity along the path
            while v != source:
                u = parent[v]
                path_flow = min(path_flow, self.adjacence[u][v])
                v = u

            # Update residual capacities
            v = sink
            while v != source:
                u = parent[v]
                self.adjacence[u][v] -= path_flow  # Forward edge capacity reduced
                self.adjacence[v][u] += path_flow  # Reverse edge capacity increased
                v = u

            max_flow += path_flow  # Add the flow to the total max flow

        return max_flow


def cell_to_node(i, j, cols):
    """Convert grid cell (i, j) to node index."""
    return i * cols + j + 1  # +1 for source offset


def build_flow_network(grid):
    """
    Build a flow network from the grid.
    - Source connects to Set A (cells where (i + j) is even)
    - Set A connects to Set B (valid adjacent pairs)
    - Set B connects to Sink
    """
    rows, cols = grid.n, grid.m
    total_nodes = rows * cols + 2  # +2 for source and sink
    source, sink = 0, total_nodes - 1
    graph = Graph(total_nodes)

    for (i1, j1), (i2, j2) in grid.all_pairs():
        node1 = cell_to_node(i1, j1, cols)
        node2 = cell_to_node(i2, j2, cols)

        # If (i1 + j1) is even → node1 in Set A, node2 in Set B
        if (i1 + j1) % 2 == 0:
            graph.set_edge(source, node1, 1)   # Source → node1 (Set A)
            graph.set_edge(node1, node2, 1)    # node1 (Set A) → node2 (Set B)
            graph.set_edge(node2, sink, 1)     # node2 (Set B) → Sink
        else:
            # Reverse scenario if node2 is in Set A
            graph.set_edge(source, node2, 1)   # Source → node2
            graph.set_edge(node2, node1, 1)    # node2 → node1
            graph.set_edge(node1, sink, 1)     # node1 → Sink

    return graph, source, sink
