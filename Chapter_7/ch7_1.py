print(' *** Adding number ***')
str_list = input('Enter your words : ').split()
output = f''
for i in range(len(str_list)):
    if output:
        output += ' '
    output += f'{(str_list[i])[::-1]}{i+1}' if not i % 2 == 0 else f'{(str_list[i])}{i+1}'
print(output)
print('==== End of program =====')