def odd_even(arr, s):
    odd = [arr[i] for i in range(len(arr)) if i % 2 == 0]
    even = [arr[i] for i in range(len(arr)) if not i % 2 == 0]
    return odd if s.lower() == 'odd' else even

print("*** Odd Even ***")
s = input('Enter Input : ').split(',')
if s[0] == "L":
    print(odd_even(s[1].split(' '),s[2]))
elif s[0] == "S":
    print(''.join(odd_even(s[1],s[2])))