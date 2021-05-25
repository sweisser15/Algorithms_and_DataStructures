# File: Palindrome.py

# Description: Finds the shortest palindrome

def reverse_join_reversed_iter(s):
    s1 = ''.join(reversed(s))
    return s1


def shortest_palindrome(word):

    # finding the revesre and appending to t original . That is a palindrome by definition.
    # We will execute the code below to determine if there is a shorter palindrome
    revOrig = reverse_join_reversed_iter(word)

    # append the original string with it reversed
    pattern = word + revOrig

    # obtain the length of the combined string
    patLength = len(pattern)

    # the following list will store the partial match values for each position
    #it will be use the last value to proone the polindrome to its' smallest size
    PmatchTable = [0]

    for i in range(1, len(pattern)):

        j = PmatchTable[i - 1]

        while j > 0 and pattern[j] != pattern[i]:
            j = PmatchTable[j - 1]

        PmatchTable.append(j + 1 if pattern[j] == pattern[i] else j)
        print(PmatchTable)


    # return the last value of the Partial match table
    a = int(PmatchTable[-1])

    # Remove the charecters from the string before shuffling appending it to the beginning of the poriginal string
    PrunedStr = pattern[0:-a]

    # determine the mid point ( end of the original string)
    finalStr = PrunedStr[(int(patLength / 2)):] + word

    print(finalStr)

def main():

    lines = []
    paliMessage = open("palindrome.txt", "r")
    fileLines = paliMessage.readlines()
    paliMessage.close()
    for line in fileLines:
        lines.append(line.strip('\n'))

    for word in lines:
        shortest_palindrome(word)

main()
