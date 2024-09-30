def myNum(b):
    b = int(b)
    return b

def mySum(a,b):
    a, b = int(a), int(b)
    total = a + b
    return total

print(" *** My sum ***")
a,b = input("Enter a b : ").split()
print(f"{a} + {b} => {a} + {myNum(b)} = {mySum(a,b)}")
print("===== End of program =====")