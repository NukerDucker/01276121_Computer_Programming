print(' *** Find divisible number ***')

num, divisor = input('Enter num divisor : ').split()
divisor = int(divisor)
possible_divisible = []

for x_value in range(0, 10):
    for y_value in range(0, 10):
        possible_num = num.replace('x', f'{x_value}').replace('y', f'{y_value}')
        possible_divisible.append(int(possible_num))

divisible = [nums for nums in possible_divisible if nums % divisor == 0]
print(divisible)
print('===== End of program ======')