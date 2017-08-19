from Graph.Node import *
from Graph.Path import Path
from Graph.Graph import Graph

def test(got,expeceted, testname):
    if expeceted == got:
        print "OK   - {} ({})".format(testname,got)
    else:
        print "Error- "+testname
        print "  expected : {}".format(expeceted)
        print "      got  : {}".format(got)



def  Create_Graph_objects(graphs_names):



    #  ---- first_nodes_group ----
    # explanation
    #    X---3*Y ==> edge from X to Y  with weight 3
    #
    #    *3-----3------
    #    a ---------5* c*-2--------d
    #     \          2*
    #      \        /
    #       1     /
    #        *  /
    #         b
    abcd_nodes=dict()
    for chr in graphs_names[0]:
        abcd_nodes[chr] = Node(chr)
    abcd_edges=[('a','b',1),('a','c',5),('b','c',2),('c','a',3),('d','c',-2)]

    #        z
    #      /*  *
    #     /10 (-3)
    #    //      \
    #   //        \
    #  1/    o     \
    # */            \
    # x----------(-4)*y
    #  *12------------

    oxyz_nodes=dict()
    for chr in graphs_names[1]:
        oxyz_nodes[chr] = Node(chr)

    oxyz_edges=[('x','y',-4),('x','z',10),('y','x',12),('y','z',-3),('z','x',11)]
    #      *n*0---------o
    #     5/
    #    //     b*2--------x----------*6y
    #   /(-5)
    #  /*
    #  m
    xbmno_nodes=dict()
    for chr in graphs_names[2]:
        xbmno_nodes[chr] = Node(chr)
    # another way to build a graph
    xbmno_nodes['o'].add_neighbor(xbmno_nodes['n'], 0)
    xbmno_nodes['x'].add_neighbor(xbmno_nodes['b'], 2)
    xbmno_nodes['x'].add_neighbor(xbmno_nodes['y'], 6)
    xbmno_nodes['m'].add_neighbor(xbmno_nodes['n'],-5)
    xbmno_nodes['n'].add_neighbor(xbmno_nodes['m'], 5)


    nodes= set(abcd_nodes) | set(oxyz_nodes) | set(xbmno_nodes)
    print "Number of nodes:{}".format(len(nodes))
    grp_abcd=Graph("abcd", abcd_nodes.values())

    grp_abcd = Graph(graphs_names[0], abcd_nodes.values())
    for e in abcd_edges:
        grp_abcd.add_edge(*e)
    grp_oxyz = Graph(graphs_names[1], oxyz_nodes.values())
    for e in oxyz_edges:
        grp_oxyz.add_edge(*e)
    grp_xbmno= Graph(graphs_names[2], xbmno_nodes.values())
    return grp_abcd,grp_oxyz,grp_xbmno
print "###########################################################################"
print "# Part II - The Graph class "
print "#\n"
print "###########################################################################"
print "# Task 1 - Define the class"
print "# Implement the Graph class"
print "#\n"
print "\nAnswer: See Graph.Graph which uses Graph.Node and Graph.Path"
print "          I added Graph.Path to make testing and debugging easier"
print "\n\n"
print "###########################################################################"
print "#   TASK 2"
print "#\n"
print "###########################################################################"
print "# Question 4"
print "# Create 3 Graph objects,  each contains a different collection of nodes,"
print "# which together contain all 10 nodes."
print "# Use the __add()__ method to create a total graph that contains the entire"
print "# data of the example"
print "#\n"
print "\nAnswer:"
grp_abcd,grp_oxyz,grp_xbmno=Create_Graph_objects(["abcd", "oxyz", "xybmno"])
grp_all=Graph("")
for g in [grp_abcd,grp_oxyz,grp_xbmno]:
    print g.dump('\t  ')
    print ""
    grp_all+=g
print "----------------"
print grp_all.dump('\t  ')
#
#                          d
#                         /
#                        /          z
#    *3-----3-------   -2         /*  *
#    a ----------5*  c *         /10  -3              *n*0-------o
#     \          2*             //      \            5/
#      \        /              //        \          //
#       1     /              11/          \        /(-5)
#        *  /                */            \      /*
#         b  *2--------------x----------(-4)*y    m
#                             *12------------
#
#   mmm... I have developed a pretty good skill at drawing ascii graphs :)

print "\n\n"
print "###########################################################################"
print "# Question 2"
print "# Make some tests to make sure your implementation works."
print "#\n"
print "\n\nTests:"
get_w=grp_all.get_edge_weight # just an alias fro readble tests...
test(grp_all.name,"+abcd+oxyz+xybmno","garph name:")
test(get_w('a','b'), 1.0, "get_edge_weight('a','b')")
test(get_w('a','c'), 5.0, "get_edge_weight('a','c')")
test(get_w('b','c'), 2.0, "get_edge_weight('b','c')")
test(get_w('c','a'), 3.0, "get_edge_weight('c','a')")
test(get_w('d','c'),-2.0, "get_edge_weight('d','c')")

test(get_w('x','b'),2.0, "get_edge_weight('x','b')")


test(get_w('x','y'),-4.0, "get_edge_weight('x','y')  -  not 6!")
test(get_w('x','z'),10.0, "get_edge_weight('x','z')")
test(get_w('z','x'),11.0, "get_edge_weight('z','x')")
test(get_w('y','z'),-3.0, "get_edge_weight('y','z')")
test(get_w('y','x'),12.0, "get_edge_weight('y','x')")

test(get_w('m','n'),-5.0, "get_edge_weight('m','n')")
test(get_w('n','m'), 5.0, "get_edge_weight('n','m')")
test(get_w('o','n'), 0.0, "get_edge_weight('o','n')")

expected_edged=set([
    ('a','b', 1.0),
    ('a','c', 5.0),
    ('b','c', 2.0),
    ('c','a', 3.0),
    ('d','c',-2.0),
    ('x','b', 2.0),
    ('x','y',-4.0),
    ('x','z',10.0),
    ('z','x',11.0),
    ('y','z',-3.0),
    ('y','x',12.0),
    ('m','n',-5.0),
    ('n','m', 5.0),
    ('o','n', 0.0)])
grp_all_edges=set(grp_all.get_edges())
test(grp_all_edges, expected_edged, "edges")
print "Number of edges: {}".format(len(grp_all_edges))
# I dont want to use Graph.get_path_weight()
print  "Total graph weight: {}".format(grp_all.get_total_weight())

print "\n\n"
print "###########################################################################"
print "# Question 3"
print "# Sort the nodes by the number of their reachable nodes."
print "#\n"
print "\nAnswer:"
by_number_of_neighbors=sorted(grp_all.get_nodes(),key=len)
cardinality_str=lambda n : "|{:}| ={}".format(str(n),len(n))
print "cardinality:\n\t",
print "\n\t".join(map(cardinality_str , by_number_of_neighbors))
print "\n"

print "\n\n"
print "###########################################################################"
print "#Question 4"
print "#What is the pair of nodes that the shortest path between them has the highest weight?"
print "#\n"
print "\nAnswer:"
pathes=grp_all.find_every_shortest_path()
sorted_pathes=sorted(pathes,key=lambda p:(-1*p.weight,len(p)))
#print "\n".join(map(str,sorted_pathes))
print sorted_pathes[0]
