def reverse_tuple(t):
    return t[::-1]

def count_line(file_name, word):
    try:
        file = open(file_name)
        char_dict = {}
        count = 0
        word_line = 0
        line_number = 0
        for line in file:
            count += 1
            word_line += line.count(word)
            if word in line:
                line_number += count
                for char in line:
                    if char != ' ' and char.isalpha():
                        char_dict[char] = char_dict.get(char, 0) + 1
            
        my_keys = sorted(char_dict.items(), key=reverse_tuple, reverse=True)[:3]
        
        print(f'Number of "{word}" => {word_line}')
        print(f'Sum of line number => {line_number:,}')
        print(f'Total lines => {count:,}')
        max_stars = max(char_dict.values())
        for key, value in my_keys:
            print(f' {key}  => {"*" * value:<{max_stars}} {value:02d}')
        file.close()
    except:
        print(f'Error can not open file => {file_name}')

def main():
    print(' *** Histogram ***')
    file_name, word = input('Enter file name and word : ').split()
    count_line(file_name, word)
    print('===== End of program =====')

if __name__ == "__main__":
    main()