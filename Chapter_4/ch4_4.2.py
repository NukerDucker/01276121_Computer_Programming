print(" *** Linear Formula ***")
x1, y1, x2, y2 = (input("Enter x1 y1 x2 y2: ")).split()
x1 = int(x1)
x2 = int(x2)
y1 = int(y1)
y2 = int(y2)

print(f"({x1},{y1}) ==> ({x2},{y2})")

a = y2-y1
b = x1-x2
c = (x2 * y1) - (x1 * y2)

if x1 == x2:
    print(f"Vertical line ==> x = {x1}.")
    
print(f'f1 ==> {a}x + {b}y + {c} = 0')    

if a < 0:
    a_abs = a*(-1)
if b < 0:
    b_abs = b*(-1)
if c < 0:
    c_abs = c*(-1)
    
if c_abs != 0:
   if (a_abs < b_abs) and (a_abs < c_abs):
       greatest_common_divisor = a_abs
   elif (b_abs < a_abs) and (b_abs < c_abs): 
       greatest_common_divisor = b_abs
   else:
       greatest_common_divisor = c_abs
else:
    if (a < b):
        greatest_common_divisor = a_abs
    else:
        greatest_common_divisor = b_abs
        
while a % greatest_common_divisor != 0 or b % greatest_common_divisor != 0 or c % greatest_common_divisor != 0:
    greatest_common_divisor -= 1
if greatest_common_divisor < 0:
    greatest_common_divisor = -greatest_common_divisor

a2 = a // greatest_common_divisor
b2 = b // greatest_common_divisor
c2 = c // greatest_common_divisor

print(f'f2 ==> {a2}x + {b2}y + {c2} = 0')

if a2 < 0:
    a3 = a2 * -1
    b3 = b2 * -1
    c3 = c2 * -1
else:
    a3 = a2
    b3 = b2
    c3 = c2

if a3 > 1:
    print(f"f3 ==> {a3}x ",end='')
else:
    print(f"f3 ==> x ",end='')

if b3 > 1 :
    print(f"+ {b3}y ",end='')
elif b3 < -1:
    print(f"- {-b3}y ",end='')
elif b3 == -1:
    print(f"- y ",end='')
else:
    print(f"+ y ",end='')

if c3 > 0:
    print(f"+ {c3} ",end='')
elif c3 < 0:
    print(f"- {-c3} ",end='')
else:
    print(f"",end='')
print("= 0")

print("===== End of program =====")