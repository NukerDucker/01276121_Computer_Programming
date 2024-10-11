cipher_key = {
    ('A', 'A'): 'b',
    ('A', 'D'): 't',
    ('A', 'F'): 'a',
    ('A', 'G'): 'l',
    ('A', 'X'): 'p',

    ('D', 'A'): 'd',
    ('D', 'D'): 'h',
    ('D', 'F'): 'o',
    ('D', 'G'): 'z',
    ('D', 'X'): 'k',

    ('F', 'A'): 'q',
    ('F', 'D'): 'f',
    ('F', 'F'): 'v',
    ('F', 'G'): 's',
    ('F', 'X'): 'n',

    ('G', 'A'): 'g',
    ('G', 'D'): 'i/j',
    ('G', 'F'): 'c',
    ('G', 'G'): 'u',
    ('G', 'X'): 'x',

    ('X', 'A'): 'm',
    ('X', 'D'): 'r',
    ('X', 'F'): 'e',
    ('X', 'G'): 'w',
    ('X', 'X'): 'y',
}

def decoder(encoded):
    cipher_chunks = []
    decoded_word = ""

    for i in range(0, len(encoded), 2):
        cipher_chunks.append(tuple(encoded[i:i + 2]))

    for pair in cipher_chunks:
        if pair in cipher_key:
            decoded_word += cipher_key[pair]
        else:
            decoded_word = "FAILED TO DECRYPT"
            break
        
    return decoded_word

if __name__ == "__main__":
    usr_input = input('Input ADFGX cipher text: ')
    decoded_word = decoder(usr_input)
    print(decoded_word)