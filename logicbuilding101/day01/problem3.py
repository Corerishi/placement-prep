"""
Problem:  Find the Larger Number Among Two Numbers
Input: user enters two numbers
Output: prints the larger number

Approach:
Read the user input using the input fucntion and then using comparison operators

"""

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
if n1 > n2:
    print(f"The first number {n1} is larger")
elif n1 < n2:
    print(f"The second number {n2} is larger")
elif n1 == n2:
    print(f"Both numbers are equal")
else:
    print(f"Enter valid number")