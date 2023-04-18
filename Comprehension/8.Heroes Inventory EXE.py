heroes = input().split(', ')

inventory = {el:{} for el in heroes}

command = input()

while  command != "End":

    name, item, gold = command.split('-')
    gold = int(gold)
    if item not in inventory[name]:
        inventory[name][item] = int(gold)



    command = input()

for hero in heroes:
    cost = sum(inventory[hero].values())
    item_count = len(inventory[name])
    print(f"{hero} -> Items: {item_count}, COST: {cost}")

