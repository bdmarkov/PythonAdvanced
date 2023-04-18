def age_assignment(*args, **kwargs):
    mydic = {}
    for i in args:
        if i[0] in kwargs:
            mydic[i] = kwargs[i[0]]

    return mydic


print(age_assignment("Peter", "George", G=26, P=19))