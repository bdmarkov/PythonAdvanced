import re

phone_numbers = input()

pattern = r"\+359( |-)2\1\d{3}\1\d{4}\b"

match = [obj.group() for obj in re.finditer(pattern, phone_numbers)]

print(", ".join(match))