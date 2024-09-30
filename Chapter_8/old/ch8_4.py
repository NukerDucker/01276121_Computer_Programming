def SumArrayZero(num_list):
    summation = []
    length = len(num_list)
    if length <= 2:
        print()
    for i in range(length):
        for j in range(i + 1, length):
            for k in range(j + 1, length):
                triplet = [num_list[i], num_list[j], num_list[k]]
                if sum(triplet) == 0 and triplet not in summation:
                    summation.append(triplet)
    return summation

input_list = input('Enter Your List : ').split(' ')
num_list = [int(i) for i in input_list]
print(SumArrayZero(num_list))
