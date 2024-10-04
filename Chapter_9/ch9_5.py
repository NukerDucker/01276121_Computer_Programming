usr_input = input('Enter increment : ')
increment = float(usr_input)
occur = 0.0
count = 0
max_increment = 1000000

for i in range(1, 1000001):
    occur += increment
    count += 1
    
    expected_value = increment * count 

    if occur != expected_value:
        print(f"accumulated {count} times")
        print(f"final accumulated value is {occur}")
        print(f"which does not equal the expected {expected_value}")
        break

    if count >= max_increment:
        print("reached max increment, breaking.")
        break
