#  File: Josephus.py

#  Description: Use circular linked list to solve Josephus problem given elimination number, start point, and number of soliders.

class Link(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class CircularList(object):
  # Constructor
  def __init__ (self):
      self.first = None

  # Insert an element (value) in the list
  def insert (self, data):
      linkedList = Link(data) # create a new link
      current = self.first # start at begining of list

      # if linked list is empty, insert new link at the begining
      if current == None:
          self.first = linkedList
          linkedList.next = linkedList # set linked list to be circular
          return
      while current.next != self.first:
          current = current.next
      current.next = linkedList # insert new link at the end of list
      linkedList.next = self.first # make sure linked list is circular

  # Find the link with the given data (value)
  def find (self, data):
      current = self.first
      if current.data is None: # empty list
          return None
      while current.data != data:
          if current.next == self.first: # data not in list
              return None
          current = current.next
      return current # return link

  # Delete a link with a given data (value)
  def delete (self, data ):
      previous = self.first
      current = self.first

      if current is None:
          return None
      # set previous equal to the last value of the circular linked list
      while (previous.next != self.first):
          previous = previous.next
      # while the node doesn't equal data, move a node up
      while current.data != data:
              previous = current
              current = current.next
      if self.first == self.first.next: # if linked list has one element, list is empty
          self.first = None
      else:  # if linked list not one element long
          self.first = current.next
      previous.next = current.next # remove current node

  # Delete the nth link starting from the Link start
  # Return the next link from the deleted Link
  def delete_after (self, start, n):
      current = self.find(start) # start point
      i = 1 # elimination includes person from start point
      # eliminates the next person at elimination number
      while i != n:
          current = current.next
          i += 1
      print(str(current.data)) # print person
      self.delete(current.data) # eliminate person
      return current.next # make next starting point at next person

  # Return a string representation of a Circular List
  def __str__ ( self ):
      current = self.first
      linked_list = ""
      while (current.next != self.first):
          linked_list += str(current.data) + "  "
          current = current.next
      return linked_list

def main():

    # read from file and assign appropriate values
    file = open("josephus.txt", "r")
    aList = []
    for i in range(0,3):
        aList.append(int(file.readline()))
    num_soliders = aList[0]
    start = aList[1]
    n = aList[2]
    solider_circle = CircularList()

    # insert soldiers into linked list in order
    for x in range(1, num_soliders + 1):
        solider_circle.insert(x)

    i = 1
    # eliminate (num_soliders - 1) soliders so that 1 solider remains
    while i < num_soliders:
        start = solider_circle.delete_after(start, n) # eliminate solider
        start = start.data # new starting point is at node next to the eliminated solider
        i += 1

    # eliminate the final solider
    solider_circle.delete_after(start, n)

main()
