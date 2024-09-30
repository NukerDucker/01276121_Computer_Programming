def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    output = f"{fahrenheit:.3f}F"
    return output

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    output = f"{celsius:.3f}C"
    return output

usr_input = input('Enter Temperature : ')

if 'C' in usr_input or 'c' in usr_input:
    num = float(usr_input.replace('C',''))
    print(celsius_to_fahrenheit(num))
if 'F' in usr_input or 'f' in usr_input:
    num = float(usr_input.replace('F',''))
    print(fahrenheit_to_celsius(num))