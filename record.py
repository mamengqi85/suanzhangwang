#-*- coding: utf-8 -*- s

import helper
from datetime import datetime, date, time
from user import User

class Record:
    _payee = []
    _payer = []
    _amount = 0
    _date = 0
    _memo = ""
    _payed = False

    def __init__(self, payee = [], payer = [], amount = 0, date = None, memo = (), payed = False):
        self._payee = payee     #ower
        self._payer = payer
        self._amount = amount
        self._date = date
        self._memo = memo
        self._payed = payed
        return

    def toString(self):
        payee_lst = []
        for i in range(0, len(self._payee)):
            payee_lst.append(self._payee[i]._nick_name)
        payee_gp = ", ".join(payee_lst)
        payer_lst = []
        for i in range(0, len(self._payer)):
            payer_lst.append(self._payer[i]._nick_name)
        payer_gp = ", ".join(payer_lst)
        return "Date: {}\nAmount: {}\nPayee: {}\nPayer: {}\nMemo: {}\nPayed: {}".format(self._date.strftime("%Y-%m-%d"), 
            self._amount, payee_gp.encode(helper.helper.OUTCODING), 
            payer_gp.encode(helper.helper.OUTCODING), 
            self._memo.encode(helper.helper.OUTCODING), self._payed)

if __name__ == "__main__":
    date = datetime.strptime("20120910", "%Y%m%d")
    user1 = User("user1", "testName1", "test1", "pw1", "abe1@gmail.com", {"apt1411", "Cornell"})
    user2 = User("user2", "testName2", "test2", "pw2", "abe2@gmail.com", {"apt1411", "Cornell"})
    user3 = User("user3", "testName3", "test3", "pw3", "abe3@gmail.com", {"apt1411", "Cornell"})
    record = Record([user1, user2], [user3], 100, date, "岳阳楼".decode(helper.helper.INCODING))
    print record.toString()
