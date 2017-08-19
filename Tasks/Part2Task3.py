from Graph.Node import Node
from Graph.Graph import Graph
from Regions.Regions import  Regions
print "###########################################################################"
print "# Task 3 - The roadmap implementation"
print "#     The files travelsEW.csv and travelsWE.csv record a large"
print "#     number of travels made by people from five regions in the country, called:"
print "#     Center, North, South, East and West."
print "#\n"
print "###########################################################################"
print "# Question 1"
print "# 1. From each file create a graph whose nodes are the country regions,"
print "# and whose edges are the roads themselves (if a travel was not recorded between"
print "# country regions, then it means such road does not exist)."
print "# The weight of each edge is defined as the average time (in seconds) of all the"
print "# travels done on that road."
print "# 2. When the two graphs are ready, add them together to create the complete graph of"
print "# the roadmap."
print "#\n"


def print_errors_log(file_name,errors_log):
    print "Errors Log of {}:".format(file_name)
    print  "\t"+"\n\t".join(errors_log)

def edges_to_graph(graph_name,edges):
    nodes=dict()

    graph = Graph(graph_name,nodes.values())
    for e in edges:
        graph.add_edge(*e)

    return graph
    #
    # for i in sorted(nodes):
    #     node = nodes[i]
    #     print node.dump()
    # for node in sorted(nodes.values()):
    #     print "node.__str__: {}".format(node)

def print_header(hdr):
    print "\n"
    print "+------------------------------------------"
    print "| " + str(hdr)
    print "+------------------------------------------"

def process_file(file_name,graph_name,time_format):
    with open(file_name, 'r') as ew_fh:
        regions = Regions(ew_fh,time_format)
        regions.parse_file()
        edges = regions.data_as_eges()
        graph = edges_to_graph(graph_name, edges)
        print_header(graph_name)
        print graph.dump()
        print ""
        print_errors_log(file_name, regions.errors_log)
        return graph


dir="D:\\tmp"
travelsEW, travelsWE= dir + "\\" + "travelsEW.csv", dir + "\\" + "travelsWE.csv"
##########################################################################
print "Answer 1.1:"
ew_graph=process_file(travelsEW,"EW","%d/%m/%Y %Hh%Mm")
we_graph=process_file(travelsWE,"WE","%I:%M:%S%p ; %b %d %y")
print "#Answer 1.2:"
# When the two graphs are ready, add them together to create the complete graph of"
# the roadmap."
world_graph1=ew_graph+we_graph
print_header("world_graph1=ew_graph+we_graph")
print world_graph1.dump()

world_graph2=we_graph+ew_graph
print_header("world_graph2=we_graph+ew_graph")
print world_graph2.dump()

print "###########################################################################"
print "# Question 2"
print "# From which region to which region it takes the longest time to travel"
print "#\n"
pathes1=world_graph1.find_every_shortest_path()
sorted_pathes1=sorted(pathes1,key=lambda p:(-1*p.weight,len(p)))
#print "\n".join(map(str,sorted_pathes))

pathes2=world_graph2.find_every_shortest_path()
sorted_pathes2=sorted(pathes2,key=lambda p:(-1*p.weight,len(p)))
#print "\n".join(map(str,sorted_pathes))

# I know I can also use max. but this way I can demonstrate perfomance later
print "The path which takes the longest time to travel:"
print "world_graph1: {}".format(sorted_pathes1[0])
print "world_graph2: {}".format(sorted_pathes2[0])




