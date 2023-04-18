sometext = input().split()

count = 0

for c in sometext:
    if ":" in c:
        for i in range(len(c)):
            if c[i] == ":":

                print(f":{c[i+1]}")

