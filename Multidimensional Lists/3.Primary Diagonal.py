n = int(input())

matrix = []
result = 0
for i in range(n):
    matrix.append([int(el) for el in input().split()])


for k in range(n):
    result += matrix[k][k]

print(result)