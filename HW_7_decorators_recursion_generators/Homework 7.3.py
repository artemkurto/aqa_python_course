import time


def decorator(fun):
    def wrapper(*args):
        time_before = time.time()
        result = fun(*args)
        time_after = time.time()
        print("Час виконання функції, сек: ", time_after - time_before)
        return result
    return wrapper


@decorator
def get_square(*args):
    res = []
    for k in range(*args):
        res.append(k ** 2)
    return res


print(get_square(2, 100000, 2))
