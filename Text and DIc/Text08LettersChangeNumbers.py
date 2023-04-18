

somestring = input().split()

sumnumber = 0

sum_of_all_numbers = 0
for i in somestring:
    firstletter = i[0]
    number = int(i[1:-1])
    lastletter = i[-1]



    sumnumber = 0

    if firstletter.isupper():
        firstletter = int(ord(firstletter)) - 64
        sumnumber = number / firstletter
    elif firstletter.islower():
        firstletter = int(ord(firstletter)) - 96
        sumnumber = number * firstletter

    if lastletter.isupper():
        lastletter = int(ord(lastletter)) - 64
        sumnumber = sumnumber - lastletter
    elif lastletter.islower():
        lastletter = int(ord(lastletter)) - 96
        sumnumber = sumnumber + lastletter

    sum_of_all_numbers += sumnumber

print(f"{sum_of_all_numbers:.2f}")