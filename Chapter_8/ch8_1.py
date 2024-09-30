def get_factorial(number: int):
    factorial = 1
    for i in range(1, number + 1):
        factorial = factorial * i
    return factorial
an_integer = int(input('Enter an integer : '))

print(get_factorial(an_integer))