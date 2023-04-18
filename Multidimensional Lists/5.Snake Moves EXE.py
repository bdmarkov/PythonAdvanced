def create_blank_matrix(row, col):
    matrix = []
    for i in range(row):
        matrix.append([[] for el in range(col)])

    return matrix




n, m = input().split()
n, m = int(n), int(m)
word = input()

matrix = create_blank_matrix(n,m)

col = 0
text_index = 0

for row in range(n):
    if row % 2 == 0:
        dir = 1
    else:
        dir = -1


    while 0 <= col < m:
        matrix[row][col] = word[text_index]
        if text_index +1 == len(word):
            text_index = -1
        text_index += 1
        col += dir
    col -= dir


for i in range(len(matrix)):
    print(''.join(matrix[i]))































# count = 1
# count_word = 0
#
# matrix = []
#
# for i in range(n):
#     count += 1
#
#     if count % 2 == 0:
#         for j in range(m):
#
#             print(word[count_word], sep='')
#             matrix.append(word[count_word])
#             count_word += 1
#
#
#     else:
#         for l in range(m, -1, -1):
#             matrix.append(word[count_word])
#             print(word[count_word], sep='')
#             count_word += 1
#     print(*matrix)
