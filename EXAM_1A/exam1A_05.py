print(" *** Quadratic solver ***")
print("     ax^2 + bx + c = 0")

a, b, c = (input("Enter a b c : ")).split()
a = float(a)
b = float(b)
c = float(c)

discriminant = float(((b**2)-(4*a*c))**0.5)
    
x1 = ((-b + (discriminant))/(2*a))
x2 = ((-b - (discriminant))/(2*a))

if discriminant > 0 or discriminant < 0:
    if x1 == int(x1):
        print(f"x1: {int(x1)}", end=", ")
    else:
        print(f"x1: {x1:.3f}", end=", ")
        
    if x2 == int(x2):
        print(f"x2: {int(x2)}")
    else:
        print(f"x2: {x2:.3f}")
        
elif discriminant == 0 and x1 == x2:
    if x1 == int(x1):
        print(f"x: {int(x1)}")
    else:
        print(f"x: {x1:.3f}") 
        
print("===== End of program =====")