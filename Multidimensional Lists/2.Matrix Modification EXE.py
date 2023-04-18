
n = int(input())

matrix = []

for i in range(n):
    matrix.append([int(el) for el in input().split()])


def is_valid(r,c):
    if (0 <= r and r < n) and (0 <= c and c < n):
        return True
    else:
        return False

command = input()

while command != "END":
    com, row, col, val = command.split()
    row, col, val = int(row), int(col), int(val)

    if is_valid(row, col):
        if com == "Add":
            matrix[row][col] += val
        else:
            matrix[row][col] -= val
    else:
        print('Invalid coordinates')

    command = input()


for k in range(len(matrix)):
    print(*matrix[k])
