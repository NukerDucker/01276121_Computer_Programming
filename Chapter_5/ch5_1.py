InputStr, InputNum = input("Enter a word and a number: ").split()
num = int(InputNum)

if 1 <= num <= 26:
    upper = ""
    encoded = ""
    for i in InputStr:
        if 'a' <= i <= 'z':
            upper += chr((ord(i) - 32))  
        else:
            upper += i
    
    for a in upper:
        if 'A' <= a <= 'Z':
            shifted = ord(a) + num
            if shifted > ord('Z'):
                shifted -= 26 
            encoded += chr(shifted)        

    print(encoded)
else:
    print("Number must be between 1-26")
