print(" *** Thai/US Conversion ***")
cash, rate = (input("Enter cash rate : ")).split()
rate = float(rate)
cash = float(cash)
cash_usd = int(cash/rate)
cash_thb = cash_usd * rate

print("--------exchange--------")
print(f"{cash_thb:,.3f} THB to {cash_usd:,.3f} USD")

print("--------current USD banknote--------")
remain_bills = cash_usd
hund_bills = remain_bills // 100
remain_bills %= 100
fifty_bills = remain_bills // 50
remain_bills %= 50
twen_bills = remain_bills // 20
remain_bills %= 20
ten_bills = remain_bills // 10
remain_bills %= 10
five_bills = remain_bills // 5
remain_bills %= 5
one_bills = remain_bills // 1
remain_bills %= 1

output = ""
if hund_bills > 0:
    output += f"{hund_bills} one-hundred {'bill' if hund_bills == 1 else 'bills'}\n"
if fifty_bills > 0:
    output += f"{fifty_bills} fifty {'bill' if fifty_bills == 1 else 'bills'}\n"
if twen_bills > 0:
    output += f"{twen_bills} twenty {'bill' if twen_bills == 1 else 'bills'}\n"
if ten_bills > 0:
    output += f"{ten_bills} ten {'bill' if ten_bills == 1 else 'bills'}\n"
if five_bills > 0 :
    output += f"{five_bills} five {'bill' if five_bills == 1 else 'bills'}\n"
if one_bills > 0 :
    output += f"{one_bills} one {'bill' if one_bills == 1 else 'bills'}"
print(output.strip())
print("===== End of program =====")