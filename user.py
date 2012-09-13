class User:

    _uid = ""
    _user_name = ""
    _nick_name = ""
    _password = ""
    _email = ""
    _group = {}

    def __init__(self, uid = "", un = "", nn = "", pw = "", em = "", gp = {}):
        self._uid = uid
        self._user_name = un
        self._nick_name = nn
        self._password = pw
        self._email = em
        self._group = gp
        return

    def toString(self):
        groupStr = "][".join(self._group)
        return "User Name: {}\nNick Name: {}\nEmail: {}\n[{}]".format(self._user_name.encode("utf-8"), self._nick_name.encode("utf-8"), self._email, groupStr)

if __name__ == "__main__":
    user = User("123", "testName", "test", "pw", "abe@gmail.com", {"apt1411", "Cornell"})
    print user.toString()


