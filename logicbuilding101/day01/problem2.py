"""
Problem: Write a program that takes a few different values (an integer, a float, a string, a boolean, and a list) and for each one prints:
    The value itself
    Its type (using type())
    Its memory size in bytes (using sys.getsizeof())
Input: user enters different data types
Output: prints the type of all data types

Approach:
Read the user input using the input fucntion then print the same value, then using the type() fucntion print the type of data and using the getsizeof function print the size of data

"""

import sys
n1 = int(input("Enter a int data type: "))
n2 = float(input("Enter a float data type: "))
n3 = str(input("Enter a string data type: "))
n4 = bool(input("Enter a Boolen data type: "))
n5 = input("Enter a list data type: ")
n5_list = n5.split(',')

print(n1)
print(n2)
print(n3)
print(n4)
print(n5_list)
print(type(n1))
print(type(n2))
print(type(n3))
print(type(n4))
print(type(n5_list))
print(sys.getsizeof((n1)))
print(sys.getsizeof((n2)))
print(sys.getsizeof((n3)))
print(sys.getsizeof((n4)))
print(sys.getsizeof((n5_list)))