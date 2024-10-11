def char_count(usr_input):
    words = usr_input.split()
    word_count = {}
    str_count = {}
    for word in words:
        count_dict = {}
        for char in word:
            count_dict[char] = word.count(char)
        word_count[word] = count_dict
    
    for char in usr_input.replace(" ", ""):
        str_count[char] = usr_input.count(char)
    
    word_count[usr_input] = str_count

    max_char = max(str_count, key=str_count.get)
    max_count = str_count[max_char]

    for word, count in word_count.items():
        print(f"{word} = {count}")
    
    print(f"Maximum Character Count: {max_char} {max_count}")

def main():
    usr_input = input('Enter : ')
    char_count(usr_input)
    print("===== End of program =====")

if __name__ == "__main__":
    main()