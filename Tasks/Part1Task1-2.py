from Graph.Node import Node
from Graph.Path import Path
from Graph.Graph import Graph
print "###########################################################################"
print "# Part I - The Node class "
print "#\n"
print "###########################################################################"
print "# Task 1 - Define the class"
print "#          Implement the Node class\n"
print "#\n"
print "\nAnswer: See Graph.Node which uses Graph.Node and Graph.Path"
print "\n\n"
print "###########################################################################"
print "# Task 2 - Exemplary usage"
print "#\n"

print "###########################################################################"
print "# Question 1"
print "# Create 10 Node objects according to the figure above, print them (textually, of course)."
print "#\n"
nodes = dict()
for i in range(1, 11):
    nodes[i] = Node(i)
edges = [
    (1, 5, 20),    (1, 6, 5),    (1, 7, 15),    (1, 2, 10),    (1, 4, 20),
    (2, 4, 10),    (2, 3, 5),
    (3, 4,  5),    (3, 2, 15),
    (4, 5, 10),
    (5, 6,  5),
    (7, 6, 10),
    (8, 1,  5),    (8, 7,  5),
    (9, 2, 15),    (9, 8, 20),    (9, 10, 10),
    (10, 3, 15),   (10, 2, 5)
]
for name, neighbor, weight in edges:
    nodes[name].add_neighbor(nodes[neighbor], weight)
print "\nHere is the dump of those 10 nodes:"
for i in sorted(nodes):
    node = nodes[i]
    print node.dump()

print "\nHere is the str output of those 10 nodes:"
for node in sorted(nodes.values()):
    print "str(node) returns: '{}'".format(node)

print "\n\n"
print "###########################################################################"
print "# Question 2"
print "# Make some tests to make sure your implementation works."
print "#\n"
print "\nAnswer: see Node_test.py (unit tests)"

print "\n\n"
print "###########################################################################"
print "# Question 3"
print "# How many edges are in the graph, and what is their total weight?"
print "#\n"
print "\nAnswer:"
total_len=sum(map(lambda n:len(n), nodes.values()))
print "number of edges:{}".format( total_len)
total_weight=sum(map(lambda n:n.get_total_weight(), nodes.values() ))
print "total weight   :{}".format(total_weight)
print "\n"

print "###########################################################################"
print "# Question 4"
print "# Sort the nodes by the number of their neighbors."
print "#\n"
print "\nAnswer:\n\t (|w| represent cardinality of w)"
by_number_of_neighbors=sorted(nodes.values(),key=len)
cardinality_str=lambda n : "{:>5} = {}".format('|'+str(n)+'|',len(n))
print "\n\t"+"\n\t".join(map(cardinality_str , by_number_of_neighbors))
print "\n"
