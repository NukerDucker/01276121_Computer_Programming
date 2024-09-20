<<<<<<< HEAD
r, N = input('Enter r N : ').split()
r, N, total_str, total = int(r), int(N), '', 0
for i in range(N):
    num = r**i
    if total_str:
        total_str += '+'
    total_str += f"{num}"
    total += num
=======
r, N = input('Enter r N : ').split()
r, N, total_str, total = int(r), int(N), '', 0
for i in range(N):
    num = r**i
    if total_str:
        total_str += '+'
    total_str += f"{num}"
    total += num
>>>>>>> c492593d5974ed1e1ded5aa5d364a9ec2caedce1
print(total_str,f' = {total}')