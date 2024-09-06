print(" *** The number of distinct remainders ***")
divisor, sequence_str = (input("Enter a divisor / a sequence : ")).split("/")
divisor = int(divisor)
sequence = sequence_str.split()
sequence = [int(i) for i in sequence]
count = [count.append(num % divisor) for num in sequence if (num % divisor) not in count]
print(f"Distinct remainders = {len(count)}")
print("===== End of program =====")