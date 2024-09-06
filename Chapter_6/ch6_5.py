print(" *** Rectangle down-left-up-left ***")
width, height = [int(i) for i in input("Enter width height : ").split()]

matrix = [[0] * width for _ in range(height)]
row, col = 0, width - 1

directions = [(1, 0), (0, -1), (-1, 0), (0, -1)]
current_direction = 0

for num in range(1, width * height + 1):
    matrix[row][col] = num

    next_row = row + directions[current_direction][0]
    next_col = col
    
    if not (0 <= next_row < height and 0 <= next_col < width and matrix[next_row][next_col] == 0):
        current_direction = (current_direction + 1) % 4
        next_row = row + directions[current_direction][0]
        next_col = col + directions[current_direction][1]

    row, col = next_row, next_col

for r in range(height):
    for c in range(width):
        print(f" {matrix[r][c]:>2}", end="")
    print()

print("===== End of program =====")
