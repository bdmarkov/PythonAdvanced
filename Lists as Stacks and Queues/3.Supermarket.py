from collections import deque

queue = deque()

names = input()

while not names == "End":
    if not names == "Paid":
        queue.append(names)
    else:
        for i in range(len(queue)):
            print(queue.popleft())
    names = input()

print(f"{len(queue)} people remaining.")