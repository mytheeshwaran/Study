#Program 1

"""
Write a Python Program to implement your own myreduce() function which works exactly
like Python's built-in function reduce()
"""
def myreduce(anyfunc, sequence):

    result = sequence[0]

    for item in sequence[1:]:
        result = anyfunc(result, item)

    return result

def sum(x,y):
    return x + y

result = str(myreduce(sum, [10,20,30]))

print ("Output of myreduce function : "   +  result)

#Program 2

"""
Write a Python program to implement your own myfilter() function which works exactly
like Python's built-in function filter()
"""

def myfilter(anyfunc, sequence):

    result = []
    for item in sequence:
        if anyfunc(item):
            result.append(item)
    return result

def ispositive(x):
    if (x <= 0):
        return False
    else:
        return True

out_result = str(myfilter(ispositive, [0,1,-2,3,4,5]))
print ("Filter +ve value : "  +  out_result)

#Program 3

"""
Implement List comprehensions to produce the following lists.
Write List comprehensions to produce the following Lists
['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
[[2], [3], [4], [3], [4], [5], [4], [5], [6]] [[2, 3, 4, 5], [3, 4, 5, 6],
[4, 5, 6, 7], [5, 6, 7, 8]]
[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3,3)]
"""

input_list = ['x','y','z']
result = [ element*num for element in input_list for num in range(1,5)  ]
print(str(result))


input_list = ['x','y','z']
result = [ element*num for num in range(1,5) for element in input_list  ]
print(str(result))


input_list = [2,3,4]
result = [ [element+num] for element in input_list for num in range(0,3)]
print(str(result))


input_list = [2,3,4,5]
result = [ [element+num for element in input_list] for num in range(0,4)  ]
print(str(result))


input_list=[1,2,3]
result = [ (b,a) for a in input_list for b in input_list]
print(str(result))