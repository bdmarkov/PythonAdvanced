
password = input()

command = input()
newpass = ""
while not command == "Done":
    command = command.split()

    if command[0] == "TakeOdd":
        for i in range(1, len(password), 2):
            newpass += password[i]
        password = newpass
        newpass = ""
        print(password)
    elif command[0] == "Cut":
        index = int(command[1])
        lenght = int(command[2])
        password = password[:index] + password[index + lenght::]
        print(password)
    else:
        substring = command[1]
        substitute = command[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

    command = input()

print(f"Your password is: {password}")