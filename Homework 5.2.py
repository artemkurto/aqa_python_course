class FormulaError(Exception):
    pass


class WrongOperatorError(Exception):
    pass


counter = 1
while counter < 4:
    try:
        data_from_user = input("Enter values as an example: '3 * 2' or '3 / 2': ").split()

        if len(data_from_user) != 3:
            raise FormulaError("Error: Not 3 values entered")

        float_first_number = float(data_from_user[0])
        str_operator = data_from_user[1]
        float_second_number = float(data_from_user[2])

        if str_operator not in ['/', '*']:
            raise WrongOperatorError('Error: Incorrect operator')
        if str_operator == '/' and float_second_number == 0:
            raise ZeroDivisionError('ZeroDivisionError')

        if str_operator == '/':
            result = float_first_number / float_second_number
            print('Result: {:.2f}'.format(result))
            break
        elif str_operator == '*':
            result = float_first_number * float_second_number
            print('Result: {:.2f}'.format(result))
            break

    except FormulaError as e:
        print(e)
        counter += 1
    except WrongOperatorError as e:
        print(e)
        counter += 1
    except ValueError as e:
        print("Error: Entered is not a number")
        counter += 1
    except ZeroDivisionError as e:
        print(e)
        counter += 1

else:
    print('You have exhausted 3 attempts to enter correct values')
