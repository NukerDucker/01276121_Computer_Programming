def create_dict(lst):
    output_dict = {}
    for i in range(0, len(lst), 2):
        output_dict[lst[i]] = lst[i + 1]
    return output_dict

print(' *** Creating Dictionary ***')
usr_input = input('Enter text : ').split()
print(create_dict(usr_input))
print('===== End of program =====')