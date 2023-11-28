# Excercises - Day 1

# 1. Check the python version you are using
import sys
print(sys.version)

# 2. Do the following operations. The operands are 3 and 4.

# addition
print(3 + 4)

# subtraction
print(3 - 4)

# multiplication
print(3 * 4)

# modulus
print(3 % 4)

# division
print(3 / 4)

# exponential
print(3 ** 2)

# floor division
print(3 // 2)

# 3. Write the following strings
print("Nicolas") # Name
print("Luévano") # Family Name
print("United States") # Country
print("I am enjoying watching the Miami Dolphins win")

# 4. Check the data types of the following
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Nicolas', 'Python', 'United States']))
print(type('Nicolas'))
print(type('Luévano'))
print(type('United States'))

# Write an example for different Python data types

# Integer
print(13)

# Float
print(13.0)

# Complex
print(2 + 4j)

# String
print('this is a string')

# Boolean
print(True)
print(False)

# List
print(['this','is','a','list'])
print([1,2,3,4,5])
print([1,'this',2,'is',3,'a',4,'set'])

# Tuple
print(('like', 'a', 'list', 'but', 'immutable'))

# Set
print({4, 3, 2, 5, 7, 8}) # only stores unique items

# Dictionary
print({
    'first_name': 'Nicolas',
    'last_name': 'Luévano',
    'problems': 99,
    'is_baller': True,
    'skills': ['this', 'that', 'third']
})

# Find an Euclidian distance between (2, 3) and (10, 8)
import math

a = 2
b = 3

c = 10
d = 8

diff_one = c - a
diff_two = d - b

sqr_sum = (diff_one ** 2) + (diff_two ** 2)

result = math.sqrt(sqr_sum)
print(result)

