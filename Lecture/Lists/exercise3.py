print(" *** Number grid ***")
width, height = (input("Enter Width Height : ")).split()
width = int(width)
height = int(height)

list_of_numbers = list(range(1, width * height + 1))

for i in range(height):
    for j in range(width):
        print(f"{list_of_numbers[i * width + j]:>2}", end=" ")
    print()
print("===== End of program =====")