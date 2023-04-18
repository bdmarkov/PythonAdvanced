n = int(input())

matrix = []

for i in range(n):
    matrix.append([int(el) for el in input().split(', ')])


primary_diagonal = []
secondary_diagonal = []

for k in range(n):
    primary_diagonal.append(matrix[k][k])

for l in range(n):
    secondary_diagonal.append(matrix[l][(n-1)-l])


print(f"Primary diagonal: {', '.join([str(el) for el in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(el) for el in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")
