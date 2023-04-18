from itertools import permutations

n = input()

perm = permutations(n)

for i in perm:
    print("".join(i))