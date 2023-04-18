command = input()

phonebook = {}

while not command.isdigit():
    name, num = command.split('-')

    phonebook[name] = num
    command = input()


for i in range(int(command)):
    contact = input()

    if contact not in phonebook:
        print(f"Contact {contact} does not exist.")
    else:
        print(f"{contact} -> {phonebook[contact]}")