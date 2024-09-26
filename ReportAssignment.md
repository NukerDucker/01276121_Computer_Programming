# Report Assignment 2024
**For Computer Programming 01276121**
Napaul Intharasing 67011178

---
### Chapter 8 Lab 5 
The Task:
ให้รับตัวเลขจำนวนเต็ม 2 จำนวน
จำนวนแรก คือ ความสูง
จำนวนที่สอง คือ รูปแบบของสี่เหลี่ยม
1 เป็นสี่เหลี่ยมกลวง 
2 เป็นสี่เหลี่ยมกลวงตัวเลข
3 เป็นสี่เหลี่ยมตัวเลข

**My approach**
```Python {.line-numbers}
def num_generator(num_range):
    num_str = ''
    num = 1
    for _ in range(1, num_range + 1):
        if num == 10:
            num = 0
        num_str += f'{num}'
        num += 1
    return num_str
# -----------------------------------------------
def square_hollow_star(h):
    output = ''
    output += f"{'*' * h}\n"
    for _ in range(h - 2):
        output += f'*{" " * (h - 2)}*\n'
    output += '*' * h
    return output
# -----------------------------------------------
def square_hollow_num(h):
    output = ''
    num_str = num_generator(h)
    reversed_num = num_str[::-1]
    output += f'{reversed_num}\n'
    for i in range(len(num_str) - 2):
        output += f'{reversed_num[i + 1:i + 2]}{" " * (len(num_str) - 2)}{num_str[i + 1:i + 2]}\n'
    output += num_str
    return output
# -----------------------------------------------   
def square_num(h):
    num_str = num_generator(h)
    output = ''
    for i in range(len(num_str)):
        output += f'{num_str[:i] + num_str[i] * (h - i)}'
        if i < len(num_str) - 1:
            output += '\n'
    return output
# -----------------------------------------------       
print(' *** Display square ***')

height, type_square = input('Enter Your List : ').split()
height = int(height)

if type_square == '1':
    print(square_hollow_star(height))
elif type_square == '2':
    print(square_hollow_num(height))
elif type_square == '3':
    print( square_num(height))
    
print('===== End of program =====')
# -----------------------------------------------
```
I chose this approach because, for me, it's the simplest and most efficient way to generate the required square patterns.

--- 
### **Dissecting the program**
```Python {.line-numbers}
def num_generator(num_range):
    num_str = ''
    num = 1
    for _ in range(1, num_range + 1):
        if num == 10:
            num = 0
        num_str += f'{num}'
        num += 1
    return num_str
# -----------------------------------------------
```
I created a function called ```num_generator()``` that takes ```num_range``` as input. I start with a variable num set to 1 and an empty string ```num_str``` to store the result. The loop runs up to ```num_range```, adding each number to the string, and resets num to 0 when it reaches 10. Finally, it returns the completed string. 
```Python
for _ in range (1, num_range + 1)
```
This creates a loop that increments ```num``` by 1 in each iteration until the specified range is met. 
```python    
    if num == 10:
        num = 0
```
If ```num``` equals 10, it resets to 0 so the function won't exceed one digit and the loop continues adding numbers to the string.
```Python        
        num_str += f'{num}'
        num += 1
    return num_str
```
Then, I add num to an f-string to form a line of numbers, and return this as the function's output.

---

```Python {.line-numbers}
def square_hollow_star(h):
    output = ''
    output += f"{'*' * h}\n"
    for _ in range(h - 2):
        output += f'*{" " * (h - 2)}*\n'
    output += '*' * h
    return output
# -----------------------------------------------
```
The next function, ```square_hollow_star()```, creates a hollow square with ```*``` as its sides. It takes ```h``` (height) as input, ensuring the square has equal width and height. 
```Python
    output = ''
    output += f"{'*' * h}\n"
```
First, I create an empty string called ```output```. Then, I add ```*``` repeated ```h``` times to represent the top of the square, followed by a ```\n``` or newline.
```Python
    for _ in range(h - 2):
        output += f'*{" " * (h - 2)}*\n
```
The loop then adds rows with ```*``` on both sides and spaces in the middle, followed by a```\n```or newline, leaving out the top and bottom rows. Finally, I return the output.

---

```Python {.line-numbers}
def square_hollow_num(h):
    output = ''
    num_str = num_generator(h)
    reversed_num = num_str[::-1]
    output += f'{reversed_num}\n'
    for i in range(len(num_str) - 2):
        output += f'{reversed_num[i + 1:i + 2]}{" " * (len(num_str) - 2)}{num_str[i + 1:i + 2]}\n'
    output += num_str
    return output
# -----------------------------------------------
```
The ```square_hollow_num()``` function creates a hollow square where the sides are made of numbers. The top row is a reversed version of the string of numbers, which can't go beyond single digits. I use ```num_generator()``` to generate this string and assign it to ```num_str```.

```Python
    reversed_num = num_str[::-1]
    output += f'{reversed_num}\n'
```
This will reverse the ```num_str``` and assign it to ```reversed_num``` using Python's slice notation ```list[<start>:<stop>:<step>]```. So, when you use ```num_str[::-1]```, it starts from the end of the string and moves towards the beginning, taking each element, effectively reversing ```num_str```. Then, I add the reversed ```num_str``` followed by ```\n``` to create a new line in the output f-string.

---


```Python {.line-numbers}
def square_num(h):
    num_str = num_generator(h)
    output = ''
    for i in range(len(num_str)):
        output += f'{num_str[:i] + num_str[i] * (h - i)}'
        if i < len(num_str) - 1:
            output += '\n'
    return output
```
The forth function, ```square_num()```, creates a square filled with numbers. Each row starts with number 1 and repeats the last digit until the length equals the side.
```Python
    num_str = num_generator(h)
    output = ''
```
First, I use ```num_generator()``` to create the number string, then I created an empty string as an output.

```Python    
    for index_string in range(len(num_str)):
        output += f'{num_str[:index_string] + num_str[index_string] * (height - index_string)}'
        if index_string < len(num_str) - 1:
            output += '\n'
```
Then, I loop through each index of num_str, adding the appropriate pattern of numbers for each row, and return the final output. 

---

```Python {.line-numbers}
print(' *** Display square ***')

height, type_square = input('Enter Your List : ').split()
height = int(height)

if type_square == '1':
    square_hollow_star(height)
elif type_square == '2':
    square_hollow_num(height)
elif type_square == '3':
    square_num(height)
    
print('===== End of program =====')
```

This is the rest of the program, which prints the header and footer messages. It takes two user inputs: ```height``` and ```type_square```. The ```height``` determines the size of the square, while ```type_square``` specifies the type of square (```1``` for hollow star, ```2``` for hollow number, and ```3``` for filled number). I use a simple ```if-else``` structure to decide which function to run based on the user's input.

---


### **Examples of alternatives**
* 1^st^ Example
```Python {.line-numbers}
def square_hollow_star(h):
    print('*' * h)
    for _ in range(h - 2):
        print(f'*{" " * (h - 2)}*' )
    print('*' * h)

def square_hollow_num(h):
    num_str = num_generator(h)
    print(num_str[::-1])
    reversed_num = num_str[::-1]
    for i in range(len(num_str) - 2):
        print(f'{reversed_num[i + 1:i + 2]}{" " * (len(num_str) - 2)}{num_str[i + 1:i + 2]}')
    print(num_str)
    
def square_num(h):
    num_str = num_generator(h)
    for i in range(len(num_str)):
        print(num_str[:i] + num_str[i] * (h - i))
        i += 1
```
I did not choose this approach because, although it was my initial code, I found it less flexible. Since the functions rely on ```print()```directly, there isn't much room for modification, like changing how the result is displayed or using it in different contexts without printing directly to the console. By returning the string instead, I can store or manipulate the output in various ways later on. 

* 2^nd^ Example
```Python {.line-numbers}

```

I did not chose this because...

* 3^rd^ Example
```Python {.line-numbers}

```

I did not chose this because...