import codecs
import os

from group import Group
from user import User
from user_parser import UserParser
import helper

class UserParserTxt(UserParser):

    def parse(self, entry, gp_lst):
        tmp = entry.split(" ")
        gp = tmp[5].split(",")
        user =  User(tmp[0], tmp[1], tmp[2], tmp[3], tmp[4], gp)
        for group in gp:
            if group not in gp_lst:
                gp_lst[group] = Group()
            gp_lst[group].add(user)
        return user

    def parseFile(self, filename, gp_lst):
        content = codecs.open(filename, "r", helper.helper.INCODING)
        usr_lst = dict()
        for line in content:
            line = line.strip()
            usr = self.parse(line, gp_lst)
            usr_lst[usr._nick_name] = usr
        return usr_lst

    def parseDir(self, pathname, gp_lst):
        usr_lst = dict()
        files = os.listdir(pathname, gp_lst)
        for filename in files:
            tmp_lst = self.parseFile(os.path.join(pathname, filename))
            usr_lst.update(tmp_lst)
        return usr_lst

if __name__ == "__main__":
    upt = UserParserTxt()
    usr_lst = upt.parseDir("users")
    for usr in usr_lst:
        print usr_lst[usr].toString() + "\n"
