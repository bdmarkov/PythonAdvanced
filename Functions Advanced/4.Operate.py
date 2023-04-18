from functools import reduce

def operate(operator, *args):

    for i in args:
        if operator == "+":
            return reduce(lambda x,y: x+y, args)
        elif operator == "-":
            return reduce(lambda x, y: x-y, args)
        elif operator == "*":
            return reduce(lambda x,y: x*y, args)
        else:
            return reduce(lambda x,y: x/y, args)



