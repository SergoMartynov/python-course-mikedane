try:
    number = int(input('Enter a number: '))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError as wrong_value:
    print(wrong_value)
