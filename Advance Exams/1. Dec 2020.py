from collections import  deque

males = [int(el) for el in input().split()]
females = deque([int(el) for el in input().split()])

matches = 0

while females and males:
    male = males.pop()
    female = females.popleft()

    if male <= 0 and female <= 0:
        continue
    if male <= 0:
        females.appendleft(female)
        continue
    if female <= 0:
        males.append(male)
        continue

    if male % 25 == 0 and female % 25 == 0:
        males.pop()
        females.popleft()
        continue
    if male % 25 == 0:
        male = males.pop()
        females.appendleft(female)
        continue
    if female % 25 == 0:
        males.append(male)
        female = females.popleft()
        continue

    if male == female:
        matches += 1
    else:
        males.append(male-2)

print(f"Matches: {matches}")
if males:
    print(f"Males left: {', '.join(reversed([str(el) for el in males]))}")
else:
    print('Males left: none')
if females:
    print(f"Females left: {', '.join([str(el) for el in females])}")
else:
    print('Females left: none')