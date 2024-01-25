user_input = input("Введіть рядок: ")
print(', '.join(f"{char} = {user_input.count(char)}" for char in set(user_input)))