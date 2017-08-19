class Path(list):
    def __init__(self,name=""):
        self.INFINITY = 9223372036854775807
        self.name=name
        self.weight=self.INFINITY
        self.distance_dict=None
        self.predecessor_dict=None


    def sub_path(self,name,sub_target):
        """
         return path object
        """
        sub_path=Path(name)
        sub_path.from_predecessor(self[0],sub_target,
                                 self.predecessor_dict,
                                 self.distance_dict)
        return sub_path

    def from_predecessor(self,source,target,predecessor_dict,distance_dict):
        self.predecessor_dict=predecessor_dict
        self.distance_dict=distance_dict

        if distance_dict[target]==9223372036854775807:
            return

        self.insert(0,target)
        if source not in predecessor_dict:
            raise KeyError("Sourse:{} not in predecessor_dict".format(source))

        if target not in predecessor_dict:
            raise KeyError("Target:{} not in predecessor_dict".format(target))

        current = predecessor_dict[target]
        while current is not None: #and current != source:
            if current not in predecessor_dict:
                raise KeyError("current node:{} not in predecessor_dict".format(current))
                return
            self.insert(0,current)
            current=predecessor_dict[current]
        self.weight = distance_dict[target]
    _str_format="{:>15}: weight={:<8.2f} nodes={}"
    @classmethod
    def set_str_format(self,str_format="{:>15}: weight={:<8.2f} nodes={}"):
        Path._str_format=str_format
    def __str__(self):
        if self.weight==None:
            return "{:>15}:  not reachable".format(self.name)
        return Path._str_format.format(self.name,self.weight,str(map(str,list(self))))
