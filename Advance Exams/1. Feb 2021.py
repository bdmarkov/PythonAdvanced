from collections import deque

firework = deque([int(el) for el in input().split(', ')])
explosive = [int(el) for el in input().split(', ')]


sum_values = 0

firework_effect = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0
}
flag = False
while firework and explosive:
    fire = firework.popleft()
    power = explosive.pop()

    if fire <= 0 and power <= 0:
        continue
    if fire <= 0:
        explosive.append(power)
        continue
    if power <= 0:
        firework.appendleft(fire)
        continue

    sum_values = fire + power



    if sum_values % 3 == 0 and not sum_values % 5 == 0:
        firework_effect["Palm Fireworks"] += 1

    elif sum_values % 5 == 0 and not sum_values % 3 == 0:
        firework_effect["Willow Fireworks"] += 1

    elif sum_values % 5 == 0 and sum_values % 3 == 0:
        firework_effect["Crossette Fireworks"] += 1

    else:
        fire -= 1
        firework.append(fire)
        explosive.append(power)

    if firework_effect["Palm Fireworks"] >= 3 and firework_effect["Willow Fireworks"] >= 3 and \
            firework_effect["Crossette Fireworks"] >= 3:
        print(f'Congrats! You made the perfect firework show!')
        flag = True
        break

if not flag:
    print("Sorry. You can't make the perfect firework show.")
if firework:
    print(f"Firework Effects left: {', '.join([str(el) for el in firework])}")
if explosive:
    print(f"Explosive Power left: {', '.join([str(el) for el in explosive])}")
for k, v in firework_effect.items():
    print(f"{k}: {v}")