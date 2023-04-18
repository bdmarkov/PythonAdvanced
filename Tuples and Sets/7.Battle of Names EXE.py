n = int(input())

odd_set = set()
even_set = set()
sum_int = 0


for i in range(1, n+1):
    command = input()

    sum_ord = ([ord(el) for el in command])

    for k in sum_ord:
        sum_int += int(k)

    sum_int = sum_int // i

    if sum_int % 2 == 0:
        even_set.add(sum_int)
    else:
        odd_set.add(sum_int)

    sum_int = 0

sum_odd = sum(odd_set)
sum_even = sum(even_set)

if sum_odd == sum_even:
    result = odd_set.union(even_set)
elif sum_even > sum_odd:
    result = odd_set.symmetric_difference(even_set)
else:
    result = odd_set.difference(even_set)

print(', '.join([str(x) for x in result]))