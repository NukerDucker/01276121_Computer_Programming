num = int(input("Enter usage: "))
amount = 0
if 0 <= num <= 150:
  amount = num * 2.74
elif 150.01 <= num <= 200:
  amount = (150 * 2.74) + ((num - 150) * 3.10)
elif 200.01 <= num <= 500:
  amount = (150 * 2.74) + (50 * 3.10) + ((num - 200) * 4.70)
elif 500.01 <= num:
  amount = (150 * 2.74) + (50 * 3.10) + (300 * 4.70) + ((num - 500) * 5.23)
print(f"The amount is {amount:,.2f} baht")