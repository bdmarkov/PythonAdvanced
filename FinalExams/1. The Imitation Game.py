message = input()

command = input()

while not command == "Decode":
    command = command.split("|")
    action = command[0]

    if action == "Move":
        number_of_letters = int(command[1])
        firsthalf = message[:number_of_letters]
        secondhalf = message[number_of_letters::]
        message = secondhalf + firsthalf

    elif action == "Insert":
        index = int(command[1])
        value = command[2]
        message = message[:index] + value + message[index::]

    else:
        substring = command[1]
        replacement = command[2]
        message = message.replace(substring, replacement)


    command = input()


print(f"The decrypted message is: {message}")