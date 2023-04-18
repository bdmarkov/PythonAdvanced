

command = input()

dic = {}

while True:
    if command == "end":
        break

    course, name = command.split(" : ")

    if course not in dic:
        dic[course] = [name]
    else:
        dic[course] += [name]

    command = input()



result = sorted(dic)

for key, value in sorted(dic.items(), key=lambda kvp: (len(kvp[1])), reverse=True):
    print(f"{key}: {len(value)}")
    value = sorted(value)
    for i in range(len(value)):
        print(f"-- {value[i]}")
