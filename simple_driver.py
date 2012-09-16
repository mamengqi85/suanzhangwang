#-*- coding: utf-8 -*- s

from record import Record
from record_parser_csv import RecordParserCsv
from user import User
from user_parser_txt import UserParserTxt
import helper

import codecs
import os

class SimpleDriver(Driver):

        _user_dir = ""
        _record_dir = ""
        _user_lst = dict()
        _record_lst = {}

    def __init__:(self, usr_dir = "users", record_dir = "records"):
        self._user_dir = usr_dir
        self._record_dir = record_dir

    def parseAll(self):
        user_parser = UserParserTxt()
        self.user_lst = user_parser.parseDir(self._user_dir)
        record_parser = RecordParserCsv(usr_lst)
        self.record_lst = record_parser.parserDir(self._record_dir)

    def queryAll(self, start_date, end_date):
        if start_date > end_date:
            return 0
        for record in self._record_lst:
            if record.payed is False and record.date >= start_date and record.date <= end_date:
                pass



