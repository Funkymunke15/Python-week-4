# Davis Arita
# September 21, 2022
# CS 131 In Class lecture lab 3
# manipulating a string

string = "  Hello World   "
print(string)
print("The number of l's is %d" % string.count("l"))
print("***" + string.strip()+"***")
print("***" + string.lstrip() + "***")
print("***" + string.rstrip() + "***")

print(string.strip().replace("o", "***"))
