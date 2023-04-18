import  re

file = open("input.txt")

for idx, line in enumerate(file.readlines()):
    if idx % 2 != 0:
        continue

    line = re.sub(r'[-,\.!?]', '@', line)
    line = ' '.join(reversed(line.split()))

    print(line.strip())

file.close()