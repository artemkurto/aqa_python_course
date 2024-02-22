first_number = float(input("Введіть перше число: "))
sign = input("Введіть знак операції: + - * / ")
second_number = float(input("Введіть друге число: "))

if sign == "+":
    result = first_number + second_number
    print("Результат складання дорівнює:", result)
elif sign == "-":
    result = first_number - second_number
    print("Результат вичитання дорівнює:", result)
elif sign == "*":
    result = first_number * second_number
    print("Результат множення дорівнює:", result)
elif sign == "/":
    if second_number == 0:
        print("На нуль ділити не можна")
    else:
        result = first_number / second_number
        print("Результат ділення дорівнює:", result)
else:
    print("Ви ввели некоректний математичний знак")