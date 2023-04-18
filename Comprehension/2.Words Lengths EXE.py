words = input().split(', ')

result = [f'{el} -> {len(el)}' for el in words]

print(", ".join(result))