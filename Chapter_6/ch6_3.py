print("*** Minimum Occurrence ***")
usr_input = [int(i) for i in input("Enter some numbers: ").split()]

frequency = len(usr_input) + 1
#counter = 0
for i in usr_input:
    curr_frequency = usr_input.count(i)
    if curr_frequency < frequency : 
        frequency = curr_frequency
        num = i

print(num)
