def isFizzBuzz(num):
    output = ''
    for i in range(len(divisors)):
        if num % divisors[i] == 0:
            output += phrases[i]
    return output if output else str(num)

usr_input = input('input : ').split()

starts_from = int(usr_input[0])
ends_at = int(usr_input[1])

divisors = []
phrases = []

for i in range(2, len(usr_input), 2):
    divisors.append(int(usr_input[i]))
    phrases.append(usr_input[i + 1])

for num in range(starts_from, ends_at + 1):
    print(isFizzBuzz(num))