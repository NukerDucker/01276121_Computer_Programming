<<<<<<< HEAD
print(" *** Fibonacci sequence ***")
a0, a1, n = (input("Enter a0 a1 n : ")).split()
a0, a1, n, fib_str, total = int(a0), int(a1), int(n), f'{a0}+{a1}', 0
for _ in range(n):
    a0, a1 = a1, a0 + a1 
    total = a0 + a1
    fib_str += f'+{a1}'
print(f'{fib_str} = {total}')
=======
print(" *** Fibonacci sequence ***")
a0, a1, n = (input("Enter a0 a1 n : ")).split()
a0, a1, n, fib_str, total = int(a0), int(a1), int(n), f'{a0}+{a1}', 0
for _ in range(n):
    a0, a1 = a1, a0 + a1 
    total = a0 + a1
    fib_str += f'+{a1}'
print(f'{fib_str} = {total}')
>>>>>>> c492593d5974ed1e1ded5aa5d364a9ec2caedce1
print("===== End of program =====")