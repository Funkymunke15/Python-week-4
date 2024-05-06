# Davis Arita
# september 19, 2022
# CS 131 exercise 4 Part B
# repeats order.py but takes input from the user whether lenient increasing
# or decreasing is allowed. 
mode = input("Do you want strict or lenient? ")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if mode == "strict":
    if num1 > num2 > num3:
        print("They are in decreasing order.")
    elif num3 > num2 > num1:
        print("They are in increasing order.")
    else:
        print("They are neither in increasing order nor decreasing order.")
elif mode == "lenient":
    if num1 > num2 or num2 > num3:
        print("They are in decreasing order.")
    elif num3 > num2 or num2 > num1:
        print("They are in increasing order.")
    elif num1 == num2 == num3:
        print("They are in both increasing order and decreasing order.")
    else:
        print("They are neither in increasing order nor decreasing order")

