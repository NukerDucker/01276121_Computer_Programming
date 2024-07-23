a, b, c = (input(" *** Min Max Avg ***\nEnter Number : ")).split()
a = int(a)
b = int(b)
c = int(c)
if a > b:
    a,b = b,a
if a > c:
    a,c = c,a
if b > c:
    b,c = c,b
print(f"min, mid, max ==> {a:.1f} {b:.1f} {c:.1f}")
print(f"Average ==> {((a+b+c)/3):.2f}")