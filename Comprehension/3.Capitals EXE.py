countries = input().split(', ')
capitals = input().split(', ')

result = zip(countries, capitals)

result_dic = dict(result)

for k, v in result_dic.items():
    print(f"{k} -> {v}")