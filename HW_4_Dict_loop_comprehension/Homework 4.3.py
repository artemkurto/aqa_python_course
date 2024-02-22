names = ['Jack', 'Leon', 'Alice', None, 32, 'Bob']

for name in names:
    if type(name) is not str:
        continue
    print(name)
