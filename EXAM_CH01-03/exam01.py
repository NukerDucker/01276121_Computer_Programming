num = int(input("Enter a second: "))
hours = num // 3600
minutes = (num % 3600) // 60
seconds = num % 3600 % 60
print(f"{num:,} => {hours:02}:{minutes:02}:{seconds:02}")
