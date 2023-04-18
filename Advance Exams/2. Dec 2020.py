
def outside(row, col):
    if row < 0 or col < 0 or row == n or col == n:
        return True
    return False

def direction(direction, r, c):
    if direction == 'up':
        return r - 1, c
    if direction == 'down':
        return r + 1, c
    if direction == 'left':
        return r, c - 1
    return r, c + 1

word = input()
n = int(input())

matrix = []

for row in range(n):
    matrix.append([el for el in input()])


row, col = 0, 0

for r in range(n):
    for c in range(n):
        if matrix[r][c] == "P":
            row, col = r, c


moves = int(input())

path = [[row, col]]

for i in range(moves):
    command = input()

    row, col = direction(command, row, col)
    path.append([row, col])

    if outside(row, col):
        if len(word) > 0:
            word = word[0:-1]
        row, col = path[0][0], path[0][1]
        path.pop(1)
        continue


    if matrix[row][col].isalpha():
        word += matrix[row][col]
        matrix[row][col] = "P"
        r, c = path[0][0], path[0][1]
        matrix[r][c] = '-'
        path.pop(0)
    elif matrix[row][col] == "-":
        r, c = path[0][0], path[0][1]
        matrix[r][c] = '-'
        matrix[row][col] = "P"
        path.pop(0)


print(word)
for i in range(n):
    print(''.join(matrix[i]))