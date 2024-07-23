print(" *** 3-digit number ***")
num = int(input("Enter 3-digit number : "))

a = num//100
b = num//10%10
c = num%10

print(f"{num} => ", end='')

if a % 2 == 0:
    print("Even ", end='')
else:
    print("Odd ", end='')
if b % 2 == 0:
    print("Even ", end='')
else:
    print("Odd ", end='') 
if c % 2 == 0:
    print("Even ")
else:
    print("Odd ")
    
print(f"{a}^2 + {b}^3 + {c}^4 = {((a**2)+(b**3)+(c**4)):,}")
print(f"===== End of program =====")