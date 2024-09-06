print(" *** Binary to Decimal ***")
UserInput = input("Enter binary number : ")
binary = ''
decimal = 0
for i in UserInput:
    try:
        if i == '$':
            break
        i = int(i)
        if i == 0 or i == 1:
            binary += str(i)
    except ValueError:
        pass        
for digit in binary:
    decimal = decimal*2 + int(digit)
print(f"{binary} ==> {decimal}")    
print("===== End of program ======")