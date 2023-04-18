
def is_in_range(row, col, n):
    if 0 <= row < n and 0 <= col < n:
        return True
    return False

n = 6

matrix = []

b = []

points = 0

for row in range(n):
    matrix.append([el for el in input().split()])



for _ in range(3):

    row, col = [int(el) for el in input()[1:-1].split(', ')]


    if is_in_range(row, col, n):
        if [row, col] in b:
            continue
        elif matrix[row][col] == "B":
            for i in range(n):
                if matrix[i][col] != "B":
                    points += int(matrix[i][col])
            b.append([row, col])

    else:
        continue


if points < 100:
    print(f"Sorry! You need {100 - points} points more to win a prize.")
elif 100 <= points <= 199:
    print(f"Good job! You scored {points} points, and you've won Football.")
elif 200 <= points <= 299:
    print(f"Good job! You scored {points} points, and you've won Teddy Bear.")
else:
    print(f"Good job! You scored {points} points, and you've won Lego Construction Set.")