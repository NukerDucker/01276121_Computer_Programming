def rotateLeft(message,n):
    n = n % len(message)
    rotated_list = message[n:] + message[:n]
    return rotated_list

print(" *** Left-Rotate string ****")
message,n = input("Enter string / n : ").split('/')
n = int(n)
message = message.strip()
print(f"New string => {rotateLeft(message,n)}")
print("===== End of program =====")