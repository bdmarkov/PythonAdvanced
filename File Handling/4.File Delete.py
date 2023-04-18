import os

try:
    os.remove("asd.txt")
except FileNotFoundError:
    print("file does not exist")