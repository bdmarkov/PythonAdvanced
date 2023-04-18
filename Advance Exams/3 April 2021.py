def flights(*args):
    f = [el for el in args]

    myflights = {}

    for i in range(len(f)):
        if f[i] == "Finish":
            return myflights
        if i % 2 == 0:
            if not f[i] in myflights:
                myflights[f[i]] = 0
        else:
            myflights[f[i-1]] += f[i]


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))