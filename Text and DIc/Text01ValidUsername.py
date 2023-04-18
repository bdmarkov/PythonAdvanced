pas = input().split(", ")
falg = True
for p in pas:
    flag = True
    for c in p:
        if c.isalnum() or c == "-" or c == "_":
            pass

        else:
            flag = False



    if 2 < len(p) < 17:
        if not p.endswith(" ") and not p.startswith(" "):
            if flag == True:

                print(p)



