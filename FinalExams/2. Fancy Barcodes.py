import re

pattern = r"[@][#]+[A-Z][A-Za-z0-9][A-Za-z0-9][A-Za-z0-9][A-Za-z0-9]+[A-Z][@][#]+"

digit = r"[0-9]+"

n = int(input())

for i in range(n):
    text = input()
    match = re.match(pattern, text)
    if match:
        d = re.findall(digit, text)
        if d:
            print(f"Product group: {''.join(d)}")
        else:
            print(f"Product group: 00")
    else:
        print("Invalid barcode")