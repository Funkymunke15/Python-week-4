# Davis Arita
# September 19, 2022
# CS 131 Exercise 4 part A
# evaluates if a list of 3 numbers is increasing, decreasing, or neither.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 > num2 > num3:
    print("They are in decreasing order.")
elif num3 > num2 > num1:
    print("They are in increasing order.")
else:
    print("They are neither in increasing order nor decreasing order.")

