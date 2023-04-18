

command = input()

dic = {}

while not command == "Sail":
    command = command.split("||")
    town = command[0]
    killed = int(command[1])
    gold = int(command[2])

    if not town in dic:
        dic[town] = {"killed": killed, "gold": gold}
    else:
        dic[town]['killed'] += killed
        dic[town]['gold'] += gold


    command = input()

command = input()

while not command == "End":
    command = command.split("=>")
    event = command[0]
    town = command[1]


    if event == "Plunder":

        killed = int(command[2])
        gold = int(command[3])

        dic[town]["killed"] -= killed
        dic[town]["gold"] -= gold
        print(f"{town} plundered! {gold} gold stolen, {killed} citizens killed.")

        if dic[town]["killed"] == 0 or dic[town]["gold"] == 0:
            print(f"{town} has been wiped off the map!")
            dic.pop(town)


    else:

        gold = int(command[2])

        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            dic[town]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {dic[town]['gold']} gold.")


    command = input()

print(f"Ahoy, Captain! There are {len(dic)} wealthy settlements to go to:")

for k, v in sorted(dic.items(), key=lambda kvp: (-kvp[1]['gold'], kvp[0])):
    print(f"{k} -> Population: {v['killed']} citizens, Gold: {v['gold']} kg")