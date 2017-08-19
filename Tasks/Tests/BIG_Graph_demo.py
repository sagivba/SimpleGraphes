from time import time
from random import randint
from Graph.Node import *
from Graph.Graph import Graph
fmt_msg_time=lambda m,n:"{:>30} time:{:4.3f} sconds".format(m,n)
a_lot_of_nodes = []
# ==================================================================
# creating nodes groups
characters = "abcdef#ghigklmnopqvwxyz" + "abcdefghigk".upper()
for c in characters:
    for i in range(1, 4):
        node_name = "{}{:02}".format(c, i)
        a_lot_of_nodes.append(Node(node_name))
tstart = time()

tstart = time()
a_lot_of_edges = []
for i in range(1,len(a_lot_of_nodes) * 2):
    ui = randint(0, len(a_lot_of_nodes) - 1)
    vi = randint(0, len(a_lot_of_nodes) - 1)

    u = a_lot_of_nodes[ui]
    v = a_lot_of_nodes[vi]
    w = randint(1, 5)

    a_lot_of_edges.append((u, v, w))

tend = time()
print "{:>30} time:{:4.3f} sconds".format("init a_lot_of_nodes",tend-tstart)
tstart = time()
g = Graph("BIG!", a_lot_of_nodes)
for e in a_lot_of_edges:
    g.add_edge(*e)
tend = time()
print fmt_msg_time("init graph",tend-tstart)
print "{:>30}: {}".format("nuber of nodes ",len(g))
print "{:>30}: {}".format("number of edges",len(g.get_edges()))
print "{:>30}: {}".format("clique is",len(g)**2-len(g))

g.forget_pathes()
g.set_memoize(False)
tstart = time()
pathes_no_memoize = g.find_every_shortest_path()
tend = time()
print fmt_msg_time("no memoize find_every_shortest_path",tend-tstart)
print "{:>30}     : {}".format("number of pathes",len(pathes_no_memoize))

#init graph again
g = Graph("BIG!", a_lot_of_nodes)
for e in a_lot_of_edges:
    g.add_edge(*e)

tstart = time()
pathes_memoize_first = g.find_every_shortest_path()
tend = time()
print fmt_msg_time("first find_every_shortest_path",tend-tstart)
print "{:>30}     : {}".format("number of pathes",len(pathes_memoize_first))

tstart = time()
pathes_memoize_second = g.find_every_shortest_path()
tend = time()
print fmt_msg_time("second find_every_shortest_path",tend-tstart)
print "{:>30}     : {}".format("number of pathes",len(pathes_memoize_second))

# #print "\n".join(map(str,a_lot_of_pathes))
#



#print "\n".join(map(str,a_lot_of_pathes))
for path in pathes_no_memoize:
    if path not in pathes_memoize_first:
        print path

print '----------------------------------------------'
#print g.dump()
#print "\n".join(map(str,a_lot_of_pathes))
