

def first_half(n):
    if n == 1:
        print('*')
    else:
        for i in range(n):
            print(' ' * (n - i), end='')
            print('* ' * i)


def second_half(n):
    print('* ' * n)
    for i in range(n-1,-1,-1 ):
        print(' ' * (n - i), end='')
        print('* ' * i)

n = int(input())

first_half(n)
second_half(n)