class Train:
    def __init__(self):
        self.wagons = [Wagons('HEAD')]

    def add_wagon(self, wagon_number):
        wagon = Wagons(wagon_number)
        self.wagons.append(wagon)


    def __len__(self):
        return len(self.wagons) - 1


    def __str__(self):
        return '<=[' + '] - ['.join(str(wagon.wagon_number) for wagon in self.wagons) + ']'


class Wagons:
    def __init__(self, wagon_number):
        self.wagon_number = wagon_number
        self.passengers = []

    def add_passengers(self, passenger):
        if len(self.passengers) < 10:
            self.passengers.append(passenger)
        else:
            print('Wagon is full')

    def __len__(self):
        return len(self.passengers)


train = Train()
train.add_wagon(1)
train.add_wagon(2)
train.add_wagon(3)

wagon1 = train.wagons[1]
wagon1.add_passengers("Mick")
wagon1.add_passengers("Clara")
wagon1.add_passengers("Mark")
wagon1.add_passengers("Joe")
wagon1.add_passengers("Suzanna")

print('Number of wagons: ', len(train))
print(train)
print('Number of passengers in wagon: ', len(wagon1.passengers))


