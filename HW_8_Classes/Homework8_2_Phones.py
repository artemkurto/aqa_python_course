from abc import abstractmethod


class Phones:

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    @abstractmethod  #абстракція
    def dial(self, phone_number):
        pass

    @staticmethod
    def calculator(num1, num2):
        result = num1 + num2
        print('Sum result: ', result)


Phones.calculator(3, 5)