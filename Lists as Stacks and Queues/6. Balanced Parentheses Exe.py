parentheses = input()

stack = []
balanced = True

for paren in parentheses:
    if paren in '{([':
        stack.append(paren)
    elif paren in "])}":
        if len(stack) == 0:
            balanced = False
            break
        opening_paren = stack.pop()

        if f'{opening_paren}{paren}' not in ['{}', '[]', '()']:
            balance = False
            break
if balanced and len(stack) == 0:
    print('YES')
else:
    print('NO')