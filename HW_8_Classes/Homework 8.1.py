class PrivatBank:
    message = 'Welcome to class "PrivatBank"'

    def __init__(self, name, card_number, cvv, date, balance):
        self.name = name
        self.card_number = card_number
        self._cvv = cvv
        self.date = date
        self.__balance = balance

    def set_balance(self, new_balance):
        self.__balance = new_balance

    def top_up(self, num):
        self.__balance = self.__balance + num

    def withdraw(self, num):
        if num <= self.__balance:
            self.__balance -= num
        else:
            print('Not enough money for this operation')

    def get_print_balance(self):
        print('Your card balance: ', self.__balance)

    @staticmethod
    def print_static_method():
        print('We have used static method')

    @classmethod
    def print_message(cls):
        print(cls.message)


privat_usd = PrivatBank('usd', 31972345657813, 123, '11/25', 1000)

PrivatBank.print_message()
PrivatBank.print_static_method()
privat_usd.set_balance(3000)
privat_usd.top_up(500)
privat_usd.withdraw(1100)
privat_usd.get_print_balance()
PrivatBank.
