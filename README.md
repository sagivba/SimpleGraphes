# SimpleGraphes
Very simple directed an nondirected  graph implementation.
This is my first Python project.
In mathematics, and more specifically in graph theory, a graph is a structure amounting to a set of objects in which some pairs of the objects are in some sense "related". 
The objects correspond to mathematical abstractions called nodes or and each of the related pairs of nodes is called an edge or an arc.
## Main Classes:
### Graph/Graph
**name**  - The name of the graph.
**nodes** - This is a dictionary fully descriptive of the graph.
            Its keys are the names of the nodes, and its values are the node
            instances (of class Node).
            
Please note that I implemented Belman Ford to find the shorted path so nodes weight can be negative.
I allso uses memoaztion in order to improve runtime performance 

### Graph/NonDirectionalGraph
  inheritance from Graph

###Graph/Node
**name** - The name of the node. The name can be any immutable object, most naturally a string or a number.
**neighbors** - a dictionary of the neighbors with the neighbors.
                names as keys and the weights of the corresponding edges as values.
###Path
This class is used in the Belman Ford shortest distance algorithm and in the memoization 
**name** - the name of the path
**weight** - the total weight of the path

### Tests
Look at Tasks/Tests directory for unit tests.


