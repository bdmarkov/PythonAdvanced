
matrix = input().split('|')



new_matrix = []
for i in range(len(matrix) -1, -1, -1):
    for k in matrix[i].split():

        new_matrix.append(k.strip())


print(*new_matrix)