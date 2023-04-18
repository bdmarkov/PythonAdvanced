n = int(input())

elements = set()

for i in range(n):
    ele = [el for el in input().split()]
    for l in ele:
        elements.add(l)



for i in elements:
    print(i)