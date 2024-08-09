print(" *** Prime number summation ***")
start, stop, max_sum = input("Enter start stop max_sum : ").split()
start = int(start)
stop = int(stop)
max_sum = int(max_sum)
current_sum = 0
prime_sum_str = ""
prime_num_count = 0

for num in range(start, stop + 1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            if current_sum + num > max_sum:
                break
            if prime_sum_str:
                prime_sum_str += "+"
            prime_sum_str += f"{num}"
            current_sum += num
            prime_num_count += 1
if prime_sum_str:
    prime_sum_str += f" = {current_sum:,}"
    print(prime_sum_str)
    print(f"Total = {prime_num_count}")
else:
    print("Invalid input !!!")

print("===== End of program =====")
