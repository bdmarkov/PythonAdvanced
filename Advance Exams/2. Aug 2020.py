def is_in_range(row, col, n):
    if 0 <= row < n and 0 <= col < n:
        return True
    return False


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "up_right": (-1, 1),
    "up_left": (-1, -1),
    "down_right": (1, 1),
    "down_left": (1, -1)
}

n = int(input())
number_bombs = int(input())

position_bombs = []



bomb_list = []

for el in position_bombs:

    bomb_list.append(int(el[0]))
    bomb_list.append(int(el[1]))


matrix = []

for row in range(n):
    matrix.append([])
    for col in range(n):
        matrix[row].append(0)

for i in range(number_bombs):
    [row, col] = map(lambda x: int(x), input()[1:][:-1].split(', '))
    matrix[row][col] = '*'

mines = 0
for r in range(n):
    for c in range(n):
        for direction in directions:
            next_row = r + directions[direction][0]
            next_col = c + directions[direction][1]
            if is_in_range(next_row, next_col, n) and matrix[r][c] != '*':
                if matrix[next_row][next_col] == '*':
                    mines += 1

        if mines > 0:
            matrix[r][c] = mines
            mines = 0

for i in range(n):
    print(*matrix[i])
