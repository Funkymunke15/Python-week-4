# Davis Arita
# September 19, 2022
# CS 131 Exercise 4 part E
# finds the number of times a substring appears in a text
string ="""Debating me breeding be answered an he. Spoil event was words her
off cause any. Tears woman which no is world miles woody. Wished be do
mutual except in effect answer. Had friendship thoroughly cultivated son
hills day ten. Examine waiting his evening day passage proceed."""
un = "un"
an = "an"
strIn = "in"
he = "he"

countUn = string.count(un)
unIndex = string.find(un)
countAn = string.count(an)
anIndex = string.find(an)
countIn = string.count(strIn)
inIndex = string.find(strIn)
countHe = string.count(he)
heIndex = string.find(he)

print("In the following paragraph:\n")
print("----------------------------------------------------------------------")
print(string)
print("----------------------------------------------------------------------\n")

print("\"un\" appears in the text", countUn,"time(s) and the lowest index of the first occournce of \"un\" is at index",unIndex)
print("\"an\" appears in the text", countAn,"time(s) and the lowest index of the first occournce of \"on\" is at index",anIndex)
print("\"in\" appears in the text", countIn,"time(s)and the lowest index of the first occournce of \"on\" is at index", inIndex)
print("\"he\" appears in the text", countHe,"time(s) and the lowest index of the first occournce of \"on\" is at index", heIndex)

