
# Davis Arita
# September 19, 2022
# CS 131 Exercise 4 part D
# calculates tension

mass = 2
rope = 3
maxTension = 60

speed = int(input("Enter the rotation speed: "))
tension = (mass * speed ** 2) / rope

if tension > maxTension:
    print("The rope breaks.")
else:
    print("The rope does not break.")
