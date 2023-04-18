n = int(input())

matrix = []


for i in range(n):
    matrix.append([el for el in input()])


symbol = input()

position = None

for row in range(n):
    for col in range(n):
        if symbol in matrix[row][col]:
            position = (row, col)
            break

    if position:
        break


if position:
    print(position)
else:
    print(f"{symbol} does not occur in the matrix")