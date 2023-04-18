
def get_magic_triangle(param):
    matrix = [[1], [1, 1]]

    for i in range(2, param):
        matrix.append([])
        for k in range(i + 1):
            if k == 0 or k == i:
                matrix[i].append(int(1))
            else:
                suming = int(matrix[i - 1][k - 1]) + int(matrix[i - 1][k])
                matrix[i].append(suming)

    return matrix



get_magic_triangle(5)