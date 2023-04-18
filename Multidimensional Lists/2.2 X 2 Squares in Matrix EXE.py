row, col = input().split()

row, col = int(row), int(col)

matrix = []
count = 0
for i in range(row):
    matrix.append([el for el in input().split()])

for k in range(row-1, 0, -1):
    for l in range(col-1, 0, -1):
        if matrix[k][l] == matrix[k][l-1] and matrix[k][l] == matrix[k-1][l-1] and matrix[k][l] == matrix[k-1][l]:
            count += 1


if count > 0:
    print(count)
else:
    print(0)