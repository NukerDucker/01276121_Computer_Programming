num = input("Enter second: ")
try:
    num = int(num)
    if num < 0 :
        print("! ! ! please enter a whole number ==>", num) # this is not the one in the actual exam but close enough
    else:
        seconds = num    
        weeks = seconds // (7 * 24 * 3600)
        seconds %= (7 * 24 * 3600)
        days = seconds // (24 * 3600)
        seconds %= (24 * 3600)
        hours = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60 # this is not the one in the actual exam but close enough

        print(f"{num:,} seconds => ", end='')
        if weeks < 0:
            print(f"{weeks} week ", end='')
        else:
            print(f"{weeks} weeks ", end='')

        if days <= 1:
            print(f"{days} day ", end='')
        else:
            print(f"{days} days ", end='') 
              
        if hours <= 1:
            print(f"{hours} hour ", end='')
        else:
            print(f"{hours} hours ", end='')

        if minutes <= 1:
            print(f"{minutes} minute ", end='')
        else:
            print(f"{minutes} minutes ", end='')
               
        if seconds <= 1:
            print(f"{seconds} second ", end='')
        else:
            print(f"{seconds} seconds ", end='')   
except:
    print(f"This number ({num}) is not VALID !!!", end='') # this is not the one in the actual exam but close enough
print("\n====End Of Program====")