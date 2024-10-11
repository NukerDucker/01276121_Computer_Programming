def count_line(file_name, word):
    fhand = open(file_name)
    count = 0
    word_line = 0
    for line in fhand:
        count += 1
        if word in line:
            word_line += 1
    print(f'Number of lines having "{word}" => {word_line}')
    print('Total lines =>', count)
    fhand.close()

def main():
    print(' *** Find number of lines for specific word ***')
    file_name, word = input('Enter file name and word : ').split()
    count_line(file_name, word)

if __name__ == "__main__":
    main()