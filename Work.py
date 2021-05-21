#  File: Work.py

#  Description: Finds the minimum amount of lines of code to
#  write given productivity factor and total number of lines to code

#  Student Name: Simon Weisser

#  Student UT EID: saw3548

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 3/2/19

#  Date Last Modified: 3/4/19

def findCups(n, k, v):

    if n == 0:
        a = 0
    elif n // k == 0:
        a = 1
    else:
        a = 0 # a represents the cups of coffee
        lineDone = int(v) #lines done after zero cups of coffee is v
        while a != -1 and lineDone < n: # while he continues to write more code per cup of coffee
                                        # and has not written at least the total amount of lines to write
            nextLines = int(v // (k ** (a + 1))) #the lines written after the next cup of coffee
            if nextLines == 0: #lines written after next cup is zero
                a = -1 # sets a = -1 to show that no matter how much coffee Vyasa drinks,
                       # he will not be able to write more lines of code and not finish the assignment
                break
            else:
                a += 1 # increase by one cup of coffee
                lineDone = lineDone + nextLines # increase the number of lines written

    return a

def binary_search(n, k):

    target = -1 # -1 assigned to values v where he can not finish the code
    nList = []
    for i in range(1, n+1): # creates a list of integers from 1 up to n
        nList.append(i)
    lower = 0 # the initial lower bound
    upper = len(nList) - 1 # the initial upper bound
    while lower < upper:
        x = lower + (upper - lower) // 2 # midpoint
        val = findCups(n, k, nList[x]) # cups of coffee needed at the midpoint
        if upper == x: # when the midpoint is the upper bound
            print(nList[x]) # v is the upper bound of list nList since nlist is in ascending order
            break
        elif lower == x: # when the midpoint is the lower bound
            print(nList[x+1]) # v is the upper bound of list nList since nlist is in ascending order
            break
        if val != target: #when it is possible to finish the code at the midpoint value
            upper = x
        elif val == target: #when it is not possible to finish the code at the midpoint value
            lower = x

def main():

    lines = []
    with open("work.txt") as file: #open file to read from
        for line in file:
            a = [int(i) for i in line.split(" ")] #convert string of file to integers
            lines.append(a)
    file.close()
    testCase = lines.pop(0)
    for j in range(0, len(lines)): #make sure the input values are in range
        if (lines[j][0] < 1) or (lines[j][0] > 10**6):
            print("Error. The number of lines, n, must be between 1 and 1,000,000 inclusive.")
            exit()
        elif (lines[j][1] < 2) or (lines[j][1] > 10):
            print("Error. The productivity factor, k, must be between 2 and 10 inclusive.")
            exit()
    for i in range(0, len(lines)):
        binary_search(lines[i][0], lines[i][1]) #run the binary search

main()