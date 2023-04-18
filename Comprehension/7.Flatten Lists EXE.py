sequence = input().split('|')

numbers = [[el for el in seq.split()]  for seq in sequence]


numbers.reverse()

numbers = [num for sequence in numbers for num in sequence]

print(' '.join([str(el) for el in numbers]))