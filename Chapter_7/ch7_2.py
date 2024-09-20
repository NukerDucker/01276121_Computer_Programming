print(' *** Remove ODD characters ***')
str_input = input('Enter a string : ')
output = f''
for i in range(len(str_input)):
    output += str_input[i] if i % 2 == 1 else ''
print('Even characters =', output)
print('===== End of program =====')