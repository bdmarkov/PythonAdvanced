n = int(input())

matrix = []

sum_first = 0
sum_second = 0

for i in range(n):
    matrix.append([int(el) for el in input().split()])



for j in range(n):
    sum_first += matrix[j][j]


for l in range(n):
    sum_second += matrix[l][(n-1)-l]


print(abs(sum_first - sum_second))
