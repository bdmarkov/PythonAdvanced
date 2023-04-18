def rounding(numbers):
    return [round(el) for el in numbers]

nums = [float(el) for el in input().split()]

print(rounding(nums))