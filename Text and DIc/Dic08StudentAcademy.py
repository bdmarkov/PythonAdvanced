num = int(input())


dic = {}

for i in range(num):
    name = input()
    score = float(input())


    if name not in dic:
        dic[name] = [score]

    else:
        dic[name] += [score]




filter = {}

for k,v in dic.items():
    v = sum(v) / len(v)
    if v >= 4.5:
        filter[k] = v



for k,v in sorted(filter.items(), key=lambda kvp: kvp[1], reverse=True):
    print(f"{k} -> {v:.2f}")
