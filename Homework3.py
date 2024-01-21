products_list = input("Enter the list of products by separating them with a space: ")
products_list = products_list.split()
while len(products_list) > 0:
    print("Your products list: ", products_list)
    change_products_list = input("Enter product to add it or '-product to del it: ")
    change_products_list = change_products_list.split()
    if change_products_list[0][0] == '-':
        change_products_list = [item.replace('-', '') for item in change_products_list]
        change_products_list = " ".join(change_products_list)
        products_list.remove(change_products_list)
    else:
        products_list += change_products_list
print('Your products list is empty. Program is over')
