def get_sum(number:int, operator:str):
    def print_table(number):
        for i in range(1, 11):
            if operator == '*':
                print(f"{number} * {i} = {number * i}")
            elif operator == '+':
                print(f"{number} + {i} = {number + i}")

    print_table(number)

    sum = number
    for i in range(9):
        number = number+1
        sum = sum + number

    return sum

if __name__ == '__main__':
    print('sum is', get_sum(5, '*'))