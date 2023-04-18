
def shopping_list(budget, **kwargs):

    if budget < 100:
        return "You do not have enough budget."
    ll = []
    count = 0
    for k, v in kwargs.items():
        if count == 5:
            break
        if v[0] * v[1] > budget:
            continue
        else:
            count+= 1
            budget -= (v[0] * v[1])

        ll.append(f"You bought {k} for {v[0] * v[1]:.2f} leva.")

    result = ""
    for i in ll:
        result += i + "\n"
    return result



print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))

