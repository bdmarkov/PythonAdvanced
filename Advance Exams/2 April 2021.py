import math

def outside(row, col):
    if row < 0 or row > 6 or col < 0 or col > 6:
        return True
    return False

def sumpoints(row, col):
    return int(matrix[0][col]) + int(matrix[6][col]) + int(matrix[row][0]) + int(matrix[row][6])

def which_turn():
    if count % 2 == 0:
        return second_name
    return first_name

first_name, second_name = input().split(', ')


players = {
    first_name: 501,
    second_name: 501
}

matrix = []
for i in range(7):
    matrix.append(input().split())

count = 0


while True:
    count += 1

    turn = which_turn()

    row, col = [int(el) for el in input()[1:-1].split(', ')]

    if outside(row, col):
        continue

    if row == 3 and col == 3:
        players[turn] = 0
    elif row == 0 or row == 6 or col == 0 or col == 6:
        players[turn] -= int(matrix[row][col])
    elif matrix[row][col] == "D":
        sumfour = sumpoints(row, col)
        players[turn] -= (sumfour * 2)
    else:
        sumfour = sumpoints(row, col)
        players[turn]-= (sumfour * 3)

    if players[turn] <= 0:
        print(f'{turn} won the game with {math.ceil(count / 2)} throws!')
        break

