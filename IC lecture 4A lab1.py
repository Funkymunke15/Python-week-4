# Davis Arita
# September 19, 2022
# CS 131 Lecture 4A lab 1
# calculates a percentage discount based on a price cutoff

discountBelow = .08
discountAbove = .16
priceCutoff = 128
totalPrice = 0
price = int(input("Please enter the total purchase price: "))
if price >= priceCutoff:
    totalPrice = price - (price * discountAbove)
else:
    totalPrice = price - (price * discountBelow)

print(f"The price after the discount is ${totalPrice:.2f}")
