print(" *** Reverse Even ***")
usr_input = [int(i) for i in input("Enter integers : ").split()]
even_numbers = [i for i in usr_input if i % 2 == 0]
result_list = []
even_numbers.reverse()
even_index = 0

for num in usr_input:
    if num % 2 == 0:
        result_list.append(even_numbers[even_index])
        even_index += 1
    else:
        result_list.append(num)
        
print(usr_input)
print(result_list)
print("===== End of program =====")
