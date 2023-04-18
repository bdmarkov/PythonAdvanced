row, col = input().split()

row = int(row)
col = int(col)

for i in range(row):
    for k in range(col):
        print(f"{chr(97 + i)}{chr(97 + i + k)}{chr(97 + i)}", end=" ")
    print()