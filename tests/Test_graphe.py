import sys 
sys.path.append("code/")

import unittest
from Graph import Graph

def node_index(i, j, cols):
    return i * cols + j + 1

class TestGraph(unittest.TestCase):
    
    def test_set_edge(self):
        graph = Graph(8)
        graph.set_edge(0, 1, 1, 0)
        self.assertEqual(graph.capacity[0][1], 1)
        self.assertEqual(graph.cost[0][1], 0)
        self.assertEqual(graph.capacity[1][0], 0)
        self.assertEqual(graph.cost[1][0], 0)
        self.assertIn(1, graph.adj[0])
        self.assertIn(0, graph.adj[1])
   
    def test_min_cost_flow(self):
        graph = Graph(4)
        source = 0
        sink = 3
        graph.set_edge(0, 1, 1, 0)
        graph.set_edge(1, 3, 1, 3)
        graph.set_edge(0, 2, 1, 1)
        graph.set_edge(2, 3, 1, 0)
        
        max_flow, total_cost = graph.min_cost_flow(source, sink)
        self.assertEqual(max_flow, 2)
        self.assertEqual(total_cost, 4)

if __name__ == '__main__':
    unittest.main()
