# File: OfficeSpace.py

# Description: Sets up system for employees to request cubicles in new office space

class Point(object):

    #constructor with floats x and y
    def __init__(self, x=0, y=0):
        self.x = float(x)
        self.y = float(y)

    #string used for error checking
    def __str__(self):
        return '(' + str(self.x) + ", " + str(self.y) + ")"

class Rectangle(object):

    #constructor with lower left and upper right points of cubicle
    def __init__(self,ll_x = 0, ll_y=0, ur_x = 1, ur_y = 1):
        if ((ur_x > ll_x) and (ur_y > ll_y)):
            self.ur = Point(ur_x,ur_y)
            self.ll = Point(ll_x, ll_y)
        else:
            self.ur = Point(1, 1)
            self.ll = Point(0, 0)

    #determine whether or not a point is inside the rectangle
    def point_in_Rect(self, p):
        return (self.ll.x < p.x) and (self.ur.x > p.x) and (self.ur.y > p.y) and (self.ll.y < p.y)

    #determine width of cubicle
    def width(self):
        return self.ur.y - self.ll.y

    #determine length of cubicle
    def length(self):
        return self.ur.x - self.ll.x

    #calculate area of cubicle
    def area(self):
        return self.length() * self.width()

    #string used for error checking
    def __str__(self):
        return "LL: " + str(self.ll) + ", UR: " + str(self.ur)

def main():

   #read lines from the file office.txt and append to a list
   lines = []
   with open("office.txt") as file:
       for line in file:
           a = line.split(' ')
           lines.append(a)
   file.close()

   #condition for iterating through the input list
   new_test_case = True
   #ctr = 0 ensures that output is calculated for only the first input
   ctr = 0
   for elements in lines:

       if new_test_case == True:
           length = int(elements[0])
           width = int(elements[1])
           numcases = int(lines[ctr + 1][0])
           nextCase=ctr+numcases+2
           new_test_case = False
           #determines the amount of cubicles based on input value and puts rectangle info into a list
           testList = lines[(ctr+2):(ctr+2+numcases)]
           #area of the entire office
           total = length*width

           #append the names of employee who outlines office space into a list
           nameList = []
           for t in range(numcases):
               name = []
               name.append(testList[t][0])
               nameList.append(name)

           #organizes cubicle by assigning lower left and upper right corner to employees name
           for i in range(numcases):
                testList[i][0] = Rectangle(int(testList[i][1]),int(testList[i][2]),int(testList[i][3]),int(testList[i][4]))
                nameList[i].append(int(testList[i][0].area()))
           totalContested = 0

           for x in range(width):
               for y in range(length):
                   #point p is the center of 1 by 1 square
                   P = Point(float(x+0.5),float(y+0.5))

                   #determines for any given point if more than one person requested it
                   contestCTR = 0
                   for i in range(numcases):
                      if testList[i][0].point_in_Rect(P) == True:
                         contestCTR += 1
                   #if more than one person requested the same point, the count of total contested is increased
                   if contestCTR >= 2:
                       totalContested += 1
                       #determines which employees contested the point and removes it from their cubicle's total area
                       for i in range(numcases):
                           if testList[i][0].point_in_Rect(P):
                               nameList[i][1] -= 1

           print()
           print("Total", int(total))
           Unallocated = int(total)- totalContested
           for unalloc in (nameList):
               Unallocated=Unallocated-int(unalloc[1])
           print("Unallocated" , Unallocated)
           print("Contested", totalContested)
           for tot in (nameList):
               print(tot[0],tot[1])


       #iterates through multiple different offices
       ctr=ctr+1
       if(ctr==nextCase):
           new_test_case = True
main()
