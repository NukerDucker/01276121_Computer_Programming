print(" *** Butterfly ***")
N = int(input("Input a positive integer : "))
if N > 0:
    print()

    for i in range(1, N + 1):
        print("*" * i, end="")
        print(" " * (N - i) * 2, end="")
        print("*" * i)
        
    for i in range(N - 1, 0, -1):
        print("*" * i, end="")
        print(" " * (N - i) * 2, end="")
        print("*" * i)
        
    print()    
else:
    print("!!!Please enter positive number!!!")    
print("===== End of program =====")    