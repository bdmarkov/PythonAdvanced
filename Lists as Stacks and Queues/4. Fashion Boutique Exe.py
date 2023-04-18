box = []

for clothin in input().split():
    box.append(int(clothin))

rack_capacity = int(input())

number_of_racks = 1
current_rack_weight = 0
for i in range(len(box)):
    clothing = box.pop()
    if clothing + current_rack_weight > rack_capacity:
        number_of_racks += 1
        current_rack_weight = 0
    current_rack_weight += clothing

print(number_of_racks)