#Program 1

"""
Write a Python Program(with class concepts) to find the area of the triangle using the below
formula.

area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
Function to take the length of the sides of triangle from user should be defined in the parent
class and function to calculate the area should be defined in subclass.

"""

class Geometry:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

class Triangle(Geometry):

    def area_of_traingle(self):
        s = (self.a + self.b + self.c)/2

        return (s* (s - self.a) * (s - self.b) * (s -self.c)) ** 0.5

a = int(input("Enter a value : "))
b = int(input("Enter b value : "))
c = int(input("Enter c value : "))

area_val = Triangle(a,b,c)

print(area_val.area_of_traingle())

#Program 2

"""
Write a function filter_long_words() that takes a list of words and an integer n and returns
the list of words that are longer than n.
"""

greater_length_list = []
def filter_long_words(word_list, length_val):
    for words in word_list:
        if len(words) > length_val:
            greater_length_list.append(words)


word_list = ['hi' , 'how' , 'what', 'there']
length_val = 3

filter_long_words(word_list,length_val)

print(greater_length_list)

#Program 3
"""
Write a Python program using function concept that maps list of words into a list of integers
representing the lengths of the corresponding words.
Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]
Here 2,3 and 4 are the lengths of the words in the list.
"""

words_list = [ 'ab','cde','erty']
length_list = []

for words in words_list:
    length_list.append(len(words))

print(length_list)

#Program 4

"""
Write a Python function which takes a character (i.e. a string of length 1) and returns True if
it is a vowel, False otherwise.
"""

vowels = ['a', 'e', 'i', 'o', 'u']

input_char = input("Enter input character : ")

if input_char in vowels:
    print(True)

else:
    print(False)
