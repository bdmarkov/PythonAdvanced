myinput = input().split()

first = myinput[0]
second = myinput[1]
flag = False
sum = 0
result = 0

for c in range(len(first)):

    sum = ord(first[c]) * ord(second[c])
    result += sum

    if len(first) == c+1:
        for t in range(c + 1 , len(second)):
            result += ord(second[t])
            flag = True


    if len(second) == c+1:
        for y in range(c + 1, len(first)):
            result += ord(first[y])
            flag = True


    if flag:
        break
print(result)