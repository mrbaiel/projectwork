class Piggy:
    def __init__(self, balance = 0, max_size = 500):
        self.balance = balance
        self.max_size = max_size

    def add_coin(self, coins):
        if self.balance + coins > self.max_size:
            return( f"max size is {self.max_size} it's full")
        else:
            balance += coins

    def get_coin(self, coins):
        self.balance -= coins

    def show_balance(self):
        return self.balance

    def delete_coins(self):
        if self.balance > 0:
            self.balance - -1
        else:
            self.balance == 0
