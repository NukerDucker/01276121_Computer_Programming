print(" *** Matrix multiplication C = A x B ****")
list1, list2 = (input("Enter Matrix 1 / Matrix 2 : ")).split("/")
list1 = [int(a) for a in list1.split()]
list2 = [int(b) for b in list2.split()]

mat1 = [list1[i:i+3] for i in range(0, 9, 3)]
mat2 = [list2[i:i+3] for i in range(0, 9, 3)]
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(3):
    for j in range(3):
        for k in range(3):
            result[i][j] += mat1[i][k] * mat2[k][j]

for i in range(3):
    print(f"{mat1[i][0]:>2} {mat1[i][1]:>2} {mat1[i][2]:>2} {'x' if i == 1 else ' '}"
          f"{mat2[i][0]:>2} {mat2[i][1]:>2} {mat2[i][2]:>2} {'=' if i == 1 else ' '} "
          f"{result[i][0]:>2} {result[i][1]:>2} {result[i][2]:>2}")
print("===== End of program =====")    
