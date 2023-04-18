from collections import deque

def check_presents(amount):
    if 100 <= amount <= 199:
        presents["Gemstone"] += 1
        return
    elif 200 <= amount <= 299:
        presents["Porcelain Sculpture"] += 1
        return
    elif 300 <= amount <= 399:
        presents["Gold"] += 1
        return
    elif 400 <= amount <= 499:
        presents["Diamond Jewellery"] += 1
        return


materials = [int(el) for el in input().split()]
magic_level = deque([int(el) for el in input().split()])


presents = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0,
}




while materials and magic_level:
    mat = materials.pop()
    ml = magic_level.popleft()

    amount = mat + ml

    if 100 <= amount <= 499:
        check_presents(amount)


    elif amount < 100:
        if amount % 2 == 0:
            mat *= 2
            ml *= 3
            new_sum = mat + ml
            check_presents(new_sum)
        else:
            amount *= 2
            check_presents(amount)

    elif amount > 499:
        amount /= 2
        check_presents(amount)


if (presents["Gemstone"] > 0 and presents["Porcelain Sculpture"] > 0) or (presents["Gold"] > 0 and presents["Diamond Jewellery"] > 0):
    print(f"The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print("Materials left: ", end='')
    print(', '.join([str(el) for el in materials]))
if magic_level:
    print("Magic left: ", end='')
    print(', '.join([str(el) for el in magic_level]))

for k, v in sorted(presents.items()):
    if v > 0:
        print(f'{k}: {v}')