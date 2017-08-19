from Graph.Node import Node
from Graph.Path import Path
from Graph.NonDirectionalGraph import  NonDirectionalGraph

class Member(Node):
    """
    Memeber extends Graph.Node as node in social network
    this member is keeping the history of number of frienships
    """
    def __init__(self,name):
        Node.__init__(self,name)
        #TODO: history is better implemented as classpropaty
        self._len_friendships_history=[]

    def add_neighbor(self, other, weight=1):
        Node.add_neighbor(self,other, weight)
        self._len_friendships_history.append(len(self))

    def remove_neighbor(self, other):
        Node.remove_neighbor(self, other)
        self._len_friendships_history.append(len(self))

    def get_max_friendships(self):
        return max(self._len_friendships_history)

class Activity:
    """
    Activity represnts adding friend or canceling
    friendship in th acrivity log
    TODO: A better wa to implement this class is as a clouser
          that get dictionary of operation and parser function and return
          factory of a activities.

    """
    def __init__(self,line):
        self.line=line
        self.members=(None,None) # just for declaration
        self.operation=None
        #TODO: this should be class property
        self.became_friend="became friend"
        #TODO: this should be class property
        self.cancelled_friendship="cancelled their friendship"
        self._parse(line)

    def _parse(self,line):
        """
        example of lines
        'Manasseh and Ephraim became friends.'
        'Dan and Joseph cancelled their friendship.'
        :param line:
        :return:
        """
        if line.count(self.became_friend)>0:
            self.operation=self.became_friend
        elif line.count(self.cancelled_friendship)>0:
            self.operation = self.cancelled_friendship
        else:
            raise ValueError("can not parse line:'{} - operation not valid.'".format(line))
        tmp=line.split()
        if tmp[1]!='and':
            raise ValueError("can not parse line:'{}' - could not detect members.".format(line))
        self.members=set([tmp[0],tmp[2]])

class SocialNetwork(NonDirectionalGraph):
    def __init__(self,name,members):
        NonDirectionalGraph.__init__(self,name,members)
        Path.set_str_format("{:>30}: distance={:<3} path members:{}")
        self.mutuality = dict()

    def performed_activities(self,*activities):
        for activity in activities:
            if activity.operation == activity.became_friend:
                self.add_edge(*activity.members)
            elif activity.operation == activity.cancelled_friendship:
                self.remove_edge(*activity.members)
            else:
                raise RuntimeError("operation: '{}' not handled.".format(activity.operation))

    def get_mutual_friends(self,member_a,member_b):
        return set(self[member_a].neighbors)&set(self[member_b].neighbors)

    def suggest_friends(self, member_name):
        """

        :param member:
        :return:The name of the member with the highest number of
                common friends with member_name, which is not already
                one of his friends."
        """
        # get friends names
        friends_names=set(self[member_name].neighbors)
        # get other memebers which ar not fiends yet
        others= set(self.get_nodes_names()) - friends_names -set(member_name)

        for other in others:
            len_mutual =len(self.get_mutual_friends(other,member_name))
            if len_mutual not in self.mutuality:
                self.mutuality[len_mutual]=[]
            self.mutuality[len_mutual].append(other)

        max_mutuality=max(self.mutuality)

        return self.mutuality[max_mutuality]


class DataLoader:
    def __init__(self,file_name):
        self.file_name=file_name
        self.activities=[]
        self.members=set()
        self.errors_log=[]
        self.lines=[] # I keep lines mainly for testing


    def load_data(self):
        with open(self.file_name,'r') as in_f:
            self.lines=map(lambda s:s.strip("\r\n"),in_f.readlines())
    def prase_lines(self):
            for i,line in enumerate(self.lines):
                try:
                    activity=Activity(line)
                    self.activities.append(activity)
                    members=set([Member(m) for m in activity.members ])
                    self.members|=members
                except Exception as e:
                    self.errors_log.append("line:{:>4} '{}'  - {}".format(i+1, line, e))

    def get_members_list(self):
        return list(self.members)

    def get_activities_list(self):
        return self.activities


