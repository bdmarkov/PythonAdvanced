
concealed_mesage = input()

command = input()

while not command == "Reveal":
    command = command.split(":|:")
    insttruction = command[0]

    if insttruction == "InsertSpace":
        index = int(command[1])
        concealed_mesage = concealed_mesage[:index] + " " + concealed_mesage[index::]
        print(concealed_mesage)
    elif insttruction == "Reverse":
        substring = command[1]
        if substring in concealed_mesage:
            concealed_mesage = concealed_mesage.replace(substring, "", 1)
            concealed_mesage = concealed_mesage + substring[::-1]
            print(concealed_mesage)
        else:
            print("error")
    else:
        substr = command[1]
        replacement = command[2]
        concealed_mesage = concealed_mesage.replace(substr, replacement)
        print(concealed_mesage)

    command = input()

print(f"You have a new text message: {concealed_mesage}")