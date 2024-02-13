def get_square():
    for num in range(0, 10, 2):
        square = num ** 2
        yield square


for square in get_square():
    print(square)