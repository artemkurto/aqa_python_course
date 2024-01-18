print("Введіть перше число")
first_number = float(input())
print("Введіть знак операції: + - * / ")
sign = input()
print("Введіть друге число")
second_number = float(input())
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
        print("На нуль деліти не можна")
    else:
        result = first_number / second_number
        print("Результат ділення дорівнює:", result)
else:
    print ("Ви ввели некоректний математичний знак")