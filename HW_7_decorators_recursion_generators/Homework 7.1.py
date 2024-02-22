def decorator(function):
    def wrapper(num1, num2):
        print('Викликана функція:', function.__name__)
        return function(num1, num2)

    return wrapper


@decorator
def get_sum(num1, num2):
    return num1 + num2


@decorator
def get_mult(num1, num2):
    return num1 * num2


result1 = get_sum(5, 3)
print('Результат: ', result1)

result2 = get_mult(5, 3)
print('Результат: ', result2)
