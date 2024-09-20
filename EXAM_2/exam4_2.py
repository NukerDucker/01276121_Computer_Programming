n = int(input('Enter height: '))

pattern = []
count = 0
for i in range(1, n + 1):
    row = []
    for j in range(i - 1):
        row.append(' ')
    for j in range(2 * (n - i) + 1):
        row.append('*')
        count += 1
    for j in range(i - 1):
        row.append(' ')
            
    row.append(' | ')
    
    for j in range(n - i):
        row.append(' ')
    for k in range(2 * i - 1):
        row.append('*')
            
    pattern.append(row)

for row in pattern:
    print(''.join(row))
print(count)
