import unittest
from Graph.Node import Node

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.node_a = Node('a')
        self.node_b = Node('b')
        self.node_c = Node('c')

    def tearDown(self):
        pass
    def test_Node(self):
        node_a = self.node_a
        self.assertTrue(node_a=='a',"__str__ test")
        self.assertTrue(node_a.is_isolated(), "is_isolated test")
        self.assertTrue(node_a == node_a, "is_isolated test")

    def test_hash(self):
        node_a = self.node_a
        self.assertTrue(hash(node_a) == hash('a'), "hash node_a")

    def test_Node_Error(self):
            self.assertRaises(TypeError,Node,[1,2])

    def test_get_edges(self):
        node_a = self.node_a
        node_b = self.node_b
        node_c = self.node_c
        node_a.add_neighbor(node_b, 3)
        node_a.add_neighbor(node_c, 7)
        edges=node_a.get_edges()
        self.assertTrue(len(edges)==2, "len edges test")
        self.assertTrue((node_a,node_b,3) in edges)
        self.assertTrue((node_a, node_c, 7) in edges)

    def test_Node_neighbors(self):
        node_a = self.node_a
        node_b = self.node_b
        node_c = self.node_c

        self.assertTrue(node_a.is_isolated(), "is_isolated test")
        self.assertTrue(len(node_a)==0, "len 0")
        node_a.add_neighbor(node_b,3)
        self.assertTrue(len(node_a) == 1, "len 1")
        self.assertTrue(node_a.get_weight(node_b)==3 ,'get weight')
        self.assertTrue(node_a.is_neighbor('b'), "is_neighbor test by name")
        self.assertFalse(node_a.is_neighbor('c'), " not a neighbor test by name")
        self.assertTrue(node_a.is_neighbor(node_b), "is_neighbor test by object")
        self.assertFalse(node_a.is_neighbor(node_c), " not a neighbor test by object")
        node_a.remove_neighbor(node_b)
        self.assertTrue(len(node_a) == 0, "len 0")

    def test_Node_neighbors_error(self):
        node_a = Node('a')
        node_b = Node('b')
        node_a.add_neighbor(node_b)
        self.assertRaises(NameError, node_a.add_neighbor, node_a)
        self.assertRaises(ValueError, node_a.add_neighbor, node_b)
        node_a.remove_neighbor(node_b)
        self.assertTrue(len(node_a) == 0, "len 0")
        self.assertRaises(KeyError, node_a.remove_neighbor, node_b)

    def test_illustrated(self):
        nodes=dict()
        for i in range(1,11):
            nodes[i]=Node(i)
        edges=[
                (1, 5, 20),
                (1, 6,  5),
                (1, 7, 15),
                (1, 2, 10),
                (1, 4, 20),

                (2, 4, 10),
                (2, 3,  5),

                (3, 4,  5),
                (3, 2, 15),

                (4, 5, 10),

                (5, 6,  5),

                (7, 6, 10),

                (8, 1,  5),
                (8, 7, 10),

                (9, 2, 15),
                (9, 8, 20),
                (9,10, 10),

                (10, 3, 15),
                (10, 2,  5)
                ]
        for name,neighbor,weight in edges:
            nodes[name].add_neighbor(nodes[neighbor],weight)

        number_of_edges=0
        for i in sorted(nodes):
            node=nodes[i]
            number_of_edges += len(node)
            print "\n"+str(node)



if __name__ == '__main__':
    unittest.main()