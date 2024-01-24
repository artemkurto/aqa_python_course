dictionary = {
    'Alex': 'House',
    'Max': 'Flat',
    'Olha': 'Appartments',
    'Oleh': 'Trench'
}

for name in dictionary:
    print(f"{name} is living in {dictionary.get(name)}")
