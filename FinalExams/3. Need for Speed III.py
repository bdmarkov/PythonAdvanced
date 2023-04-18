
n = int(input())

dic = {}

for i in range(0, n):
    command = input().split("|")
    car = command[0]
    mileage = int(command[1])
    fuel = int(command[2])
    dic[car] = {"mileage": mileage,"fuel": fuel}

command = input()

while not command == "Stop":
    command = command.split(" : ")
    event = command[0]
    car = command[1]

    if event == "Drive":
        distance = int(command[2])
        fuel = int(command[3])
        if fuel > dic[car]["fuel"]:
            print(f"Not enough fuel to make that ride")
        else:
            dic[car]["mileage"] += distance
            dic[car]["fuel"] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if dic[car]["mileage"] > 100000:
            print(f"Time to sell the {car}!")
            dic.pop(car)
    elif event == "Refuel":
        fuel = int(command[2])
        if dic[car]["fuel"] + fuel > 75:
            print(f"{car} refueled with {75-dic[car]['fuel']} liters")
            dic[car]["fuel"] = 75
        else:
            print(f"{car} refueled with {fuel} liters")
            dic[car]["fuel"] += fuel
    else:
        kilometers = int(command[2])
        if dic[car]["mileage"] - kilometers < 10000:
            dic[car]["mileage"] = 10000
        else:
            dic[car]["mileage"] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")

    command = input()

for k, v in sorted(dic.items(), key=lambda kvp: (-kvp[1]['mileage'], kvp[0])):
    print(f"{k} -> Mileage: {v['mileage']} kms, Fuel in the tank: {v['fuel']} lt.")