def char_count(usr_input):
    words = usr_input.split()
    full_count = {}

    for word in words:
        count_dict = {}
        for char in word:
            count_dict[char] = word.count(char)
        full_count[word] = count_dict
        
    total_count = {}
    
    for char in usr_input.replace(" ", ""):
        total_count[char] = usr_input.count(char)
    
    full_count[usr_input] = total_count

    max_char = max(total_count, key=total_count.get)
    max_count = total_count[max_char]

    for word, count in full_count.items():
        print(f"{word} = {count}")
    
    print(f"Maximum Character Count: {max_char} {max_count}")

if __name__ == "__main__":
    usr_input = input('Enter : ')
    char_count(usr_input)
    print("===== End of program =====")