import time


def decorator(fun):
    def wrapper(num1, num2):
        time_before = time.time()
        fun(num1, num2)
        time_after = time.time()
        print("Час виконання функції, сек: ", round(time_after - time_before, 2))

    return wrapper


@decorator
def get_square(num1, num2):
    for k in range(num1, num2):
        square = k ** 2
        print(square)


get_square(2, 100000)
