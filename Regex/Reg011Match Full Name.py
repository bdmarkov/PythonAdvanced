import re

text = input()

reg = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"

match = re.findall(reg, text)

print(" ".join(match))