


dic = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}

flag = False

while True:

    command = input().split()

    for i in range(0, len(command), 2):
        num = int(command[i])
        name = command[i+1].lower()


        if name in dic:
            dic[name] += num
        else:
            if name not in junk:
                junk[name] = num
            else:
                junk[name] += num


        if "fragments" in dic:
            if dic["fragments"] >= 250:
                print("Valanyr obtained!")
                dic["fragments"] -= 250
                flag = True
                break
        if "shards" in dic:
            if dic["shards"] >= 250:
                print("Shadowmourne obtained!")
                dic["shards"] -= 250
                flag = True
                break
        if "motes" in dic:

            if dic["motes"] >= 250:
                print("Dragonwrath obtained!")
                dic["motes"] -= 250
                flag = True
                break

    if flag:
        break

for k, v in sorted(dic.items(), key=lambda kvp: (-kvp[1], kvp[0])):
    print(f"{k}: {v}")

for k, v in sorted(junk.items(), key=lambda kvp: kvp[0]):
    print(f"{k}: {v}")