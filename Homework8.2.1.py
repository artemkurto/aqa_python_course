class Phones:

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def dial(self, phone_number):
        print(f'Calling to {phone_number}')
