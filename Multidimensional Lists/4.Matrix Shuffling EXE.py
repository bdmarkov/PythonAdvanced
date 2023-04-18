row, col = input().split()

row, col = int(row), int(col)


matrix = []

for i in range(row):
    matrix.append([el for el in input().split()])


command = input()

while not command == "END":

    len_split = len(command.split())

    if "swap" in command and len_split == 5:
        com, i1, i2, i3, i4 = command.split()
        i1, i2, i3, i4 = int(i1), int(i2), int(i3), int(i4)


        if len(matrix) < i1 or len(matrix) < i2 or len(matrix[0]) < i3 or len(matrix[0]) < i4:
            print("Invalid input!")
        else:
            num = matrix[i1][i2]
            swap_num = matrix[i3][i4]

            matrix[i1][i2] = swap_num
            matrix[i3][i4] = num
            for j in range(row):
                for k in range(col):
                    print(matrix[j][k], end=' ')
                print()
    else:
        print("Invalid input!")

    command = input()

