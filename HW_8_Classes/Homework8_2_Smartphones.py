from Homework8_2_Phones import Phones


class Smartphones(Phones):

    def __init__(self, name, price, weight, os, browser, touch_screen=True):
        super().__init__(name, price, weight)
        self.os = os
        self.touch_screen = touch_screen
        self.browser = browser

    def dial(self, phone_number):
        print(f'Calling to {phone_number}')

    def open_browser(self, browser):
        print(f'You opened {self.browser}')


samsung_a23 = Smartphones('Samsung A23', 350, 190, 'Android', browser='Chrome')
samsung_a23.dial("+380676815677")
samsung_a23.open_browser(samsung_a23.browser)