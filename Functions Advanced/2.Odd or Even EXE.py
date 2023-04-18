command = input()

numbers = [int(el) for el in input().split()]


def odd_or_even(nums):
    filter = []

    if command == "Even":
        filter = filter(lambda num:num % 2 == 0, nums)
    else:
        filter = filter(lambda num:num % 2 != 0, nums)


    return sum(filter) * len(nums)



print(odd_or_even(numbers))