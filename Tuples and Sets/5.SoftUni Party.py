n = int(input())

a = set()
b = set()

command = input()

while not command == "END":
    if command not in a:
        a.add(command)
    else:
        b.add(command)
    command = input()



a.difference_update(b)
a = list(a)
print(len(a))
for name in sorted(a):
    print(name)
