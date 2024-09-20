print(" *** Sum odd / Subtract even ***")
usr_input = [int(i) for i in (input('Enter numbers : ')).split()]
total = sum([-i if i % 2 == 0 else i for i in usr_input])
print(f"Sum is {total}")