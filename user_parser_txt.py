import codecs
import os

from user import User
from user_parser import UserParser

class UserParserTxt(UserParser):

    def parse(self, entry):
        tmp = entry.split(" ")
        gp = tmp[5].split(",")
        return User(tmp[0], tmp[1], tmp[2], tmp[3], tmp[4], gp)

    def parseFile(self, filename):
        content = codecs.open(filename, "r", "utf-8")
        usr_lst = dict()
        for line in content:
            line = line.strip()
            usr = self.parse(line)
            usr_lst[usr._nick_name] = usr
        return usr_lst

    def parseDir(self, pathname):
        usr_lst = dict()
        files = os.listdir(pathname)
        for filename in files:
            tmp_lst = self.parseFile(os.path.join(pathname, filename))
            usr_lst.update(tmp_lst)
        return usr_lst

if __name__ == "__main__":
    upt = UserParserTxt()
    usr_lst = upt.parseDir("users")
    for usr in usr_lst:
        print usr_lst[usr].toString() + "\n"
