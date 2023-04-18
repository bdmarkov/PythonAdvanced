from collections import deque

substring = deque(input().split())

main_colours = {'red', 'yellow', 'blue'}
secondary_colourrs = {'orange', 'purple', 'green'}

collected_colours = []

while substring:
    left = substring.popleft()
    right = substring.pop() if substring else ''
    colour = left + right
    if colour in main_colours or colour in secondary_colourrs:
        collected_colours.append(colour)
        continue
    colour = right + left
    if colour in main_colours or colour in secondary_colourrs:
        collected_colours.append(colour)
    else:
        left = left[:-1]
        right = right[:-1]
        if left:
            substring.insert(len(substring) // 2, left)
        if right:
            substring.insert(len(substring) // 2, right)

secondary_required_colours = {
    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['yellow', 'blue'],
}

for colour in collected_colours:
    if colour in main_colours:
        continue
    required_colours = secondary_required_colours[colour]
    is_valid = all([x in collected_colours for x in required_colours])
    if not is_valid:
        collected_colours.remove(colour)

print(collected_colours)
