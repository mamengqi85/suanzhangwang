from record import Record

class RecordParser:
    def __init__(self):
        if self.__class__ is RecordParser:
            raise NotImplementedError("abstract")

    def parseFile(self, filename):
        pass

    def parseDir(self, pathname):
        pass

if __name__ == "__main__":
    rp = RecordParser()
    rp.parse("hehe.txt")
