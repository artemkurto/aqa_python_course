from Homework8_2_Smartphones import Smartphones


class Android(Smartphones):

    def __init__(self, name, price, weight, android_ver, benchmark_score, browser, os='android'):
        super().__init__(name, price, weight, os, browser)
        self.os = os
        self.android_ver = android_ver
        self.benchmark_score = benchmark_score

    def print_price_performance_ratio(self, price): #поліморфізм
        benchmark_score = self.get_benchmark_ratio(self.benchmark_score)
        price_performance_ratio = benchmark_score / price
        print(f'{self.name} price_performance_ratio: {price_performance_ratio}')

    def get_benchmark_ratio(self, benchmark_score): #інкапсуляція
        print('Looking for benchmark score ...')
        return self.benchmark_score


xiaomi11 = Android('Xiaomi11', 500, 220, 13.5, 7050, browser='Chrome')

xiaomi11.print_price_performance_ratio(xiaomi11.price)
