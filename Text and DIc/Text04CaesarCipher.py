sometext = input()

newtext = ""
newchar = ""
num = 0
for c in sometext:
    num = ord(c) + 3
    newchar = chr(num)
    newtext += newchar



print(newtext)