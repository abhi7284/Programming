import math


# 3.print the element at rth row and cth col
def getElement(r,c):
    print(int((math.factorial(r)) /(int(math.factorial(r-c))*int(math.factorial(c)))),end=" ")
    #optimse nCr calc O(n^2) to O(n)
    

# 2.print row of rth row
def printNthrow(r):
    for i in range(0,r+1):
        #calc ith element
        getElement(r=r,c=i)

# 1.print upto nth row
def printPascalTriangle(n):
    for i in range(0,n+1):
        printNthrow(r=i)
        print()

#printPascalTriangle(6)

printNthrow(10)
