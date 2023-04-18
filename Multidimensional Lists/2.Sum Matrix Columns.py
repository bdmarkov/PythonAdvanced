rows, cols = [int(el) for el in input().split(', ')]

matrix = []
sums = 0


for i in range(rows):
    matrix.append([int(el) for el in input().split()])


for j in range(cols):
    sums = 0
    for k in range(rows):
        sums += matrix[k][j]
    print(sums)