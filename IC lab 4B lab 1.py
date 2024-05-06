# Davis Arita
# September 21, 2022
# CS 131 In Class lecture 4B lab 1
# takes  3 integers as input and determines if they are all the same,
# all different, or neither.

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# testing if the numbers are all the same
if num1 == num2 == num3:
    print("They are all the same.")
# testing if the numbers are all different
elif num1 != num2 != num3:
    print("They are all different.")
# if neither are true print neither
else:
    print("They are all neither different nor the same.")
