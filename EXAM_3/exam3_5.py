def print_mountain_section(height: int, mountain_height: int, row: int) -> None:
    if row < height:
        left_dots = row
        inner_dots = (height - row - 1) * 2
        print('.' * left_dots + '/' + '.' * inner_dots + '\\' + '.' * left_dots, end='')
    else:
        print('.' * (height * 2), end='')

def draw_mountains(heights: list[int]) -> None:
    max_height = max(heights)
    digits = len(str(max_height))

    for i in range(max_height - 1, -1, -1):
        row = max_height - i
        print(f'{row:0>{digits + 1}d}', end='')
        print(' | ', end='')
        
        for height in heights:
            print_mountain_section(height, max_height, i)
            print(' | ', end='')
        print()

print(" *** Mountains ***")
heights_input: str = input("Enter mountain heights (e.g., 6 3 7): ")
heights = [int(h) for h in heights_input.split()]

dot = '.'
left = '/'
right = '\\'

draw_mountains(heights)

print("===== End of program =====")