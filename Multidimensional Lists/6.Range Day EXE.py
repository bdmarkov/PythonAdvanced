def is_outside(row, col, size):
    if row < 0 or col < 0 or row >= size or col >= size:
        return True
    return False

def get_next_position(direcion, r, c, steps):
    if direcion == 'up':
        return r - steps, c
    if direcion == 'down':
        return r + steps, c
    if direcion == 'left':
        return r, c -steps
    return r, c + steps



matrix = []
size = 5
player_row, player_col = 0, 0

target_count = 0

for row in range(size):
    elements = input().split()
    matrix.append(elements)
    for col in range(size):
        element = elements[col]
        if element == 'A':
            player_row, player_col = row, col
        elif element == 'x':
            target_count += 1

n = int(input())
hit_targets = []

for _ in range(n):
    line_args = input().split()
    command = line_args[0]
    direction = line_args[1]

    if command == 'move':
        steps = int(line_args[2])
        next_player_row, next_player_col = get_next_position(direction, player_row, player_col, steps)

        if is_outside(next_player_row, next_player_col, size):
            continue
        if matrix[next_player_row][next_player_col] != '.':
            continue

        matrix[player_row][player_col] = '.'
        matrix[next_player_row][next_player_col] = 'A'
        player_row, player_col = next_player_row, next_player_col
    else:
        bullet_row,bullet_col = get_next_position(direction, player_row, player_col, 1)
        while True:
            if is_outside(bullet_row, bullet_col, size):
                break
            if matrix[bullet_row][bullet_col] == 'x':
                hit_targets.append([bullet_row, bullet_col])
                matrix[bullet_row][bullet_col] = '.'
                break

            bullet_row, bullet_col = get_next_position(direction,bullet_row, bullet_col, 1)
        if len(hit_targets) == target_count:
            break

if len(hit_targets) == target_count:
    print(f"Training completed! All {target_count} targets hit.")
else:
    print(f'Training not completed! {target_count - len(hit_targets)} targets left.')

for target in hit_targets:
    print(target)