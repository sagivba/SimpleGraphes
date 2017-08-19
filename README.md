# SimpleGraphes
Very simple directed an nondirected  graphe implimentation

In mathematics, and more specifically in graph theory, a graph is a structure amounting to a set of objects in which some pairs of the objects are in some sense "related". 
The objects correspond to mathematical abstractions called nodes or and each of the related pairs of nodes is called an edge or an arc.
## Classes:
### Graph
**name**  - The name of the graph.
**nodes** - This is a dictionary fully descriptive of the graph.
            Its keys are the names of the nodes, and its values are the node
            instances (of class Node).
            
Please note that I implemented Belman Ford to find th shorted path so nodes weight can be negative.
I allso uses memoaztion in order to improve runtime performance 

### NonDirectionalGraph
  inherance from Graph

###Node
**name** - the name of the node, name can be any immutable object, most naturally a string or a number.
**neighbors** - a dictionary of the neighbors with the neighbors.
                names as keys and the weights of the corresponding  edges as values.
###Path
This calss is used in the Belman Ford shortest distance algorithm and in th memoazation 
**name** - the name of the path
**weight** - the total weight of the path
