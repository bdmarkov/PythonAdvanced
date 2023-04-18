first_number, second_number = input().split()



first_set = set()
second_set = set()

for i in range(int(first_number)):
    num = input()
    first_set.add(num)

for i in range(int(second_number)):
    num = input()
    second_set.add(num)

new_set = first_set.intersection(second_set)

for i in new_set:
    print(i)
