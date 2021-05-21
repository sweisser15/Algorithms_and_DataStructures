# File: Geom.py

# Description: Performs fundamental geometry functions

# Student Name: Simon Weisser

# Student UT EID: saw3548

# Partner Name: Alec Rubenstein

# Partner UT EID: arr3634

# Course Name: CS313E

# Unique Number: 50725

# Date Created: 2/8/19

# Date Last Modified: 2/11/19

import math

class Point(object):
    # constructor
    # x and y are floats
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # get distance
    # other is a Point object
    def dist(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    # get a string representation of a Point object
    # takes no arguments
    # returns a string
    def __str__(self):
        return '(' + str(self.x) + ", " + str(self.y) + ")"

    # test for equality
    # other is a Point object
    # returns a Boolean
    def __eq__(self, other):
        tol = 1.0e-16
        return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))


class Circle(object):
    # constructor
    # x, y, and radius are floats
    def __init__(self, radius=1, x=0, y=0):
        self.radius = radius
        self.center = Point(x, y)

    # compute cirumference
    def circumference(self):
        return 2.0 * math.pi * self.radius

    # compute area
    def area(self):
        return math.pi * self.radius * self.radius

    # determine if point is strictly inside circle
    def point_inside(self, p):
        return (self.center.dist(p) < self.radius)

    # determine if a circle is strictly inside this circle
    def circle_inside(self, c):
        distance = self.center.dist(c.center)
        return (distance + c.radius) < self.radius

    # determine if a circle c overlaps this circle (non-zero area of overlap)
    # but neither is completely inside the other
    # the only argument c is a Circle object
    # returns a boolean
    def circle_overlap(self, c):
        distance = self.center.dist(c.center)
        return (distance < (self.radius + c.radius))

    # determine the smallest circle that circumscribes a rectangle
    # the circle goes through all the vertices of the rectangle
    # the only argument, r, is a rectangle object
    def circle_circumscribe(self, r):
        circR = r.ul.dist(r.lr) / 2
        centX = (r.ul.x + r.lr.x) / 2
        centY = (r.ul.y + r.lr.y) / 2
        return circR, centX, centY

    # string representation of a circle
    # takes no arguments and returns a string
    def __str__(self):
        return "Radius: " + str(self.radius) + ", Center: " + str(self.center)

    # test for equality of radius
    # the only argument, other, is a circle
    # returns a boolean
    def __eq__(self, other):
        tol = 1.0e-16
        return (abs(self.radius - other.radius) < tol)


class Rectangle(object):
    # constructor
    def __init__(self, ul_x=0, ul_y=1, lr_x=1, lr_y=0):
        if ((ul_x < lr_x) and (ul_y > lr_y)):
            self.ul = Point(ul_x, ul_y)
            self.lr = Point(lr_x, lr_y)
        else:
            self.ul = Point(0, 1)
            self.lr = Point(1, 0)

    # determine length of Rectangle (distance along the x axis)
    # takes no arguments, returns a float
    def length(self):
        return self.lr.x - self.ul.x

    # determine width of Rectangle (distance along the y axis)
    # takes no arguments, returns a float
    def width(self):
        return self.ul.y - self.lr.y

    # determine the perimeter
    # takes no arguments, returns a float
    def perimeter(self):
        return 2 * self.length() + 2 * self.width()

    # determine the area
    # takes no arguments, returns a float
    def area(self):
        return self.length() * self.width()

    # determine if a point is strictly inside the Rectangle
    # takes a point object p as an argument, returns a boolean
    def point_inside(self, p):
        return (self.ul.x < p.x) and (self.lr.x > p.x) and (self.ul.y > p.y) and (self.lr.y < p.y)

    # determine if another Rectangle is strictly inside this Rectangle
    # takes a rectangle object r as an argument, returns a boolean
    # should return False if self and r are equal
    def rectangle_inside(self, r):
        return (self.ul.x < r.ul.x) and (self.ul.y > r.ul.y) and (self.lr.x > r.lr.x) and (self.lr.y < r.lr.y)

    # determine if two Rectangles overlap (non-zero area of overlap)
    # takes a rectangle object r as an argument returns a boolean
    def rectangle_overlap(self, r):
        ur = Point(r.lr.x, r.ul.y)
        ll = Point(r.ul.x, r.lr.y)
        return (self.point_inside(r.ul)) or (self.point_inside(r.lr)) or (self.point_inside(ur)) or (
            self.point_inside(ll))

    # determine the smallest rectangle that circumscribes a circle
    # sides of the rectangle are tangents to circle c
    # takes a circle object c as input and returns a rectangle object
    def rectangle_circumscribe(self, c):
        ul_x = c.center.x - c.radius
        ul_y = c.center.y + c.radius
        lr_x = c.center.x + c.radius
        lr_y = c.center.y - c.radius
        return ul_x, ul_y, lr_x, lr_y

    # give string representation of a rectangle
    # takes no arguments, returns a string
    def __str__(self):
        return "UL: " + str(self.ul) + ", LR: " + str(self.lr)

    # determine if two rectangles have the same length and width
    # takes a rectangle other as argument and returns a boolean
    def __eq__(self, other):
        return (self.width() == other.width()) and (self.length() == other.length())


def main():
    # open the file geom.txt
    lines = []
    with open("geom.txt") as file:
        for line in file:
            a = line.split(' ')
            lines.append(a)
    file.close()

    # create Point objects P and Q
    P = Point(float(lines[0][0]), float(lines[0][1]))
    Q = Point(float(lines[1][0]), float(lines[1][1]))

    # print the coordinates of the points P and Q
    print("Coordinates of P:", Point(P.x, P.y))
    print("Coordinates of Q:", Point(Q.x, Q.y))

    # find the distance between the points P and Q
    print("Distance between P and Q:", P.dist(Q))

    # create two Circle objects C and D
    C = Circle(float(lines[2][0]), float(lines[2][1]), float(lines[2][2]))
    D = Circle(float(lines[3][0]), float(lines[3][1]), float(lines[3][2]))

    # print C and D
    print("Circle C:", C)
    print("Circle D:", D)

    # compute the circumference of C
    print("Circumference of C:", C.circumference())

    # compute the area of D
    print("Area of D:", D.area())

    # determine if P is strictly inside C
    if C.point_inside(P) == True:
        print("P is inside C")
    else:
        print("P is not inside C")

    # determine if C is strictly inside D
    if C.circle_inside(D) == True:
        print("C is inside D")
    else:
        print("C is not inside D")

    # determine if C and D intersect (non zero area of intersection)
    if C.circle_overlap(D) == True:
        print("C does intersect D")
    else:
        print("C does not intersect D")

    # determine if C and D are equal (have the same radius)
    if (C == D) == True:
        print("C is equal to D")
    else:
        print("C is not equal to D")

    # create two rectangle objects G and H
    G = Rectangle(float(lines[4][0]), float(lines[4][1]), float(lines[4][2]), float(lines[4][3]))
    H = Rectangle(float(lines[5][0]), float(lines[5][1]), float(lines[5][2]), float(lines[5][3]))

    # print the two rectangles G and H
    print("Rectangle G:", G)
    print("Rectangle H:", H)

    # determine the length of G (distance along x axis)
    print("Length of G:", G.length())

    # determine the width of H (distance along y axis)
    print("Width of H:", H.width())

    # determine the perimeter of G
    print("Perimeter of G:", G.perimeter())

    # determine the area of H
    print("Area of H:", H.area())

    # determine if point P is strictly inside rectangle G
    if G.point_inside(P) == True:
        print("P is inside G")
    else:
        print("P is not inside G")

    # determine if rectangle G is strictly inside rectangle H
    if H.rectangle_inside(G) == True:
        print("G is inside H")
    else:
        print("G is not inside H")

    # determine if rectangles G and H overlap (non-zero area of overlap)
    if H.rectangle_overlap(G) == True:
        print("G does overlap H")
    else:
        print("G does not overlap H")

    # find the smallest circle that circumscribes rectangle G
    # goes through the four vertices of the rectangle
    E = Circle()
    print("Circle that circumscribes G:", E.circle_circumscribe(G))

    # find the smallest rectangle that circumscribes circle D
    # all four sides of the rectangle are tangents to the circle
    Rec = Rectangle()
    print("Rectangle that circumscribes D:", Rec.rectangle_circumscribe(D))

    # determine if the two rectangles have the same length and width
    if (G == H) == True:
        print("Rectangle G is equal to H")
    else:
        print("Rectangle G is not equal to H")

# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()