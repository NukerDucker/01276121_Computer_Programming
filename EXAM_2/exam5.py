print(" *** Spiral Rectangle ***")
side, directions = input("Enter side height: ").split()
side = int(side)

matrix = [[0] * side for _ in range(side)]

if directions == 'up':
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    row, col = 0, 0
elif directions == 'down':
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    row, col = side - 1, side - 1
elif directions == 'left':
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    row, col = 0, 0
elif directions == 'right':
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    row, col = 0, side - 1

current_direction = 0

for num in range(side * side, 0, -1):
    matrix[row][col] = num

    next_row = row + directions[current_direction][0]
    next_col = col + directions[current_direction][1]
    
    if not (0 <= next_row < side and 0 <= next_col < side and matrix[next_row][next_col] == 0):
        current_direction = (current_direction + 1) % 4
        next_row = row + directions[current_direction][0]
        next_col = col + directions[current_direction][1]

    row, col = next_row, next_col

for row in matrix:
    for num in row:
        print(f"{num:>2}", end=" ")
    print()
print("===== End of program ======")