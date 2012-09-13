from user import User

class UserParser:
    def __init__(self):
        if self.__class__ is UserParser:
            raise NotImplementedError("abstract")

    def parse(self, entry):
        pass

    def parseFile(self, filename):
        pass

    def parseDir(self, pathname):
        pass

if __name__ == "__main__":
    up = UserParser()
    up.parse("hehe.txt")
