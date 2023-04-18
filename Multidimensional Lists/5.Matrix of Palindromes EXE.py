row, col = input().split()

row, col = int(row), int(col)

matrix = []


for i in range(row):
    matrix.append([])
    for k in range(col):
        value = (chr(97+i)) + (chr(97+k+i)) + (chr(97+i))
        matrix[i].append(value)

for j in range(len(matrix)):
    print(' '.join(matrix[j]))