from  Social.Social import *
import unittest
class TestDatabase(unittest.TestCase):
    def setUp(self):
        file_name = "d:\\tmp\\social.txt"
        self.dl = DataLoader(file_name)
        self.dl.load_data()
        self.dl.lines=self.dl.lines[0:11]
        self.dl.prase_lines()
        # Manasseh and Joseph became friends.       ==>      Joseph+
        # Naphtali and Judah became friends.
        # Asher and Naphtali became friends.
        # Joseph and Dan became friends.            ==>DAN+  Joseph+
        # Gad and Issachar became friends.
        # Ephraim and Asher became friends.
        # Judah and Joseph became friends.          ==>      Joseph+
        # Issachar and Judah became friends.
        # Ephraim and Benjamin became friends.
        # Manasseh and Ephraim became friends.
        # Dan and Joseph cancelled their friendship.==>DAN-   Joseph-
        #                                           -------------------
        #                                       total:    0         2
    def test_Memmber(self):
        dl=self.dl
        activities =  filter(lambda a:'Dan' in a.members ,dl.get_activities_list())
        self.assertTrue(len(activities) == 2, "len(activities)={}\n".format(len(activities)))
        self.assertTrue(activities[0].operation==activities[0].became_friend,"Dan first acitvity")
        self.assertTrue(activities[1].operation == activities[0].cancelled_friendship, "Dan second acitvity")


    def test_DataLoader(self):
        dl=self.dl
        members = set(map(str, dl.get_members_list()))
        expected_members = set(['Asher', 'Benjamin', 'Dan', 'Ephraim', 'Gad',
                                'Issachar', 'Joseph', 'Judah', 'Manasseh',
                                'Naphtali'])

        activities=dl.get_activities_list()
        self.assertEquals(members,expected_members,"get_members_list {}".format(members-expected_members))
        self.assertTrue(len(activities)==11,"len(activities)={}\n{}".format(len(activities),dl.lines[-1]))

    def test_SocialNetwork(self):
        dl = self.dl
        members = dl.get_members_list()
        activities = dl.get_activities_list()
        social_net = SocialNetwork("social_net", members)
        social_net.performed_activities(*activities)
        self.assertTrue(len(social_net['Dan'])==0,"performed_activities")
        self.assertTrue(len(social_net['Joseph']) == 2, "performed_activities")