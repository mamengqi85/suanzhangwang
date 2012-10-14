#-*- coding: utf-8 -*- s

from user import User
import helper

class Group:
    name = ""
    members = set()
    ad = User()

    def __init__(self, name = "", members = set(), ad = User()):
        self.name = name
        self.members = members
        self.ad = ad

    def add(self, member):
        self.members.add(member)

    def remove(self, member):
        self.members.remove(member)

    def toString(self):
        members_lst = set()
        for member in self.members:
            members_lst.add(member._user_name)
        members_str = ",".join(members_lst)
        return "Group Name: {}\nAdministrator: {}\nMembers: {}".format(self.name.encode(helper.helper.OUTCODING), self.ad._user_name.encode(helper.helper.OUTCODING), members_str.encode(helper.helper.OUTCODING))

if __name__ == "__main__":
    group = Group()
    user1 = User("user1", "玩家1".decode("utf-8"), "test1", "pw1", "abe1@gmail.com", {"apt1411", "Cornell"})
    user2 = User("user2", "testName2", "test2", "pw2", "abe2@gmail.com", {"apt1411", "Cornell"})
    user3 = User("user3", "testName3", "test3", "pw3", "abe3@gmail.com", {"apt1411", "Cornell"})
    group.add(user1)
    print group.toString()
    group.add(user2)
    print group.toString()
    group.add(user1)
    print group.toString()
    group.remove(user1)
    print group.toString()
    group.add(user3)
    print group.toString()
