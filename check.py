from user import User

class Check:
    amount  = 0
    sender = User()
    receiver = User()

    def __init__(amount, sender, receiver):
        self.amount = amount
        self.sender = sender
        self.receiver = receiver
