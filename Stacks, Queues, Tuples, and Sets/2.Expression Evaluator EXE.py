def operator(operator, num1, num2):
    if operator == '/':
        return num1 // num2
    if operator == '*':
        return num1 * num2
    if operator == '-':
        return num1 - num2
    if operator == '+':
        return num1 + num2


sequence = input().split()

stack = []

operators = "+-*/"

for i in sequence:

    if i in operators:
        while True:
            num = operator(i, stack[0], stack[1])
            stack.pop(0)
            stack.pop(0)
            stack.insert(0, num)
            if len(stack) == 1:
                num = 0
                break
    else:
        stack.append(int(i))


print(*stack)