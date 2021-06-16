from datetime import datetime

class Contract:
    def __init__(self, player1, player2, money_transfer, order, frequency, start_date=None, end_date=None):
        self.player1 = player1
        self.player2 = player2
        self.completed = False
        self.order = order
        self.frequency = frequency

        if not start_date:
            start_date = datetime.now()
        self.start_date = start_date
        self.end_date = end_date
