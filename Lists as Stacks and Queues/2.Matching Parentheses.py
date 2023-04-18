expression = input()
stack = []
for i in range(len(expression)):
    if expression[i] == '(':
        stack.append(i)
    elif expression[i] == ')':
        index = int(stack[-1])
        print(expression[index:i+1])
        stack.pop()