#-*- coding: utf-8 -*- s

from driver import Driver
from record import Record
from record_parser_csv import RecordParserCsv
from user import User
from user_parser_txt import UserParserTxt
import helper

from datetime import datetime
import codecs
import os

class SimpleDriver(Driver):

    _user_dir = ""
    _record_dir = ""
    _user_lst = dict()
    _record_lst = {}
    _report = dict()

    def __init__(self, usr_dir = "users", record_dir = "records"):
        self._user_dir = usr_dir
        self._record_dir = record_dir

    def parseAll(self):
        user_parser = UserParserTxt()
        self._user_lst = user_parser.parseDir(self._user_dir)
        record_parser = RecordParserCsv(self._user_lst)
        self._record_lst = record_parser.parseDir(self._record_dir)

    #TODO: use array or DB
    def queryAll(self, start_date = datetime.min, end_date = datetime.max):
        total = 0
        if start_date > end_date:
            return 0
        for record in self._record_lst:
            if record._payed is False and record._date >= start_date and record._date <= end_date:
                sub_amount = float(record._amount) / len(record._payee) / len(record._payer)
                for payer_entry in record._payer:
                    for payee_entry in record._payee:
                        if payer_entry == payee_entry:
                            continue
                        if payer_entry not in self._report:
                            self._report[payer_entry] = dict()
                        if payee_entry not in self._report:
                            self._report[payee_entry] = dict()
                        if payer_entry not in self._report[payee_entry]:
                            self._report[payee_entry][payer_entry] = -sub_amount
                        else:
                            self._report[payee_entry][payer_entry] -= sub_amount
                        if payee_entry not in self._report[payer_entry]:
                            self._report[payer_entry][payee_entry] = sub_amount
                        else:
                            self._report[payer_entry][payee_entry] += sub_amount
                        total += sub_amount
        print "total" + str(total)

    def payAll(self, start_date = datetime.min, end_date = datetime.max):
        for record in self._record_lst:
            if record._date >= start_date and record._date <= end_date:
                record._payed = True

    def reportAll(self):
        output = []
        for usr in self._report:
            output.append("user:" + usr._user_name)
            for other in self._report[usr]:
                output.append(other._nick_name + str(self._report[usr][other]))
            output.append("")
        return "\n".join(output)

if __name__ == "__main__":
    driver = SimpleDriver()
    driver.parseAll()
    driver.queryAll()
    output = driver.reportAll()
    print output


