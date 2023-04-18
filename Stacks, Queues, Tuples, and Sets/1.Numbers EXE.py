
first_seq = {int(el) for el in input().split()}
second_seq = {int(el) for el in input().split()}

n = int(input())

for i in range(n):
    command = input()
    if command.startswith("Add"):
        command = command.split()
        if command[1] == 'First':
            nums = [int(el) for el in command[2:]]
            for i in nums:
                first_seq.add(i)
        else:
            nums = [int(el) for el in command[2:]]
            for i in nums:
                second_seq.add(i)
    elif command.startswith("Remove"):
        command = command.split()
        if command[1] == 'First':
            nums = [int(el) for el in command[2:]]
            for i in nums:
                if i in first_seq:
                    first_seq.remove(i)
        else:
            nums = [int(el) for el in command[2:]]
            for i in nums:
                if i in second_seq:
                    second_seq.remove(i)
    else:
        if first_seq.issubset(second_seq) or second_seq.issubset(first_seq):
            print('True')
        else:
            print('False')

first_seq = [str(el) for el in sorted(first_seq)]
second_seq = [str(el) for el in sorted(second_seq)]

print(', '.join(first_seq))
print(', '.join(second_seq))