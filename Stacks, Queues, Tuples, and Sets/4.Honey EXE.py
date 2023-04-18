from collections import deque

def operator(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    if operator == '-':
        return num1 - num2
    if operator == '*':
        return num1 * num2
    if operator == '/':
        if num1 == 0 or num2 == 0:
            return 0
        return num1 / num2

working_bees = [int(el) for el in input().split()]
nectar = [int(el) for el in input().split()]
symbols = [el for el in input().split()]

honey = 0



while True:

    if working_bees[0] > nectar[-1]:
        nectar.pop(-1)
    else:
        honey += abs(operator(working_bees[0],symbols[0],nectar[-1]))
        working_bees.pop(0)
        nectar.pop(-1)
        symbols.pop(0)
    if len(working_bees) == 0 or len(nectar) == 0:
        break

print(f'Total honey made: {honey}')
if working_bees:
    print(f'Bees left: {", ".join([str(el) for el in working_bees])}')
if nectar:
    print(f'Nectar left: {", ".join([str(el) for el in nectar])}')

