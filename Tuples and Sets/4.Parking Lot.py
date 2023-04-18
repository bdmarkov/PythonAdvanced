n = int(input())

parking_lot = set()

for _ in range(n):
    command, car = input().split(', ')
    if command == "IN":
        parking_lot.add(car)
    else:
        parking_lot.remove(car)

if parking_lot:
    for car in parking_lot:
        print(car)
else:
    print('Parking Lot is Empty')