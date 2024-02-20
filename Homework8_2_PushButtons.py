from Homework8_2_Phones import Phones


class PushButtons(Phones):
    def __init__(self, name, price, weight, keyboard_type='standard', color_display=True):
        super().__init__(name, price, weight)
        self.keyboard_type = keyboard_type
        self.color_display = color_display

    def dial(self, phone_number):
        print(f'Calling to {phone_number}')


nokia3310 = PushButtons(color_display=False, name='nokia3310', price=40, weight=280)
nokia3310.dial('+3806745698745')
