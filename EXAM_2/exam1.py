print(" *** Fibonacci sequence ***")
a0, a1, n = (input("Enter a0 a1 n : ")).split()
a0, a1, n, fib_str, total = int(a0), int(a1), int(n), f'{a0}+{a1}', 0
for _ in range(n):
    a0, a1 = a1, a0 + a1 
    total = a0 + a1
    fib_str += f'+{a1}'
print(f'{fib_str} = {total}')
print("===== End of program =====")