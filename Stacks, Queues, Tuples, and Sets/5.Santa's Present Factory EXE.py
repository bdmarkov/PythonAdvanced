from collections import deque

materials = [int(el) for el in input().split()]
magic_level = deque([int(el) for el in input().split()])

presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

presents_count = {}

while materials and magic_level:
    material = materials.pop()
    magic = magic_level.popleft()

    total_magic = material * magic

    if material == 0 and magic == 0:
        continue
    if material == 0:
        magic_level.appendleft(magic)
        continue
    if magic == 0:
        materials.append(material)
        continue

    if total_magic < 0:
        materials.append(material + magic)

    elif total_magic in presents:
        current_present = presents[total_magic]
        if current_present in presents:
            presents_count[current_present] += 1
        else:
            presents_count[current_present] = 1

    else:
        materials.append(material + 15)

is_done = ("Doll" in presents_count and "Wooden train" in presents_count) or (
            "Bicycle" in presents_count and "Teddy bear" in presents_count)

if is_done:
    print(f'The presents are crafted! Merry Christmas!')
else:
    print(f'No presents this Christmas!')

if materials:
    print(f'Materials left: {", ".join(reversed([str(el) for el in materials]))}')
if magic_level:
    print(f'Magic left: {", ".join([str(el) for el in magic_level])}')

for k, v in sorted(presents_count.items()):
    print(f'{k}: {v}')
