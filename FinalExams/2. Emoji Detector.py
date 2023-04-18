import re

text = input()

pattern = r'(?P<surr>\:\:|\*\*)(?P<emoji>[A-Z][a-z]{2,}(?P=surr))'
patern_num = r'\d'

all_numbers = re.findall(patern_num, text)

all_numbers = [int(num) for num in all_numbers]

result = 1

for el in all_numbers:
    result *= el

print(f"Cool threshold: {result}")

emoji_count = 0
emojis_to_print = []

for match in re.finditer(pattern, text):
    data = match.groupdict()
    emoji_count += 1
    emoji = data['emoji']
    emoji_coolnes = sum([ord(letter) for letter in emoji])

    if emoji_coolnes >= result:
        emojis_to_print.append(f'{data["surr"]}{data["emoji"]}')

print(f"{emoji_count} emojis found in the text. The cool ones are:")

for emoji in emojis_to_print:
    print(emoji)