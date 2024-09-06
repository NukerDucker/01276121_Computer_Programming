print(" *** Sum odd / Subtract even ***")
usr_input = [int(i) for i in (input('Enter numbers : ')).split()]
ans = 0
for i in usr_input:
    if i % 2 == 0:
        ans -= i
    else:
        ans += i
print(f"Sum is {ans}")            