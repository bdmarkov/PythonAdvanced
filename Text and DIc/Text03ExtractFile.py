path = input().split("\\")

file = ""

for word in path:
    if "." in word:
        file = word

splitfile = file.split(".")

print(f"File name: {splitfile[0]}")
print(f"File extension: {splitfile[1]}")