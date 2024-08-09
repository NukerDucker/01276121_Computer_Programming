print(" *** Pyramid-V ***")
height = int(input("Enter height : "))

for i in range(height):
    print(' ' * (height - i - 1), end='')
    print('/', end='')
    if i == height - 1:
        print('_' * (2 * i), end='')
    else:
        print('.' * (2 * i), end='')
    print('\\')

print("===== End of program =====")
