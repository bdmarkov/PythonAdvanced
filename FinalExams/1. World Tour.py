
mystops = input()

command = input()

while not command == "Travel":
    command = command.split(":")
    action = command[0]

    if "Add" in action:
        index = int(command[1])
        string = command[2]
        if len(mystops) > index and index >= 0:
            mystops = mystops[:index] + string + mystops[index::]
        print(mystops)
    elif "Remove" in action:
        startindex = int(command[1])
        endindex = int(command[2])
        if startindex in range(len(mystops)) and endindex in range(len(mystops)):
            mystops = mystops[:startindex] + mystops[endindex + 1::]
        print(mystops)
    else:
        oldstring = command[1]
        newstring = command[2]

        mystops = mystops.replace(oldstring, newstring)
        print(mystops)


    command = input()

print(f"Ready for world tour! Planned stops: {mystops}")