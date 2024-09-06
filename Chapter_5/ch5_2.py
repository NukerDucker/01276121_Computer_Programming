print(" *** Maximum value ***")
largest = None 
nums = input("Enter some numbers : ").split()

for num in nums:
    try:
        if num == 'stop' or int(num) == -1:
            break
        num = int(num)
        if largest is None or num > largest:
            largest = num 
    except ValueError:
        pass

if largest is None:
    print("Max value = None")
else:
    print(f"Max value = {largest}")
print("===== End of program =====")