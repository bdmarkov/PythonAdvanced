words = input().split()

result = ([el for el in words if len(el) % 2 ==0])

print('\n'.join(result))