print(" *** Integer type and odd even ***")
num = int(input("Enter any number : "))
if num > 0:
    print(f"{num} is positive.")
elif num == 0:
    print(f"{num} is zero.")
else:
    print(f"{num} is negative.")

if num % 2 == 0 :
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")  