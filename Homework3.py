products_list = input("Enter the list of products by separating them with a space: ")
products_list = products_list.split()

while len(products_list) > 0:
    print("Your products list: ", products_list)
    change_products_list = ''

    while change_products_list == '':
        change_products_list = input('Enter "product name" to add it or "-product name" to del it: ')
    change_products_list = change_products_list.split()

    if change_products_list[0][0] == '-':
        change_products_list = [minus.replace('-', '') for minus in change_products_list]
        change_products_list = " ".join(change_products_list)

        if change_products_list in products_list:
            products_list.remove(change_products_list)
        else:
            print("Product isn't in the products_list")

    else:
        products_list += change_products_list

print('Your products list is empty. Program is over')
