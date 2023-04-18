numbers = input().split()

numbers = [int(el) *1.0 for el in numbers]
numbers_list = []
numbers = tuple(numbers)

for i in numbers:
    if i not in numbers_list:
        print(f"{i} - {numbers.count(i)} times")
        numbers_list.append(i)


