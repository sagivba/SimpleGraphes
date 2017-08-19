from time import time
from random import randint
from Graph.Node import *
from Graph.Path import Path
from Graph.Graph import Graph
n=dict()
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
print g_acb.dump()
print "\nEges:\n\t",
print g_acb.get_edges()

ab_path = g_acb.find_shortest_path(n['a'], n['c'])
print "\npath a to b:\n\t",
print ab_path
print '===================================================\n\n'
print g_acb['a'].get_edges()