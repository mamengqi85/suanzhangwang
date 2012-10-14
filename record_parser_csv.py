#-*- coding: utf-8 -*- s

from datetime import datetime
import codecs
import os

from record import Record
from record_parser import RecordParser
from user import User
import helper

class RecordParserCsv(RecordParser):

    _user_lst = dict()
    _nick_lst = []

    def __init__(self, user_lst):
        self._user_lst = user_lst

    #hard code for now
    def parseTitle(self, line, style = "1411"):
        formats = dict()
        title_lst = ["amount", "payer", "memo", "date", "payed"]
        content = line.split(",")
        for i in range(len(content)):
            found = False
            for title in title_lst:
                if helper.helper.checkWords(title, content[i]):
                    formats[title] = i
                    found = True
                    break
            if found == False:
                for user in self._user_lst:
                    if user == content[i]:
                        self._nick_lst.append(user)
                        formats[user] = i
                        found = True
                        break
#        if style == "1411":
#            self._nick_lst = ["刘".decode("utf-8"), "陈".decode("utf-8"), "庄".decode("utf-8"), "马".decode("utf-8")]
#            formats["amount"] = 0
#            formats[self._nick_lst[0]] = 1
#            formats[self._nick_lst[1]] = 2
#            formats[self._nick_lst[2]] = 3
#            formats[self._nick_lst[3]] = 4
#            formats["payer"] = 5
#            formats["memo"] = 6
#            formats["date"] = 7
#            formats["payed"] = 8
        return formats

    def parse(self, entry, formats):
        content = entry.split(",")
        payees = []
        for i in range(len(self._nick_lst)):
            if helper.helper.checkWords("true", content[formats[self._nick_lst[i]]]):
                payees.append(self._user_lst[self._nick_lst[i]])
        payers = content[formats["payer"]]
        payers = payers.split("，".decode(helper.helper.INCODING))
        for i in range(len(payers)):
            payers[i] = self._user_lst[payers[i]]
        isPayed = False
        if len(content) == 9 and helper.helper.checkWords("true", content[formats["payed"]]):
            isPayed = True
        record = Record(
                amount = content[formats["amount"]],
                payee = payees,
                payer = payers,
                date = datetime.strptime(content[formats["date"]], helper.helper.DATE_FORM),
                memo = content[formats["memo"]],
                payed = isPayed
                )
        return record

#TODO: use tree map as return
    def parseFile(self, filename):
        content = codecs.open(filename, "r", helper.helper.OUTCODING)
        record_lst = set()
        first = True
        formats = None
        for line in content:
            line = line.strip()
            if first:
                formats = self.parseTitle(line, style = "1411")
                first = False
            else:
                record = self.parse(line, formats)
                record_lst.add(record)
        return record_lst

    def parseDir(self, pathname):
        record_lst = set()
        files = os.listdir(pathname)
        for filename in files:
            tmp_lst = self.parseFile(os.path.join(pathname, filename))
            record_lst.update(tmp_lst)
        return record_lst

if __name__ == "__main__":
    from user_parser_txt import UserParserTxt
    upt = UserParserTxt()
    user_lst = upt.parseDir("users")
    for user in user_lst:
        print user_lst[user].toString() + "\n"

    rpt = RecordParserCsv(user_lst)
    record_lst = rpt.parseDir("records")
    for record in record_lst:
        print record.toString() + "\n"
