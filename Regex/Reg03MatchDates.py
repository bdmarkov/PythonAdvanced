import re

phone_numbers = input()

pattern = r"\b(?P<Day>\d{2})(?P<separator>(/|.|-))(?P<Month>[A-Z][a-z]{2})(?P=separator)(?P<Year>\d{4})\b"

match = [obj.groupdict() for obj in re.finditer(pattern, phone_numbers)]

print('\n'.join([f"Day: {data['Day']}, Month: {data['Month']}, Year: {data['Year']}" for data in match]))
