a, b, c= input("Enter side: ").split()
try:
    a = int(a)
    b = int(b)
    c = int(c)

    if a + b <= c:
        print("It's not triangle")
    elif a**2 == ((b**2)+(c**2)) or b**2 == ((a**2)+(c**2)) or c**2 == ((b**2)+(a**2)):
        print("It's right triangle")
    elif a == b == c:
        print("It's equilateral triangle")
    elif a == b or a == c or b == c:
        print("It's isosceles triangle")
    else:
        print("It's simple triangle")            
except:
    print("Enter numeric ! ! !")