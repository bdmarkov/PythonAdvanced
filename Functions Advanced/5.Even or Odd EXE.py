def is_even(num):
    return num % 2 == 0

def is_odd(num):
    return num % 2 != 0

def even_odd(*args):
    command = args[-1]
    print(command)
    numbers = args[:-1]

    if command == "even":
        return list(filter(is_even, numbers))
    else:
        return list(filter(is_odd, numbers))


print(even_odd(1, 2, 3, 4, 5, 6, "even"))