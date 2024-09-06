print(" *** Median Mean ***")
usr_input = input("Enter numbers : ").split()
list0 = usr_input
list1 = []
list2 = []

for i in usr_input:
    try:
        num = int(i)
        list1.append(num)
    except ValueError:
        list2.append(i)

n = len(list1)          
mean = sum(list1) / n
sorted_list = list1.copy()
sorted_list.sort()

middle = len(sorted_list) // 2
if len(sorted_list) % 2 == 0:
    median = (sorted_list[middle - 1] + sorted_list[middle]) / 2
else:
    median = sorted_list[middle]

mean = int(mean) if int(mean) == mean else f"{mean:.2f}"
median = int(median) if int(median) == median  else f"{median:.2f}"
print(f"list0 =  {list0}")
print(f"list1 =  {list1}")
print(f"Mean = {mean}")
print(f"sort = {sorted_list}")
print(f"Median = {median}")
print(f"list2 =  {list2}")
print("===== End of program =====")
