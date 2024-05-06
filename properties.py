# Davis Arita
# September 19, 2022
# CS 131 Exercise 4 part C
# reads a string and prints whether it contains only letters, only uppercase letters,
# only lowercase letters, starts with an uppercase letter,
# only digits, or ends with a period


string = input("Enter a string: ")

if string.isalpha():
    print("The string contains only letters.")
if string.isupper():
    print("All letters in the string are uppercase letters.")
if string.islower():
    print("All letters in the string are lowercase letters.")
if string.isdigit():
    print("The string contains only digits.")
if string[0].isupper():
    print("The string starts with an uppercase letter")
if string[-1] == ".":
    print("The string ends with a period")