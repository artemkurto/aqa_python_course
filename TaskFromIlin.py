print("Input flat_number" )
flat_number = input()
flat_number = int(flat_number)
entrance_number = (flat_number - 1) // 20 + 1
print("entrance #", entrance_number)

floor_number = (flat_number -1) % 20 // 4 + 1
print("floor #", floor_number)