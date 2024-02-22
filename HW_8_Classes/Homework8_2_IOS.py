from Homework8_2_Smartphones import Smartphones


class Iphone(Smartphones):

    def __init__(self, name, price, weight, ios_ver, browser, os="ios"):
        super().__init__(name, price, weight, os, browser)
        self.ios_ver = ios_ver
        self.os = os

    def download_app(self, name):
        app_name = input('Write app name: ')
        print(f'You download {app_name} to {self.name}')

    def print_price_performance_ratio(self, price):  # поліморфізм
        benchmark_score = self.get_benchmark_ratio(self.name)
        price_performance_ratio = benchmark_score / price
        print(f'{self.name} price_performance_ratio: {price_performance_ratio}')

    def get_benchmark_ratio(self, name):  # інкапсуляція
        if self.name == 'Iphone14':
            benchmark_score = 9034
            return benchmark_score
        else:
            print(f'No data for {self.name}')
            return 0


iphone14 = Iphone('Iphone14', 800, 170, 14.3, browser='Safari')

# iphone14.download_app(iphone14.name)

iphone14.print_price_performance_ratio(iphone14.price)
