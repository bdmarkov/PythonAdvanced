somestring = input()

newstr = ""
finalstring = ""
count = ""
countstr = 0

finalstring_to_set = []


index = 0

while index < len(somestring):
    if not somestring[index].isdigit():
        newstr += somestring[index].upper()
        index += 1

    else:
        while somestring[index].isdigit():
            count += somestring[index]
            index+=1
            if index == len(somestring):
                break

        countstr = int(count)
        finalstring += (newstr * countstr)

        newstr = ""
        count = ""



for i in finalstring:
    finalstring_to_set.append(i)


finalstring_to_set = set(finalstring_to_set)
countstr = len(set(finalstring_to_set))

print(f"Unique symbols used: {countstr}")
print(finalstring)