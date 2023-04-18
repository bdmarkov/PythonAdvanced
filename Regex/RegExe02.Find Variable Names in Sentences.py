import re

text = input()

pattern = r"(^_|(?<=\s_))[A-Za-z0-9]+\b"

valid_matches = [obj.group() for obj in re.finditer(pattern, text)]

print(*valid_matches, sep=",")