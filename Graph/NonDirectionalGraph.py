from Graph import Graph

class NonDirectionalGraph(Graph):
    def __init__(self, name="", nodes=[]):
        """
        :param self:
        :param name: will be stored as string name is an identifier
        :param nodes: nodes is an iterable of Node instances
        :return:
        """

        Graph.__init__(self,name,nodes)
        self.validate()


    def validate(self):
        for (v,u,w) in Graph.get_edges(self):
            if not self.is_edge(u,v,w):
                raise ValueError("the edge {}->{}:w={} exisits but no counterpart.")

    def add_edge(self, frm_name, to_name, weight=1):
        Graph.add_edge(self,frm_name, to_name, weight)
        Graph.add_edge(self, to_name,frm_name, weight)


    def remove_edge(self, frm_name, to_name):
        Graph.remove_edge(self,frm_name,to_name)
        Graph.remove_edge(self,to_name,frm_name)

    def get_unique_edges(self):
        edges=set()
        for e in Graph.get_edges(self):
            edge = (max(e[0], e[1]), min(e[0], e[1]), e[2])
            edges.add(edge)
        return list(edges)
