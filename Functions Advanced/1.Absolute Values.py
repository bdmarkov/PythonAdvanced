
def absolute_values(numbers):
    result =  [abs(el) for el in numbers]
    return result



nums = [float(el) for el in input().split()]

print(absolute_values(nums))