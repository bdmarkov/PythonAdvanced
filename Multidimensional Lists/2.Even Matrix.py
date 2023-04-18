
n = int(input())

matrix = []

for i in range(n):
    matrix.append([int(el) for el in input().split(', ')])


even_matrix = []

for j in range(n):

    even_matrix.append([el for el in matrix[j] if el % 2 == 0])

print(even_matrix)