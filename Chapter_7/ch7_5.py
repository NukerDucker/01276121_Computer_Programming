print(' *** Center-starting Spiral Rectangle ***')
user_input = input('Enter side direction: ').split()
side, direction = int(user_input[0]), user_input[1]

if len(user_input) == 3:
    start_num = user_input[2]

matrix = [[0] * side for _ in range(side)]

row, col = (side // 2, side // 2) if side % 2 != 0 else (side // 2 - 1, side // 2 - 1)

if direction == 'up':
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up -> right -> down -> left
elif direction == 'down':
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]  # down -> left -> up -> right
elif direction == 'left':
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]  # left -> up -> right -> down
elif direction == 'right':
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right -> down -> left -> up

current_direction = 0
num = int(start_num) if start_num else 1
step_size = 1 
total_steps = 0  
steps_in_current_direction = 0 
count = 1

while count <= side * side:
    matrix[row][col] = num 
    num += 1
    count += 1
    steps_in_current_direction += 1

    row += directions[current_direction][0]
    col += directions[current_direction][1]
    
    if steps_in_current_direction == step_size:
        current_direction = (current_direction + 1) % 4
        steps_in_current_direction = 0 
        total_steps += 1
        step_size += 1 if total_steps % 2 == 0 else 0


max_digits = len(str(side**2))

for row in matrix:
    for num in row:
        print(f"{num:>{max_digits}}", end=" ")
    print()

print('===== End of program ======')