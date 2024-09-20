print(' *** String Diamond ***')
input_str = input("Enter string : ")
length = len(input_str)

start = 2 if length % 2 == 0 else 1

for i in range(start, length + 1, 2):
    substring = input_str[(length - i) // 2: (length + i) // 2]
    print(" " * ((length - i) // 2) + substring)
for i in range(length - 2, start - 1, -2):
    substring = input_str[(length - i) // 2: (length + i) // 2]
    print(" " * ((length - i) // 2) + substring)
    
print("===== End of program =====")