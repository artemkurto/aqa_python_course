string_for_calculate = input("Для прорахунку кількості символів, введіть будь-який текст: ")
dict_for_calculate = {}

for word in string_for_calculate:
    if word in dict_for_calculate:
        dict_for_calculate[word] += 1
    else:
        dict_for_calculate[word] = 1

for el in dict_for_calculate:
    print((f"Символ '{el}' зустрічається {dict_for_calculate.get(el)} раз"))
