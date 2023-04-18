

n = int(input())

stack = []

for i in range(n):

    command = input().split()

    if command[0] == "1":
        stack.append(command[1])
    elif command[0] == "2":
        stack.pop()
    elif command[0] == "3":
        if stack:
            print(max(stack))
    elif command[0] == "4":
        if stack:
            print(min(stack))


reverse_stack = []

for i in range(len(stack)):
    reverse_stack.append(str(stack.pop()))


print(', '.join(reverse_stack))