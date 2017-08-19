from Node import Node
from Path import Path
class Graph:
    """
    name   - the name of the graph.
    nodes  - This is a dictionary fully descriptive of the graph.
            Its keys are the names of the nodes, and its values are the node
            instances (of class Node).

            msg to Amit - Please note that I used Belman Ford so nodes weight can
                          be negative

    """

    def __init__(self, name="", nodes=[ ]):
        """
        :param self:
        :param name: will be stored as string name is an identifier
        :param nodes: nodes is an iterable of Node instances
        :return:
        """
        self.INFINITY = 9223372036854775807
        self.name =str(name)
        self.nodes=dict(map(lambda n:(n.name,n), nodes))
        self.memoized_pathes=dict() # remember all those old pathes
        self.memoized_edges=list()  # for get_edges optimisation
        self.please_memoize =True

    def __str__(self):
        """
        This method return print the description of all the nodes in the graph.
        Node.__str__() method,  but also the built-in function str().
        :param self:
        :return:
        """
        return ",".join(map( lambda n: str(n) ,self.nodes) )

    def __len__(self):
        """
         returns the number of nodes in the graph
        """
        return len(self.nodes)

    def __contains__(self, key):
        """
        :param key:
        :return:True in two cases:
                    (1) If key is a string, then if a node called key is in self, and
                    (2) If key is a Node, then if a node with the same name is in self.
        """
        if isinstance(key,str):
            node=Node(key)
        elif isinstance(key,Node):
            node = key
        else:
            raise TypeError("Argument must be the type of Node or string")
        return node.name in self.nodes

    def __getitem__(self, name):
        """
        This method  raise KeyError if name is not in the graph.
        :param name:
        :return: returns the Node object whose name is name.
        """

        return self.nodes[name]

    def __add__(self, other):
        """
        If a node exists both in self and in other, then the original node should not be updated.

        :param other:
        :return: returns a new Graph object that includes all the nodes and edges of self and other
        """
        new_name = self.name + "+" + other.name
        new_graph=Graph(new_name, self.nodes.values())
        for node in other.nodes:
            new_graph.add_node( other[node])
        return new_graph

    def set_memoize(self,memoize=True ):
        self.please_memoize=memoize

    def get_nodes(self):
        return self.nodes.values()

    def get_nodes_names(self):
        return self.nodes

    def get_edges(self):
        if self.please_memoize and len(self.memoized_edges)>0:
            return self.memoized_edges
        self.forget_edges()
        for node in self.get_nodes():
            self.memoized_edges.extend(node.get_edges())
        return self.memoized_edges

    def forget_pathes(self):
        self.memoized_pathes=dict()
    def forget_edges(self):
        self.memoized_edges=list()
    def get_all_memoized_paths(self):
        return self.memoized_pathes.values()

    def add_node(self,node):
        """
        adds a new node to the graph
        Its input argument is a Node instance.
        If a node with the same name already exists in the graph,
        then existing edges should not be overwritten, but new edges should be added.

        :param node:
        :return:
        """
        if not isinstance(node,Node):
            raise TypeError("input must be Node instance")
        self.forget_pathes()
        self.forget_edges()
        if node.name in self.nodes:
            self.nodes[node.name].copy_neighbors_of(node)
        else:
            self.nodes[node.name]=node

    def remove_node(self, name):
        """
          This method should not fail if name is not in self.
          removes the node name from self.
        """
        removed_node=None
        if name  in self.nodes:
            removed_node= self.nodes.pop(name)
            for node in self.get_nodes():
                if node.is_neighbor(removed_node):
                    node.remove_neighbor(removed_node)
        self.forget_pathes()
        self.forget_edges()
        return removed_node

    def is_edge(self, frm_name, to_name):
        """
        returns True if to_name is a neighbor of frm_name.
        This method should not fail if either frm_name is not in self.
        """
        if frm_name in self.nodes and to_name in self.nodes:
            return self.nodes[frm_name].is_neighbor(to_name)
        else:
            return False

    def add_edge(self, frm_name, to_name, weight=1):
        """
         adds an edge making to_name a neighbor of frm_name.
        This method should not fail if either frm_name or to_name are not in self.
        If to_name is already a neighbor of frm_name, then the method should do nothing.
        If frm_name and to_name are identical, then the method should do nothing.
        """
        if frm_name==to_name:
            return False
        if self.is_edge(frm_name, to_name):
            return False

        self.forget_pathes()
        self.forget_edges()
        if frm_name not in self.nodes:
            self.add_node(Node(frm_name))
        self[frm_name].add_neighbor(to_name, weight)
        return True

    def remove_edge(self, frm_name, to_name):
        """
        removes to_name from being a neighbor of frm_name.
        This method should not fail if frm_name is not in self.
        This method should not fail if to_name is not a neighbor of frm_name.
        :param self:
        :param frm_name:
        :param to_name:
        :return:
        """
        if self.is_edge(frm_name, to_name):
            self.forget_pathes()
            self.forget_edges()
            self.nodes[frm_name].remove_neighbor(to_name)

    def get_edge_weight(self, frm_name, to_name):
        """
        returns the weight of the edge between frm_name and to_name.
        This method should not fail if either frm_name or to_name are not in self.
        This method should return None if to_name is not a neighbor of frm_name.

        :param self:
        :param frm_name:
        :param to_name:
        :return:
        """
        if self.is_edge(frm_name, to_name):
            return self.nodes[frm_name].get_weight(to_name)

    def get_total_weight(self):
        weights=sorted(map(lambda e:e[2], self.get_edges()))
        return sum(weights)

    def get_path_weight(self, path):
        """
        returns the total weight of the given path,
        where path is an iterable of nodes' names.
        This method should return None if the path is not feasible in self.
        This method should return None if path is an empty iterable.
        Tip: The built-in functions any() and all() regard nonzero numbers as True and None as False.

        :param self:
        :param path:
        :return:
        """
        if len(path)==0:
            return None
        weight=0
        for name in path:
            if name in self.nodes:
                weight+=self.nodes.get_weight(name)

        return weight

    def dump(self,indentation='\t  '):
        prefix="grph {}:".format(self.name)
        for node in sorted(self.get_nodes(),key=str):
            prefix+="\n"+node.dump(indentation)
        return prefix

    def is_reachable(self, frm_name, to_name):
        """
        returns True if to_name is reachable from frm_name.
        This method should not fail if either frm_name or to_name are not in self.

        :param self:
        :param frm_name:
        :param to_name:
        :return:
        """
        path=self.find_shortest_path(frm_name, to_name)
        return path.weight !=None

    def find_every_shortest_path(self):
        pathes = []
        self.forget_edges()
        for src in sorted(self.get_nodes()):
            for trgt in sorted(self.get_nodes(),reverse=True):
                # I use sorted and reverse sorted for debuging and to increase the
                #  chances of early pathes will be lng ones
                # in memoize this can give better performance
                try:
                    # msg to Amit : memory is not an issue here so I remember and sor pathes
                    path = self.find_shortest_path(src, trgt)
                    if not self.please_memoize:
                        pathes.append(path)
                except RuntimeError as rt:
                    print "{}------>{}".format(src, trgt)
                    print "RuntimeError" + str(rt)
                    # print str(path)
        if self.please_memoize:
            pathes =  self.get_all_memoized_paths()
        return filter( lambda p : p.weight <self.INFINITY,pathes)

    def _remember_path(self,path,frm_name, to_name):
        path_id = (frm_name, to_name)
        if path_id in  self.memoized_pathes :
            return
        self.memoized_pathes[path_id] = path

    def find_shortest_path(self, frm_name, to_name):
        """
        returns the path from frm_name to to_name which has the minimum total weight.
        This method should return None if there is no path between frm_name and to_name.
        Note: path finding is usually implemented with recursion.
        We didn't learn recursion in our course, so I recommend implementing a
        non-recursive algorithm like "breadth-first search" or "depth-first search".

        :param self:
        :param frm_name:
        :param to_name:
        :return:
        """
        create_path_name=lambda src, trgt: "{} => {}".format(src, trgt)
        path_id=(frm_name, to_name)
        if self.please_memoize and path_id in  self.memoized_pathes:
            # print "path:{} exists".format(self.pathes[path_id])
            return self.memoized_pathes[path_id]

        distance, predecessor=self.BellmanFord(frm_name)

        path_name = create_path_name(frm_name, to_name)
        path = Path(path_name)
        path.from_predecessor(frm_name, to_name, predecessor,distance)
        if self.please_memoize:
            self._remember_path( path, str(frm_name), str(to_name))
            for index,name in enumerate(path,start=1):
                sub_path_name=create_path_name(frm_name, name)
                sub_path=path.sub_path(sub_path_name,name)
                self._remember_path(sub_path, frm_name, name)

        # print "pathes size {}: path name:{}".format(len(self.pathes),path_name)
        return path

    def BellmanFord(self, source_name):
        """
        This is Blman and Ford  algirithm implemantaion
        as described in the book by:
            T.H. Cormen, C.E. Leiserson, R.L. Rivest & C. Stein,
            Introduction to Algorithms, 2nd ed. (MIT Press, 2000)

        :param source_name:
        :return: distance and predecessor a dictionary and not as array
        """

        distance = {}
        predecessor = {}

        # This implementation takes in a graph, represented as set of vertices and edges,
        # and fills two arrays(distance and predecessor) with shortest - path
        # (less cost / distance / metric) information
        source=self[source_name]
        # Step 1 -  initialize
        for v in map( str,self.get_nodes()):
            distance[v] = self.INFINITY
            predecessor[v] = None
            # the  beginning, all vertices have a weight
            # of infinity (max int) predecessor[v]:= null
            # And a null predecessor
        distance[source] = 0  # Except  for the Source, where the Weight is zero

        # Step 2: relax edges repeatedly
        for i in range(1, len(self)):
            # print "Itration {}".format(i)
            for (u, v, w) in self.get_edges():
                # print "\t",e
                u=str(u)
                v=str(v)
                if distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w
                    predecessor[v] = u
                    # print  "\tdistance   :",self._str_dict(distance)
                    # print  "\tpredecessor:",self._str_dict(predecessor)
                    # print ""
                    # print "\n"

        # Step 3: check for negative - weight cycles
        for (u, v, w) in self.get_edges():
            u = str(u)
            v = str(v)
            if distance[u] + w < distance[v]:
                raise RuntimeError("Graph "+self.name+" contains a negative-weight cycle {}=>{}".format(source,u))



        return distance, predecessor