from collections import deque

queue = deque()

quantity = int(input())

names = input()

while not names == "Start":
    queue.append(names)
    names = input()

command = input()

while not command == "End":
    if command.startswith("refill"):

        quantity += int(command.split()[-1])
    else:
        command = int(command)
        if quantity >= command:
            print(f"{queue.popleft()} got water")
            quantity -= command
        else:
            print(f"{queue.popleft()} must wait")

    command = input()

print(f"{quantity} liters left")