# File: Pancake.py

# Description: Organize a stack of pancakes by flipping pancakes

# Student's Name: Simon Weisser

# Student's UT EID: saw3548

# Partner's Name: Alec Rubenstein

# Partner's UT EID: arr3634

# Course Name: CS 313E

# Unique Number: 50725

# Date Created: 3/6/19

# Date Last Modified: 3/8/19


# This function flips all pancakes above and including the pancake at index i
def flipPancakes(pList, i):
    n = len(pList)
    ordList = []
    revList = []

    for j in range(n):
        if j <= i:
            revList.append(pList[j]) # append left of (and including) i to revList
        else:
            ordList.append(pList[j]) # append all pancakes right of i to ord list
    revList.reverse() # flip the pancakes left of (and including) i
    finList = revList + ordList # combine stack of flipped pancakes with pancakes that weren't flipped
    return finList


# This function sorts the stack of pancakes in ascending order of size only by flipping
def sortPancakes(pList):
    orig_pList = ""
    for i in pList: # create a string of original stack of pancakes for output
        orig_pList = orig_pList + str(i) + " "
    pivot = len(pList) - 1 # initialize pivot as last pancake in the stack
    f_pan = True
    fin_str = ""
    while f_pan == True:

        # find max diameter in stack of pancakes above and including the pivot
        ind_max = 0
        for x in range(0,pivot + 1):
            if pList[x] >= pList[ind_max]:
                ind_max = x

        # when largest pancake isn't at the top of stack and isn't
        # at the pivot, put spatula under largest pancake and flip
        if ind_max != 0 and ind_max!= pivot:
            pList = flipPancakes(pList, ind_max)
            fin_str = fin_str + str(len(pList) - ind_max) + " " # string for output

        # when largest pancake is at the top of the stack and not at the pivot,
        # put spatula under largest pancake and flip
        elif ind_max == 0 and ind_max != pivot:
            pList = flipPancakes(pList, pivot)
            pivot -= 1 # move the pivot one pancake above
            fin_str = fin_str + str(len(pList) - 1 - pivot) + " " # string for output

        # when largest pancake is at pivot, do nothing to stack
        elif ind_max == pivot:
            pivot -= 1 # move the pivot one pancake above

        # when the pivot is the pancake at the top of the stack,
        # add 0 to output string and break the while loop
        if pivot == 0:
            fin_str = fin_str + str(0) + " "
            f_pan = False

    print(orig_pList) # print original stack of pancakes
    print(fin_str) # print the output


def main():
    lines = []
    with open("pancake.txt") as file: # open file to read from
        for line in file:
            a = [int(i) for i in line.split(" ")] # convert string of file to integers
            lines.append(a)
    file.close()
    for userList in lines:
        sortPancakes(userList)

main()
