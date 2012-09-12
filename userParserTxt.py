from user import User
from userParser import UserParser
import codecs

class UserParserTxt(UserParser):

    def parse(self, entry):
        pass

    def parseFile(self, filename):
        content = codecs.open(filename, "r", "utf-8")
        usr_lst = dict()
        for line in content:
            usr = parse(line)
            usr_lst[usr._nick_name] = usr
        return usr_lst

    def parseDir(self, filename):
        pass


