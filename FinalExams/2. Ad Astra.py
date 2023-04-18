import re

text = input()


pattern = r"(#|\|)(?P<item>[A-Za-z\s]+)\1(?P<date>[\d]{2}/[\d]{2}/[\d]{2})\1(?P<calories>[0-9]{1,4}|10000)\1"

food_data = []
calories = 0
days = 0

matches = re.finditer(pattern, text)

for match in matches:
    object_dict = match.groupdict()
    food_data.append(match)
    calories += int(object_dict['calories'])




days = calories // 2000

print(f"You have food to last you for: {days} days!")

for food in food_data:
    print(f"Item: {food['item']}, Best before: {food['date']}, Nutrition: {food['calories']}")


# print(data)

