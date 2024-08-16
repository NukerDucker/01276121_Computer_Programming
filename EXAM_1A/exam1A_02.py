num = input("Enter Num : ")
try:
    num = int(num)
    if num < 0:
        print(f"{num} is Negative")
    elif num > 0:
        print(f"{num} is Positive")
    elif num == 0:
        print("Zero")        
except ValueError:
    print("Not Number")    