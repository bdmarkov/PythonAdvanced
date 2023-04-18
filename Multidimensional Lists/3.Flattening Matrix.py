n = int(input())

matrix = []

for i in range(n):
    matrix.append([int(el) for el in input().split(', ')])

new_matrix = []

for j in range(n):
    new_matrix.extend(matrix[j])

print(new_matrix)