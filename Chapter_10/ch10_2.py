def count_line(file_name):
    fhand = open(file_name)
    count = 0
    empty = 0
    for line in fhand:
        count += 1
        if not line.strip():
            empty += 1
    print('Empty lines =>', empty)
    print('Total lines =>', count)
    fhand.close()
    
def main():
    print(' *** Find Empty lines ***')
    file_name = input('Enter file name : ')
    count_line(file_name)

if __name__ == "__main__":
    main()