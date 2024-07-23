usr_inp = input(" *** Transform second ***\nEnter seconds : ")
try:
    num = int(usr_inp)
    if num < 0:
        print(f"This number ({usr_inp}) is not VALID !!!")
    else:    
        seconds = num    
        weeks = seconds // (7 * 24 * 3600)
        seconds %= (7 * 24 * 3600)
        days = seconds // (24 * 3600)
        seconds %= (24 * 3600)
        hours = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        
        output = f"{num:,} seconds ==> "
        if weeks > 0:
            output += f"{weeks} {'week' if weeks == 1 else 'weeks'} "
        if days > 0:
            output += f"{days} {'day' if days == 1 else 'days'} "
        if hours > 0:
            output += f"{hours} {'hour' if hours == 1 else 'hours'} "
        if minutes > 0:
            output += f"{minutes} {'minute' if minutes == 1 else 'minutes'} "
        if seconds > 0 :
            output += f"{seconds} {'second' if seconds == 1 else 'seconds'}"
        print(output.strip())
except ValueError:
    print("! ! ! please enter a whole number ==>", usr_inp)
    print(f"This number ({usr_inp}) is not VALID !!!")
print("===== program end =====")