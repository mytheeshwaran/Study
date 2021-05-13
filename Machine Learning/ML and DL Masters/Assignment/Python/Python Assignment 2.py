#Program 1

"""
Create the below pattern using nested for loop in Python.
    *
    * *
    * * *
    * * * *
    * * * * *
    * * * *
    * * *
    * *
    *
"""

max_star = 6

for outer_val in range(0,max_star,1):
    print_result = []
    for inner_val in range(0,outer_val):
        print_result.append('*')
    print("".join(print_result))


for outer_val in range(max_star,0,-1):
    print_result = []
    for inner_val in range(0,outer_val):
        print_result.append('*')
    print("".join(print_result))

#Program 1

"""
Write a Python program to reverse a word after accepting the input from the user.
"""
input_val = input("Please enter input : ")

print(input_val[::-1])