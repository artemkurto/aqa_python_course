print("Введіть температуру в градусах Цельсія С")
temperature_c = input()
temperature_c = int(temperature_c)
temperature_f = temperature_c * 9/5 + 32
temperature_k = temperature_c + 273.15
print("Температура в Кельвінах дорівнює", temperature_k)
print("Температура в Фаренгейтах дорвівнює", temperature_f)