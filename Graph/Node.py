class Node:
    def __init__(self,name):
        """The method does not have to test the validity of name."""

        self.name = name # the .name. of the node
        hash(name)       # name can be any immutable object,
                         # most naturally a string or a number.
        self.neighbors=dict()   # a dictionary of the neighbors with the neighbors.
                                # names as keys and the weights of the corresponding
                                #  edges as values.

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return str(self.name)

    def __len__(self):
        """
        :return:the number of neighbors
        """
        return  len(self.neighbors)

    def __eq__(self, other):
        """
        :param other: based on the name attribute
        :return: bool
        """
        #based on the name attribute
        return  self.name == Node(other).name

    def __ne__(self, other):
        """
        :param other: based on the name attribute
        :return: bool
        """
        return self.name != other.name

    def is_neighbor(self, name):
        """
        :param name:
        :return: True if name is a neighbor of self.
        """
        return name in self.neighbors

    def add_neighbor(self, other, weight=1):
        """
        adds name as a neighbor of self.
        This method does not test whether a node named name exists.
        This method does not allow adding a neighbor with a name of
        an existing neighbor.
        This method does not allow adding a neighbor with the same name as self.

        :param other:
        :param weight: somthing that can be converted into float (negative or positive)
        :return:
        """
        if other == self:
            raise NameError("Node can not be neighbor of itself."+str(self))
        if self.is_neighbor(other):
            raise ValueError("This Node is already a neighbor: " + str(other) +
                             " with weight:" + str(self.neighbors[other]))
        # I allow negative values
        self.neighbors[other]=float(weight)

    def copy_neighbors_of(self,node):
        """
        copies only non exists neighbors from node
        :param node:
        :return:
        """
        for neighbor in node.neighbors:
            if neighbor not in self.neighbors:
                self.add_neighbor(neighbor,node.get_weight(neighbor))

    def remove_neighbor(self, other):
        """
        removes name from being a neighbor of self.
        This method does not test whether a node named name exists.
        This method should not fail if name is not a neighbor of self.
        """
        self.neighbors.pop(other)

    def get_weight(self, name):
        """
        This method return None if name is not a neighbor of self.
        :param name:
        :return: returns the weight of the relevant edge.
        """
        return self.neighbors[name]

    def get_total_weight(self):
        return sum(self.neighbors.values())

    def is_isolated(self):
        """
        returns True if self has no neighbors
        """
        return len(self.neighbors)==0

    def get_edges(self):
        return map(lambda (n,w): (str(self),str(n),w),self.neighbors.items() )

    def get_neighbors_names(self):
        return self.neighbors

    def dump(self,indentation='\t'):
        prefix="node {:>4}:".format(str(self))
        if self.is_isolated():
            return prefix+ " is_isolated!"

        edges=map(lambda n : "  -->{:>2} : w={:>4}".format(n,self.get_weight(n)),
                  self.neighbors)
        seperator="\n {}".format(indentation)
        return prefix+seperator+seperator.join(edges)
