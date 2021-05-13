#Program 1

"""
 Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
 The numbers obtained should be printed in a comma-separated sequence on a single line.
"""
starting_num = 2000
ending_num = 3200

out_list = [str(num) for num in range(starting_num, ending_num + 1) if (num % 7 == 0) & (num % 5 != 0) ]
print(",".join(out_list))

#Program 2

"""
Write a Python program to accept the user's first and last name and 
then getting them printed in the the reverse order with a space between first name and last name.
"""

first_name = input("Please enter First name : ")
last_name = input("Please enter last name : ")

full_name = first_name + " " + last_name

print(full_name[::-1])

#Program 3
"""
Write a Python program to find the volume of a sphere with diameter 12 cm)
Formula: V=4/3 * π * r 3
"""

pi = 22/7
r = 12
V = 4/3 * pi * r**3

print("Volume of Sphere is : " , V)