from collections import deque


chocolates = [int(el) for el in input().split(', ')]
milk = deque([int(el) for el in input().split(', ')])


milkshakes = 0

while milk and chocolates and milkshakes < 5:
    chocolate = chocolates.pop()
    milk_cup = milk.popleft()

    if chocolate <= 0 and milk_cup <= 0:
        continue
    if chocolate <= 0:
        milk.appendleft(milk_cup)
        continue
    if milk_cup <= 0:
        chocolates.append(chocolate)
        continue

    if chocolate == milk_cup:
        milkshakes += 1
    else:
        milk.append(milk_cup)
        chocolates.append(chocolate - 5)


if milkshakes == 5:
    print(f'Great! You made all the chocolate milkshakes needed!')
else:
    print(f'Not enough milkshakes.')
if chocolates:
    print(f'Chocolate: {", ".join([str(el) for el in chocolates])}')
else:
    print(f'Chocolate: empty')
if milk:
    print(f'Milk: {", ".join([str(el) for el in milk])}')
else:
    print(f'Milk: empty')