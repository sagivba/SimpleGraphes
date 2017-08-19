from time import time
from random import randint
from Graph.Node import Node
from Graph.Graph import Graph
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

        self.node_a.add_neighbor(self.node_b, 3)
        self.node_a.add_neighbor(self.node_c, 7)
        self.node_b.add_neighbor(self.node_c, 1)
        self.node_b.add_neighbor(self.node_a, 2)

        self.node_z.add_neighbor(self.node_y, 1)
        self.node_z.add_neighbor(self.node_w, 2)
        self.node_z.add_neighbor(self.node_u, 3)

        # ('a','b',3),('a','c',7),('b','c',1),('b','a',2)
        self.graph = Graph("abc", [self.node_a, self.node_b, self.node_c])
        self.graph_other=Graph("zwyu", [self.node_z, self.node_y, self.node_w,self.node_u])

    def test_Graph(self):

        g = self.graph
        self.assertTrue(len(g) == 3, "len test")
        edges=g.get_edges()
        self.assertTrue(len(edges) == 4, "edges test")
        edges_2=[('f','g'),('h','k')]
        g_fghk=Graph("fghk",[Node(c) for c in "fghk"])
        for e in edges_2:
            g_fghk.add_edge(*e)
        self.assertTrue(len(edges_2) == 2, "edges {} test".format(edges_2))
        e_fg_w=g_fghk.get_edge_weight('f','g')
        self.assertTrue(e_fg_w == 1, "get_edge_weight ('f','g') ={}".format(e_fg_w))

    def test_contain(self):
        g=self.graph
        self.assertTrue('a' in g, "conatin (str) test")
        self.assertTrue(self.node_b in g, "conatin node test")

    def test_get_item(self):
        g = self.graph
        name=self.node_b.name
        self.assertTrue(g[name]==self.node_b, "conatin (str) test")
        self.assertRaises(KeyError, g.__getitem__, 'xxx')

    def test_remove_node(self):
        g = self.graph
        g.remove_node('bogus') # should not fail
        self.assertTrue(len(self.graph) == 3, "len test")
        edges = self.graph.get_edges()
        self.assertTrue(len(edges) == 4, "edges test")
        g.remove_node('a')
        g.remove_node('a')
        edges = self.graph.get_edges()
        self.assertTrue(len(edges) == 1, "edges test")
        self.assertTrue(len(self.graph) == 2, "len test")

    def test_is_edge(self):
        g = self.graph
        self.assertTrue(g.is_edge('a',  'b'), "is_edge a=>b")
        self.assertTrue(g.is_edge('a',  'c'), "is_edge a=>c")
        self.assertFalse(g.is_edge('a', 'd'), "is_edge a=>d")
        self.assertFalse(g.is_edge('c', 'a'), "is_edge c=>a")
        self.assertTrue(g.is_edge(self.node_a, self.node_b), "is_edge a=>b(nodes)")

    def test_add_node(self):
        g = self.graph
        self.assertTrue(len(g) == 3, "len test before add_node")
        self.assertRaises(TypeError, g.add_node, 'string is not a Node Object')
        node_d=Node('d')

        node_d.add_neighbor(g['a'],2)
        g['a'].add_neighbor(node_d, 3)
        g.add_node(node_d)
        edges =g.get_edges()
        self.assertTrue(len(g) == 4, "len test after add_node")
        self.assertTrue(len(edges) == 6, "edges test")
        self.assertTrue(g.is_edge('d', 'a'), "edge test")
        self.assertTrue(g.is_edge('a', 'd'), "edge test")
        expected_edges=set([('d','a',2.0)])
        d_edges=set(g['d'].get_edges())
        self.assertEquals(d_edges,expected_edges, "edges set test"+str(d_edges))
        # lets add exiositing node with differnt edges
        # before d edges : ('d','a',2)
        # after  d edges : ('d','a',10),'d','c',10),
        node_d_new = Node('d')
        node_d_new.add_neighbor(g['a'], 10)
        node_d_new.add_neighbor(g['c'], 11)
        g.add_node(node_d_new)

        expected_edges = set([('d', 'a', 2.0),('d', 'c', 11.0)])
        d_edges = set(g['d'].get_edges())
        self.assertEquals(d_edges, expected_edges, "edges set test" + str(d_edges))

    def test_add_edge(self):
        g = self.graph
        edges = g.get_edges()
        self.assertTrue(len(edges) == 4, "edges g test before add_edge")
        g.add_edge('c','b')
        edges = g.get_edges()
        self.assertTrue(len(edges) == 5, "edges g test after add_edge")

    def test_add_graph(self):
        g1=self.graph
        g2=self.graph_other
        edges1 = g1.get_edges()
        self.assertTrue(len(edges1) == 4, "edges g1 test")
        self.assertTrue(len(g1) == 3, "len g1 test")
        edges2 = g2.get_edges()
        self.assertTrue(len(edges2) == 3, "edges g2 test")
        self.assertTrue(len(g2) == 4, "len g2 test")
        g_plus=g1+g2
        edges_plus=g_plus.get_edges()
        self.assertTrue(len(edges_plus) == 7, "edges g1+g2 test")
        self.assertTrue(len(g_plus) == 7, "len g1+g2 test")

    def test__add__sub_graph(self):
        g1=self.graph
        new_node_a = Node('a')
        new_node_c = Node('c')
        new_node_d = Node('d')
        new_node_a.add_neighbor(new_node_c, 10)
        new_node_c.add_neighbor(new_node_d, 8)
        new_node_d.add_neighbor(new_node_c, 9)
        g3=Graph("acd",[new_node_a, new_node_c,new_node_d])

        # g1=> ('a','b',3),('a','c',7),('b','c',1),('b','a',2)
        # g3=> ('c','d',8),('d','c',9),('a','b',3),('a','c',7),('b','c',1),('b','a',2)
        #                                         7 not 10  ^
        print g1.dump()
        print g3.dump()

        g_plus = g1 + g3
        edges_plus = g_plus.get_edges()
        for e in [('c','d',8),('d','c',9),('a','b',3),('a','c',7),('b','c',1),('b','a',2)]:
            self.assertTrue(e in edges_plus, " g1+g2 edge:"+str(e))
            e_weight=g_plus.get_edge_weight(e[0],e[1])
            self.assertTrue(e_weight==e[2], " g1+g2 get_edge_weight:" + str(e))
        self.assertFalse(('a','c',10) in edges_plus, " g1+g2 did not copy edge:" + str(('a','c',10)))

    def test_belmanford(self):
        g_1_node=Graph("a", [Node('a')])
        d,p=g_1_node.BellmanFord(self.node_a)
        self.assertTrue(len(d)==1, "g_1_node d:"+str(d))
        self.assertTrue(len(p) == 1, "g_1_node p:" + str(p))
        n=dict()
        n['a']=Node('a')
        n['b']=Node('b')
        n['a'].add_neighbor(n['b'],-1)
        g_2_node=Graph("ab", n.values())
        d,p=g_2_node.BellmanFord(n['a'])
        self.assertTrue(len(d)==2, "g_2_node d:"+str(d))
        self.assertTrue(len(p) == 2, "g_2_node p:" + str(p))
        self.assertTrue((n['a'],None) in  p.items(), "g_1_node p:" + str(p.items()))

        #negative circle
        n['a'] = Node('a')
        n['b'] = Node('b')
        n['a'].add_neighbor(n['b'], -1)
        n['b'].add_neighbor(n['a'], -1)
        g_2_negative = Graph("ab-", n.values())
        self.assertRaises(RuntimeError, g_2_negative.BellmanFord, n['a'])


        n['a'] = Node('a')
        n['b'] = Node('b')
        n['c'] = Node('c')
        n['a'].add_neighbor(n['b'], 1)
        n['a'].add_neighbor(n['c'], 5)
        n['b'].add_neighbor(n['c'], 2)
        n['c'].add_neighbor(n['a'], 3)
        #    *-----3-------
        #    a --- 5 -----* c
        #     \          2*
        #      \        /
        #       1     /
        #        *  /
        #         b

        g_acb = Graph("abc", n.values())
        ac_path= g_acb.find_shortest_path(n['a'],n['c'])
        self.assertTrue(len(ac_path)==3 , "ac_path:" + str(ac_path))
        ab_path = g_acb.find_shortest_path(n['a'], n['b'])
        s= str(ab_path)
        test_name="ab_path:{}".format(str(ab_path))
        self.assertTrue(len(ab_path) == 2, test_name)
        a_path = g_acb.find_shortest_path(n['a'], n['a'])
        test_name="a_path:{}".format(str(a_path))
        self.assertTrue(len(a_path) == 1, test_name)

    def test_shortest_path(self):
        a = Node('a')
        b = Node('b')
        c = Node('c')
        g=Graph("sp",[a,b,c])
        edges_abc=[('a', 'b', 1), ('b', 'c', 2), ('c', 'a', 4)]
        for (u,v,w) in edges_abc:
            g.add_edge(u, v, w)
            g.add_edge(v, u, w)


    def test_memoiztion(self):
        a = Node('a')
        b = Node('b')
        c = Node('c')
        d = Node('d')
        g=Graph("sp",[a,b,c,d])
        edges_abc=[('a', 'b', 1), ('b', 'c', 2), ('c', 'd', 4)]
        for e in edges_abc:
            g.add_edge(*e)
        path_a2d=g.find_shortest_path(a,d)
        self.assertTrue(len(path_a2d) == 4, "path path_a2d:{}".format(path_a2d))
        path_list=g.get_all_memoized_paths()
        for exected_path in [[a,b], [a,b,c],[a,b,c,d]]:
            self.assertTrue(exected_path in path_list, "{} in path_list".format(exected_path))


    def _test_big_graph(self):
        a_lot_of_nodes=[]
        characters="abcdefghigklmnopqvwxyz"+"abcdefghigklmnopqvwxyz".upper()
        for c in characters:
            for i in range(1,2):
                node_name="{}{:2}".format(c,i)
                a_lot_of_nodes.append(Node(node_name))

        g=Graph("BIG!",a_lot_of_nodes)
        a_lot_of_edges=[]
        for i in range(1,len(a_lot_of_nodes)/2):
            ui=randint(0,len(a_lot_of_nodes)-1)
            vi=randint(0,len(a_lot_of_nodes)-1)

            u = a_lot_of_nodes[ui]
            v = a_lot_of_nodes[vi]
            w = randint(1,20)

            a_lot_of_edges.append((u,v,w))

        for e in a_lot_of_edges:
            g.add_edge(*e)

        tstart = time()
        a_lot_of_pathes=g.find_every_shortest_path()
        tend   = time()
        self.assertFalse(1==1,"find_every_shortest_path took {:.3f} seconds".format(tstart - tend))


