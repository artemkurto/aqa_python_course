products_list = input("Enter the list of products by separating them with a space: ").split()

while len(products_list) > 0:
    print("Your products list: ", ', '.join(products_list))
    change_products_list = ''
    while change_products_list == '':
        change_products_list = input('Enter "product name" to add it or "-product name" to del it: ')

    if change_products_list.startswith('-'):
        change_products_list = change_products_list.lstrip('-')

        if change_products_list in products_list:
            products_list.remove(change_products_list)
        else:
            print(f"{change_products_list} isn't in the products_list")

    else:
        change_products_list = change_products_list.split()
        products_list += change_products_list

print('Your products list is empty. Program is over')
