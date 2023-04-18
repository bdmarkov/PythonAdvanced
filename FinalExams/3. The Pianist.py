
n = int(input())

dic = {}

for i in range(0, n):

    piece, composer, key = input().split("|")

    dic[piece] = {'composer' : composer, 'key' : key}


command = input()

while not command == "Stop":
    command = command.split("|")

    if "Add" in command:
        piece = command[1]
        composer = command[2]
        key = command[3]

        if piece not in dic:
            dic[piece] = {"composer" : composer, "key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif "Remove" in command:
        piece = command[1]
        if piece in dic:
            dic.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    else:
        piece = command[1]
        key = command[2]
        if piece in dic:
            dic[piece]["key"] = key
            print(f"Changed the key of {piece} to {key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")


    command = input()

for k,v in sorted(dic.items(), key=lambda kvp: (kvp[0], kvp[1]["composer"])):
    print(f"{k} -> Composer: {v['composer']}, Key: {v['key']}")
