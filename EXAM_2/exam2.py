<<<<<<< HEAD
print(' Even largest and second largest')
even_list = [int(i) for i in input("Enter Numbers : ").split() if int(i) % 2 == 0]
even_list.sort()
print(f"Largest Number = {even_list[-1]}\n" 
=======
print(' Even largest and second largest')
even_list = [int(i) for i in input("Enter Numbers : ").split() if int(i) % 2 == 0]
even_list.sort()
print(f"Largest Number = {even_list[-1]}\n" 
>>>>>>> c492593d5974ed1e1ded5aa5d364a9ec2caedce1
      f"Second Largest Number = {even_list[-2]}" ) if len(even_list) >= 2 else print('Not Enough Data')