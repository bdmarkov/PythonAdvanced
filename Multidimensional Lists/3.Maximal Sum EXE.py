row, col = input().split()

row, col = int(row), int(col)

matrix = []

max_num = None
position = ()

for i in range(row):
    matrix.append([int(el) for el in input().split()])


for j in range(row-2):
    for k in range(col-2):
        current_sum = matrix[j][k] + matrix[j][k+1] + matrix[j][k+2] + matrix[j+1][k] + matrix[j+1][k+1] + matrix[j+1][k+2] + matrix[j+2][k] + matrix[j+2][k+1] + matrix[j+2][k+2]

        if max_num == None or current_sum > max_num:
            max_num = current_sum
            position = (j, k)



print(f"Sum = {max_num}")


row, col = position
print(f"{matrix[row][col]} {matrix[row][col+1]} {matrix[row][col+2]}")

print(f"{matrix[row+1][col]} {matrix[row+1][col + 1]} {matrix[row+1][col + 2]}")

print(f"{matrix[row+2][col]} {matrix[row+2][col + 1]} {matrix[row+2][col + 2]}")

