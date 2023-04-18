from collections import  deque


pizza_orders = deque([int(el) for el in input().split(', ')])
employees = [int(el) for el in input().split(', ')]

pizzas = 0

while pizza_orders and employees:
    pizza = pizza_orders.popleft()
    capacity = employees.pop()


    if pizza > 10:
        employees.append(capacity)
        continue
    if pizza <= 0:
        employees.append(capacity)
        continue

    if pizza <= capacity:
        pizzas += pizza

    elif pizza > capacity:
        pizzas += capacity
        remain = pizza - capacity
        while True:
            if employees:
                capacity = employees.pop()
            else:
                pizza_orders.appendleft(remain)
                break
            if remain <= capacity:
                pizzas += (remain)
                break
            else:
                pizzas += remain - capacity
                remain = remain - capacity



if not pizza_orders:
    print(f'All orders are successfully completed!')
    print(f'Total pizzas made: {pizzas}')
    print(f'Employees: {", ".join([str(x) for x in employees])}')
else:
    print(f'Not all orders are completed.')
    print(f'Orders left: {", ".join([str(x) for x in pizza_orders])}')