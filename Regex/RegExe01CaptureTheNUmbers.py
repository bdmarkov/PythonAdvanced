import re
text = input()

pattern = r"\d+"

matchlist = []
while text:


    match = re.findall(pattern, text)
    matchlist.extend(match)
    text = input()



for m in matchlist:
    print(m, end=" ")