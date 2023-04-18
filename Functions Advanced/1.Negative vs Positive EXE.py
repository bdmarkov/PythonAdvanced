numbers = [int(el) for el in input().split()]

def nums(numbers):

    sum_neg = 0
    sum_pos = 0

    for i in numbers:
        if i >= 0:
            sum_pos += i
        else:
            sum_neg += i

    print(sum_neg)
    print(sum_pos)

    if sum_pos > abs(sum_neg):
        return f"The positives are stronger than the negatives"
    return f"The negatives are stronger than the positives"




print(nums(numbers))