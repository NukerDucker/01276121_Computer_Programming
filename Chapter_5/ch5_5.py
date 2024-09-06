print(" *** Pyramid-XV ***")
height = int(input("Enter height : "))
offset = 0
for row in range(height):
    
    dashes = '-' * (height - 1 - row)
    periods = '.' * row
    char = ""
    
    for i in range(row + 1):
        char += chr((ord('A')) + (offset % 26))
        offset += 1
    mid_text = f"{periods}{char}"
    
    if row % 2 == 0:
        reverse_str = ""
        for alphabeth in mid_text:
            reverse_str = f"{alphabeth}{reverse_str}"
        print(f"{dashes}{reverse_str}{dashes}")
    else:
        print(f"{dashes}{mid_text}{dashes}")
                
print("===== End of program =====")