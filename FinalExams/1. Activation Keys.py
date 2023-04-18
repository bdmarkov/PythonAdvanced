
mykey = input()

command = input()

while not command == "Generate":
    commandsplit = command.split(">>>")
    if "Contains" in command:
        substring = commandsplit[1]
        if substring in mykey:
            print(f"{mykey} contains {substring}")
        else:
            print(f"Substring not found!")
    elif "Flip" in command:
        upper_or_lower = commandsplit[1]
        start = int(commandsplit[2])
        end = int(commandsplit[3])
        if upper_or_lower == "Upper":

            mykey = mykey[:start] + mykey.upper()[start:end] + mykey[end::]
        else:
            mykey = mykey[:start] + mykey.lower()[start:end] + mykey[end::]


        print(mykey)

    else:
        start = int(commandsplit[1])
        end = int(commandsplit[2])
        firsthalf = mykey[0:start]
        secondhalf = mykey[end::]

        mykey = firsthalf + secondhalf
        print(mykey)

    command = input()

print(f"Your activation key is: {mykey}")