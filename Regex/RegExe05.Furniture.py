import re

text = input()

pattern = r">>(?P<furniture>[a-zA-Z]+)<<(?P<price>\d+(\.\d+)?)\!(?P<quantity>\d+)"
sum = 0
furnitures = []

while not text == "Purchase":

    match = re.match(pattern,text)

    if match:
        data = match.groupdict()
        furnitures.append(data["furniture"])
        sum += int(data["quantity"]) * float(data["price"])

    text = input()

print("Bought furniture:")
if furnitures:
    print("\n".join(furnitures))
print(f"Total money spend: {sum:.2f}")
