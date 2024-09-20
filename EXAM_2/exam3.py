r, N = input('Enter r N : ').split()
r, N, total_str, total = int(r), int(N), '', 0
for i in range(N):
    num = r**i
    if total_str:
        total_str += '+'
    total_str += f"{num}"
    total += num
print(total_str,f' = {total}')