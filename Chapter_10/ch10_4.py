def count_line(file_name, word):
    try:
        fhand = open(file_name, 'r', encoding='UTF-8')
        count = 0
        word_line = 0
        line_number = 0
        for line in fhand:
            count += 1
            if word in line:
                word_line += 1
                line_number = line_number + count
        print(f'Number of lines having "{word}" => {word_line}')
        print(f'Sum of line number => {line_number:,}')
        print(f'Total lines => {count:,}')
        fhand.close()
    except:
        print(f'Error can not open file => {file_name}')
        print('===== End of program =====')
        quit()

def main():
    print(' *** File Error Handling ***')
    file_name, word = input('Enter file name and word : ').split()
    count_line(file_name, word)
    print('===== End of program =====')

if __name__ == "__main__":
    main()
