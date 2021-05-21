#  File: Boxes.py

#  Description: Given a list of boxes, this programs finds the largest subset(s) of boxes that can fit into one another.

#  Student Name: Simon Weisser

#  Student UT EID: saw3548

#  Partner Name: Alec Rubenstein

#  Partner UT EID: arr3634

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 3/22/19

#  Date Last Modified: 2/24/19


# check if one box fits into another
def does_fit(box1, box2):
  return (box1[0] < box2[0]) and (box1[1] < box2[1]) and (box1[2] < box2[2])

# standard subset function except it checks the conditions
# before added to box to the list of subsets
def subsets (a, b, lo, subset):
  hi = len(a)
  if (lo == hi):
    if check_dimensions(b) and len(b) > 1:
        subset.append(b)
        return
  else:
    c = b[:]
    b.append (a[lo])
    subsets (a, c, lo + 1, subset)
    subsets (a, b, lo + 1, subset)

# check if all the boxes in a given subset fit
def check_dimensions(sub):
    for i in range(0, len(sub) - 1):
        if does_fit(sub[i], sub[i + 1]) == False:
            return False
    return True

def main():
  # open file for reading
  in_file = open ("./boxes.txt", "r")

  # read the number of boxes
  line = in_file.readline()
  line = line.strip()
  num_boxes = int (line)

  # create an empty list of boxes
  box_list = []

  # read the list of boxes from the file
  for i in range (num_boxes):
    line = in_file.readline()
    line = line.strip()
    box = line.split()
    for j in range (len(box)):
      box[j] = int (box[j])
    box.sort()
    box_list.append (box)
  print(box_list)

  # close the file
  in_file.close()

  # sort the box list
  box_list.sort()

  # find the smallest boxes that can fit into
  orig_sub = []
  fin_sub = []

  # get all subsets of boxes
  subsets(box_list, orig_sub, 0, fin_sub)

  # find the largest subset(s) of boxes
  max = 2
  for i in range(0, len(fin_sub)):
     if len(fin_sub[i]) > max:
        max = len(fin_sub[i])

  # keep track of it
  badBoxes = []
  for j in range(0, len(fin_sub)):
      if len(fin_sub[j]) != max:
          badBoxes.append(fin_sub[j])

  for sub in badBoxes:
      fin_sub.remove(sub)

  # sort the list to meet output conditions
  fin_sub.sort()

  # if there are no subsets of at least 2 elements
  if len(fin_sub) == 0:
      print("No Nesting Boxes")
  else:
    print ("Largest Subset of Nesting Boxes")
    for subset in fin_sub:
      for box in subset:
        print (box)
      print('')

main()
