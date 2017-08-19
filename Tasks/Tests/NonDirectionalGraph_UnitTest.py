from Graph.Node import Node
from Graph.NonDirectionalGraph import NonDirectionalGraph as NDGraph
import unittest

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.node_a = Node('a')
        self.node_b = Node('b')
        self.node_c = Node('c')
        self.node_d = Node('d')

        self.node_z = Node('z')
        self.node_y = Node('y')
        self.node_w = Node('w')
        self.node_u = Node('u')

        self.graph = NDGraph("abc", [self.node_a, self.node_b, self.node_c])
        self.edges_abc=[('a','b',1),('b','c',2),('c','a',3)]

    def test_Graph(self):
        g = self.graph
        self.assertTrue(len(g) == 3, "len test 0")
        edges = g.get_unique_edges()
        self.assertTrue(len(edges) == 0, "edges test")
        for e in self.edges_abc:
            g.add_edge(*e)
        edges = g.get_unique_edges()
        self.assertTrue(len(edges) == len(self.edges_abc), "edges test")

    def test_add_remove_edge(self):
        g = self.graph
        for e in self.edges_abc:
            g.add_edge(*e)
        extra_edges_1=[('u', 'v',5),  ('a','u',10),  ('v','c',5),
                       ('v', 'u', 5), ('u', 'a', 10), ('c', 'v', 5),
                       ]
        for e in extra_edges_1:
            g.add_edge(*e)
        edges = g.get_unique_edges()
        self.assertTrue(len(edges) == len(self.edges_abc)+3, "edges test (x,y,1)==y,x,1")
        g.remove_edge('b','a')
        self.assertFalse(g.is_edge('a','b') ,"is_edge('a','b')")
        self.assertFalse(g.is_edge('b','a'), "is_edge('b','a')")

    def test_shortest_path(self):
        g = self.graph
        for e in self.edges_abc:
            g.add_edge(*e)
        path=g.find_shortest_path(self.node_a,self.node_c)
        l='a'
        self.assertTrue(list(path) in [['a','c'],['a','b','c']], "{}\n{}\n".format(path,g.dump()))




