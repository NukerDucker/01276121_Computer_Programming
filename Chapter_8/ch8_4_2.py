INCREASING = '0'
DECREASING = '1'

def find_substrings(input_data):
    mode, numbers = input_data.split('/')
    numbers = [int(num) for num in numbers.split()]
    if len(numbers) < 2:
        return None
    substrings = [str(numbers[0])]
    for num in numbers[1:]:
        last_number = int(substrings[-1][-1])
        if mode == INCREASING:
            is_next = num == last_number + 1
        elif mode == DECREASING: 
            is_next = num == last_number - 1
        if is_next:
            substrings[-1] += str(num)
        else:
            substrings.append(str(num))
    
    return [" ".join(list(substring)) for substring in substrings]

def main():
    print("*** Find Substrings ***")
    user_input = input("Enter mode (0 for increasing, 1 for decreasing) and numbers: ")
    substrings = find_substrings(user_input)
    if substrings is None:
        print("Error: You need at least 2 numbers.")
    else:
        for i, substring in enumerate(substrings, 1):
            print(f"Substring {i}: {substring}")
    print("===== End of program =====")

if __name__ == "__main__":
    main()
