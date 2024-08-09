print(" *** Fibonacci sequence ***")
a0, a1, n = (input("Enter a0 a1 n : ")).split()
a0 = int(a0)
a1 = int(a1)
n = int(n)
a = 1
print(f"{a0}, {a1}, ", end="")
while a <= n-2:
    next_num = a0+a1
    if a < n-2 :
        print(next_num, end=", ")
    else:
        print(next_num, end="")
    a0 = a1
    a1 = next_num
    a += 1
print("\n===== End of program =====")