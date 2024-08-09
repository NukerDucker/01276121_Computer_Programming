print(" *** Factorial ***")
fac = int(input("Enter an integer(n) : "))

a = 1
sum = 1
print(f"Fac({fac}) => " , end="")
while a <= fac:
    if a == fac:
        print(f"{a:,}",end="")
    else:
        print(f"{a:,}*", end="")
    sum *= a
    a += 1
print(f" = {sum:,}")
print("===== End of program =====")