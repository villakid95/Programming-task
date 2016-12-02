def backwardsString():
    string = "Reverse this text"
    string = string.split()
    newString = []
    for letters in string:
        newString.insert(0,letters)
    return " ".join(newString)
# FUNCTION REVERSE ()
# x -> "text"
# x -> x.SPLIT()
# y = []
# FOR z IN x
#   y.INSERT(0,z)
#RETURN "".JOIN(y)

#Run Time Bound = 0(n^2)
