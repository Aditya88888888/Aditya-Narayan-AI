# Write a Python program to print all positive numbers in a range.

# Python program to print positive Numbers in given range 
  
start, end = -4, 19
  
# iterating each number in list 
for num in range(start, end + 1): 
  
    # checking condition 
    if num >= 0: 
        print(num, end=" ") 