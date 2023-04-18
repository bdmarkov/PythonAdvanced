import re

text = input()

pattern = r"(#|@)[A-Za-z][A-Za-z][A-Za-z]+\1\1[A-Za-z][A-Za-z][A-Za-z]+\1"

valid_words = [el.group() for el in re.finditer(pattern, text)]

backwards_words = [el for el in valid_words if el[::] == el[::-1]]





valid = []

if valid_words:
    print(f"{len(valid_words)} word pairs found!")
    if backwards_words:
        print("The mirror words are:")
        for i in backwards_words:
            if "#" in i:
                word = i.replace("#", "")
            else:
                word = i.replace("@", "")
            length = int(len(word) / 2)
            valid.append(f"{word[:length]} <=> {word[length:]}")

        print(*valid, sep=", ")
    else:

        print("No mirror words!")
else:
    print("No word pairs found!")
    print("No mirror words!")