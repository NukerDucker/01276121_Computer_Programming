def count_line(file_name):
    with open(file_name, encoding='UTF-8') as file:
        print(f'property => {file}')
        lines = file.readlines()
        line_count = len(lines)
        output = f'Total lines : {line_count:,}'
        return output
    
def main():
    print(' *** Find Total lines ***')
    file_name = input('Enter file name : ')
    print(count_line(file_name))
    print('===== End of progam =====')

if __name__ == "__main__":
    main()