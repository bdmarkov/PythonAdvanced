numbers = input().split(', ')

numbers = [int(el) for el in numbers]

positive = [el for el in numbers if el >= 0]
negative = [el for el in numbers if el < 0]
odd = [el for el in numbers if el % 2 != 0]
even = [el for el in numbers if el % 2 == 0]

print(f'Positive: {", ".join([str(el) for el in positive])}')
print(f'Negative: {", ".join([str(el) for el in negative])}')
print(f'Even: {", ".join([str(el) for el in even])}')
print(f'Odd: {", ".join([str(el) for el in odd])}')