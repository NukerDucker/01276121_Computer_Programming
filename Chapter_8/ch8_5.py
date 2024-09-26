def num_generator(num_range):
    num_str = ''
    num = 1
    for _ in range(1, num_range + 1):
        if num == 10:
            num = 0
        num_str += f'{num}'
        num += 1
    return num_str

def square_hollow_star(h):
    output = ''
    output += f"{'*' * h}\n"
    for _ in range(h - 2):
        output += f'*{" " * (h - 2)}*\n'
    output += '*' * h
    return output

def square_hollow_num(h):
    output = ''
    num_str = num_generator(h)
    reversed_num = num_str[::-1]
    output += f'{reversed_num}\n'
    for i in range(len(num_str) - 2):
        output += f'{reversed_num[i + 1:i + 2]}{" " * (len(num_str) - 2)}{num_str[i + 1:i + 2]}\n'
    output += num_str
    return output
    
def square_num(h):
    num_str = num_generator(h)
    output = ''
    for i in range(len(num_str)):
        output += f'{num_str[:i] + num_str[i] * (h - i)}'
        if i < len(num_str) - 1:
            output += '\n'
    return output
        
print(' *** Display square ***')

height, type_square = input('Enter Your List : ').split()
height = int(height)

if type_square == '1':
    square_hollow_star(height)
elif type_square == '2':
    square_hollow_num(height)
elif type_square == '3':
    square_num(height)
    
print('===== End of program =====')