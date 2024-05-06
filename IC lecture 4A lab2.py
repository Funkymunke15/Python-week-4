# Davis Arita
# September 19, 2022
# CS 131 Lecture 4A lab 2
# calculates the shipping cost

shipping = 0
international = input("Are you shipping internationally(yes or no)? ")
if international == "yes":
    shipping = 10
else:
    continental = input("Are you shipping continental (yes or no)? ")
    if continental == "no":
        shipping = 10
    else:
        shipping = 5

print(f"The shipping rate is ${shipping:.2f}")
