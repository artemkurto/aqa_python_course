list = {'Alex', None, 'Peter'}

for el in list:
    if el is None:
        break
else:
    print("There is no None")
