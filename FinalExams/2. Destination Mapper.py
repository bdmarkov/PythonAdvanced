import re

text = input()

pattern = r"(?<=(/|\=))[A-Z][a-zA-Z][a-zA-Z]+(?=\1)"

valid_destinations = [el.group() for el in re.finditer(pattern, text)]
travel_points = sum([len(el) for el in valid_destinations])

print(f"Destinations: {', '.join(valid_destinations)}")
print(f"Travel Points: {travel_points}")