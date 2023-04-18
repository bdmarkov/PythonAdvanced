somestring = input()

previous_char = ""
newstring = ""
for c in somestring:

    if c != previous_char:
        newstring += c

    previous_char = c


print(newstring)