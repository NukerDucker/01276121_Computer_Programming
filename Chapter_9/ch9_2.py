def create_dict(lst):
    dictionary = {}
    for i in range(0, len(lst), 2):
        if lst[i] in dictionary:
            dictionary[lst[i]] += int(lst[i + 1])
        else:
            dictionary[lst[i]] = int(lst[i + 1])
    return dictionary

def main():
    print(' *** Creating Dictionary ***')
    usr_input = input('Enter text : ').split()
    print(create_dict(usr_input))
    print('===== End of program =====')

if __name__ == "__main__":
    main()