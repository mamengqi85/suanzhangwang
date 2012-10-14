#-*- coding: utf-8 -*- s

import codecs

class Helper:
    _entries = [
                "input_coding",
                "output_coding",
                "dateform",
                "true",
                "amount",
                "payer",
                "memo",
                "date",
                "payed"
                ]
    _word_set = dict()

    def __init__(self):
        self.parseConfig()

    def _parseLine(self, line):
        for i in range(len(self._entries)):
            ind = line.find(self._entries[i])
            if ind >= 0:
                res = line[ind + len(self._entries[i]) + 1:]
                res = res.strip()
                return (i, res)
        return (-1, None)

    def _getValue(self, val, path):
        inf = codecs.open(path)
        content = inf.read()
        i = content.find(val)
        res = content[i:]
        i = res.find("\n")
        res = res[len(val):i]
        res = res.replace("\r", "")
        inf.close()
        return res

    def checkWords(self, var, val):
        if var not in self._word_set:
            return False
        if val in self._word_set[var]:
            return True
        if var == "true" and val == 1:
            return True
        return False

    def parseConfig(self, path = "config.dat"):
        inf = codecs.open(path)
        for line in inf:
            (var, val) = self._parseLine(line)
            if var == -1:
                pass
            elif var == 0:
                self.INCODING = val
            elif var == 1:
                self.OUTCODING = val
            elif var == 2:
                self.DATE_FORM = val
        inf = codecs.open(path, "r", self.INCODING)
        for line in inf:
            (var, val) = self._parseLine(line)
            if var == 3:
                self._word_set["true"] = val.split(",")
            elif var == 4:
                self._word_set["amount"] = val.split(",")
            elif var == 5:
                self._word_set["payer"] = val.split(",")
            elif var == 6:
                self._word_set["memo"] = val.split(",")
            elif var == 7:
                self._word_set["date"] = val.split(",")
            elif var == 8:
                self._word_set["payed"] = val.split(",")

helper = Helper()

if __name__ == "__main__":
    helper = Helper()
    print helper.checkWords("true", 1)
    print helper.checkWords("memo", "备忘")
    print helper._word_set
    print helper.INCODING
