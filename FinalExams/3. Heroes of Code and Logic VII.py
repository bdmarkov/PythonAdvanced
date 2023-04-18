
n = int(input())

dic = {}

for i in range(0, n):

    heroes = input()
    name, hp, mp = heroes.split()
    hp = int(hp)
    mp = int(mp)

    dic[name] = {"hp": hp, "mp": mp}


command = input()

while not command == "End":
    command = command.split(' - ')
    action = command[0]
    if action == "CastSpell":
        heroname = command[1]
        mpneeded = int(command[2])
        spellname = command[3]
        if dic[heroname]["mp"] >= mpneeded:
            dic[heroname]["mp"] -= mpneeded
            print(f"{heroname} has successfully cast {spellname} and now has {dic[heroname]['mp']} MP!")
        else:
            print(f"{heroname} does not have enough MP to cast {spellname}!")
    elif action == "TakeDamage":
        heroname = command[1]
        damage = int(command[2])
        attacker = command[3]
        if dic[heroname]["hp"] <= damage:
            print(f"{heroname} has been killed by {attacker}!")
            dic.pop(heroname)
        else:
            dic[heroname]["hp"] -= damage
            print(f"{heroname} was hit for {damage} HP by {attacker} and now has {dic[heroname]['hp']} HP left!")

    elif action == "Recharge":
        heroname = command[1]
        amount = int(command[2])


        if dic[heroname]["mp"] + amount > 200:
            print(f"{heroname} recharged for {200 - (dic[heroname]['mp'])} MP!")
            dic[heroname]["mp"] = 200

        else:
            print(f"{heroname} recharged for {amount} MP!")
            dic[heroname]["mp"] += amount
    else:
        heroname = command[1]
        amount = int(command[2])


        if dic[heroname]["hp"] + amount > 100:
            print(f"{heroname} healed for {100 - dic[heroname]['hp']} HP!")
            dic[heroname]["hp"] = 100
        else:
            print(f"{heroname} healed for {amount} HP!")
            dic[heroname]["hp"] += amount
    command = input()

for k, v in sorted(dic.items(), key=lambda kvp: (-kvp[1]['hp'], kvp[0])):
    print(f"{k}")
    print(f"  HP: {v['hp']}")
    print(f"  MP: {v['mp']}")
