from  Social.Social import *

# Task 2 - The social network implementation
# The file social.txt describes chronologically the intrigues among 14 friends.
# Use the data in the file and the classes you've defined to answer the
# following questions.
def test(got,expeceted, testname):
    if expeceted == got:
        print "OK   - {} ({})".format(testname,got)
    else:
        print "Error- "+testname
        print "  expected : {}".format(expeceted)
        print "      got  : {}".format(got)


file_name="d:\\tmp\\social.txt"
dl=DataLoader(file_name)
dl.load_data()
dl.prase_lines()
members=dl.get_members_list()
activities=dl.get_activities_list()
test(len(members),14, "Number of members")
test(len(dl.errors_log),0, "Number of errors")

print "###########################################################################"
print "#Question 1"
print "# What was the highest number of simultaneous friendships?"
print "#\n"
social_net=SocialNetwork("social_net",members)
social_net.performed_activities(*activities)
max_friendships_of_members=map(lambda m:m.get_max_friendships(),social_net.get_nodes())
max_simultaneous_friendships=max(max_friendships_of_members)
print "max_simultaneous_friendships={}\n".format(max_simultaneous_friendships)


print "###########################################################################"
print "# Question 2"
print "# What was the maximum number of friends Reuben had simultaneously?"
print "#\n"
print "Answer :{}\n".format(social_net["Reuben"].get_max_friendships())

print ""
print "###########################################################################"
print "# Question 3"
print "# At the current graph (considering all the data of the file),"
print "# what is the maximal path between nodes in the graph?"
print "#\n"

pathes=social_net.find_every_shortest_path()
sorted_pathes=sorted(pathes,key=lambda p:(-1*p.weight,len(p)))
print "\nAnswer:{}".format(sorted_pathes[0].weight)
fltr=lambda p: p.weight >=sorted_pathes[0].weight
filtered_pathes=filter( fltr ,pathes)
#print "list of max shortest pathes:"
#print "\n".join(map(str,filtered_pathes))

print "###########################################################################"
print "# Question 4"
print "# Implement a function called suggest_friend(graph, node_name)"
print "# that returns the name of the node with the highest number of"
print "# common friends with node_name, which is not already one of his friends."
print "#\n"
print "Answer:suggested_friends"
member_name="Reuben"
suggested_friends=social_net.suggest_friends(member_name)
for sf_name in suggested_friends:
    print "\t{} has {} mutual friend with {}".format(
        sf_name,
        len(social_net.get_mutual_friends(member_name,sf_name)),
        member_name)