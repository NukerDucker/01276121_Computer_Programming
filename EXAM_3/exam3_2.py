def pluralize(noun):
    if noun[-1] == 'y':
        if noun[-2] not in 'aeiou':
            return noun[:-1] + 'ies'
    elif noun[-1] in 'sxz' or noun[-2:] in ['sh', 'ch'] or noun[-1] == 'o':
        return noun + 'es'
    elif noun[-1] == 'f':
        return noun[:-1] + 'ves'
    elif noun[-2:] == 'fe':
        return noun[:-2] + 'ves'
    return noun + 's'

def main():
    noun = input("Enter noun : ")
    plural = pluralize(noun)
    print(f"{plural}")

if __name__ == "__main__":
    main()