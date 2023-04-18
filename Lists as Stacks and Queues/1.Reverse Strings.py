word = list(input())
steck = []

while word:
    steck.append(word.pop())

print(''.join(steck))