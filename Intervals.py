# File: Interval.py

# Description: Collapses intersecting intervals and produces output of non-intersecting intervals

def organizeTuples(tupleList):

    #organizes the tuples by the first value, then the second value
    tupleList = sorted(tupleList, key=lambda tup: (tup[0], tup[1]))

    return tupleList

def checkIntersection(userList):

    # assign the first interval values into two variable that track the lower and upper bound for each non-intersectiong interval
    collapseIntervalMin = userList[0][0]
    collapseIntervalMax = userList[0][1]

    nonIntersect = []

    for numbers in range(1, len(userList)):

        # the condition below idetify gaps in two consecutives intervals and start a new collapsed non-intersectiong interval
        if userList[numbers][0] > collapseIntervalMax:
            nonIntersect.append((collapseIntervalMin, collapseIntervalMax))
            collapseIntervalMin = userList[numbers][0]
            collapseIntervalMax = userList[numbers][1]

        if userList[numbers][0] <= collapseIntervalMax and userList[numbers][1] >= collapseIntervalMax:
            collapseIntervalMax = userList[numbers][1]

    # Add the last interval to the list
    nonIntersect.append((collapseIntervalMin, collapseIntervalMax))

    return nonIntersect

def main():

    userList = []

    #reads from the input.txt file, creates tuple for two user input values, adds the tuples to a list
    userIntervals = open("intervals.txt", "r")
    for line in userIntervals:
        userTuples = tuple(map(int, line.strip().split()))
        userList.append(userTuples)

    #organizes the tuples in the user list by value
    sortedUserList = organizeTuples(userList)

    finalInterval = checkIntersection(sortedUserList)
    print("Non-intersecting Intervals:")
    print(*finalInterval, sep='\n')

    #organize the list by the range on the tuple
    finalInterval.sort(key=lambda tup:(abs(tup[1]-tup[0])))
    print('\n'"Non-intersecting Intervals in order of size:")
    print(*finalInterval, sep='\n')
    userIntervals.close()

main()
