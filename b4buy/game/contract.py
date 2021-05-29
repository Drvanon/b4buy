class Contract:
    def __init__(self, player1, player2, end_date, money_transfer, order, frequency):
        self.player1 = player1
        self.player2 = player1
        self.end_date = end_date
        self.completed = False
        self.order = order
        self.frequency = frequency
