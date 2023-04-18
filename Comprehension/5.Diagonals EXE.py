n = int(input())

matrix = [[int(el) for el in input().split(', ')] for _ in range(n)]


first_diag = [matrix[i][i] for i in range(n)]
second_diag = [matrix[i][n-1-i] for i in range(n)]


sum_first = sum([int(el) for el in first_diag])
sum_second = sum([int(el) for el in second_diag])


print(f"First diagonal: {', '.join([str(el) for el in first_diag])}. Sum: {sum_first}")
print(f"Second diagonal: {', '.join([str(el) for el in second_diag])}. Sum: {sum_second}")