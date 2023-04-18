n = int(input())

maximum = None

for i in range(n):
    first_range, second_range = input().split('-')

    first_range = first_range.split(',')
    second_range = second_range.split(',')

    first_range = int(first_range[0]), int(first_range[1])
    second_range = int(second_range[0]), int(second_range[1])

    near_point = max(first_range[0], second_range[0])
    far_point = min(first_range[1], second_range[1])

    current_span = far_point - near_point + 1

    if maximum is None or current_span > len(maximum):
        maximum = list(range(near_point, far_point + 1))

print(f"Longest intersection is {maximum} with length {len(maximum)}")