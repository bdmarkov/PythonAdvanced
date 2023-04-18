from collections import deque

quantity = int(input())

orders = [int(el) for el in input().split()]
orders = deque(orders)
max_order = max(orders)
for i in range(len(orders)):

    order = orders.popleft()
    if order <= quantity:
       quantity -= order

    else:
        orders.appendleft(order)
        break




print(max_order)
if len(orders) == 0:
    print(f"Orders complete")
else:
    print(f'Orders left:',' '.join(str(order) for order in orders))