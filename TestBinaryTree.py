#  File: TestBinaryTree.py

#  Description: Test the methods of balanced binary trees.

class Node (object):
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None

class Tree (object):
  def __init__ (self):
    self.root = None

  # Search for a node with the key
  def search (self, aNode):
    current = self.root
    while ((current != None) and (current.data != aNode)):
      if (aNode < current.data):
        current = current.lChild
      else:
        current = current.rChild
    if current == None:
        return -1
    return current

  # Returns the height of the tree
  def get_height (self, aNode):
      if aNode is None:
          return -1
      current = self.search(aNode)
      paths = []
      self.height_helper(current, 0, paths) # initialize length to 0 and start at aNode
      paths.sort() # sort list that consists of the heights of all possible paths
      return paths[-1] # return the largest height

  def height_helper (self, aNode, length, paths):
        if aNode is None:
            paths.append(length - 1) # length - 1 since leaves have height 0
            return
        else:
            self.height_helper(aNode.rChild, length + 1, paths) # increase length by 1 and move to right child
            self.height_helper(aNode.lChild, length + 1, paths) # increase length by 1 and move to left child

  # Returns the number of nodes in the left subtree and
  # the number of nodes in the right subtree and the root
  def num_nodes (self, aNode):
      current = self.search(aNode) # search for aNode
      nodes = self.num_nodes_helper(current)
      return nodes

  def num_nodes_helper (self, aNode):
      if aNode is None:
          return 0
      else: # return 1 for the current node and move to left and right children
          return 1 + self.num_nodes_helper(aNode.lChild) + self.num_nodes_helper(aNode.rChild)

  # returns the difference between the height of the left
  # sub tree and the height of the right sub tree
  def balance_factor (self, aNode):
      if aNode.lChild is None:
          if aNode.rChild is None: # leaf node
              return 0
          return -1 - self.get_height(aNode.rChild.data) # if left node is empty but right isn't
      if aNode.rChild is None:# if right node is empty but left isn't
          return self.get_height(aNode.lChild) + 1
      return self.get_height(aNode.lChild.data) - self.get_height(aNode.rChild.data)

  # returns True if the tree is balanced and False otherwise
  # in a balanced tree every node has a balance factor of -1, 0, 1
  def is_balanced (self, aNode):
      # create list nodes consists of each element as a F or T,
      # T if it has a balanced factor of -1, 0, 1
      nodes = []
      current = aNode
      self.is_balanced_helper1(current, nodes)
      # check if list has any F's
      for i in nodes:
          if i == 'F':
              return False
      return True

  def is_balanced_helper1 (self, aNode, aList):
      if aNode == None:
          return aList
      if self.is_balanced_helper2(aNode): # if balance factor valid
          aList.append('T')
          self.is_balanced_helper1(aNode.lChild, aList) # recursion on left child
          self.is_balanced_helper1(aNode.rChild, aList) # recursion on right child
          return aList
      else: #end recursion and append F
          aList.append('F')
          return aList

  # conditions of valid balance factor
  def is_balanced_helper2 (self, aNode):
      if (self.balance_factor(aNode) == 1):
          return True
      elif (self.balance_factor(aNode) == 0):
          return True
      elif (self.balance_factor(aNode) == -1):
          return True
      else:
          return False

  # Insert a node in the tree
  def insert(self, val):
      newNode = Node(val)
      if (self.root == None):
          self.root = newNode
      else:
          current = self.root
          parent = self.root
          while (current != None):
              parent = current
              if (val < current.data):
                current = current.lChild
              else:
                current = current.rChild
          if (val < parent.data):
              parent.lChild = newNode
          else:
              parent.rChild = newNode

  # create a balanced binary search tree from a sorted list
  def create_tree (self, a_list):
      return self.create_tree_helper(a_list, 0, len(a_list) - 1)


  def create_tree_helper(self, a_list, lo, hi):
      if lo > hi:
          return
      #find midpoint
      mid = (lo + hi) // 2
      cur = a_list[mid]
      self.insert(cur) #insert midpoint

      self.create_tree_helper(a_list, lo, mid - 1) # recursion on everything left of mid
      self.create_tree_helper(a_list,  mid + 1, hi) # recursion on everything right of mid

  # prints the nodes breadth first
  def print_level(self):
      current = self.root
      curLevel = 1 # determine the row
      nodes = []
      top = 1
      self.print_level_helper(curLevel, top, nodes, current) # initialize at correct row and at aNode
      while len(nodes) != 0:
          if len(nodes) == 0:
              return
          else:
              for i in nodes:
                  print(i, end=" ")
              print()
              print(nodes[-1])
              print()
              nodes = [] # make nodes back to empty list for next row
              curLevel += 1 # increase row
              self.print_level_helper(curLevel, top, nodes, current)


  def print_level_helper(self, level, cur, aList, aNode):
      if cur > level or aNode == None:
          return
      else:
          if cur == level:
              aList.append(aNode.data) # append everything on same level to list
          else:
              self.print_level_helper(level, cur + 1, aList, aNode.lChild) # increase row
              self.print_level_helper(level, cur + 1, aList, aNode.rChild) # increase row



def main():

    # Create at least two binary search trees - one balanced and
    # the other not

    # create a balanced binary tree
    balanced_list = [60,40,80,30,50,70,90,25,35,45,55,65,75,85,95]
    bal_tree = Tree()
    for dig in balanced_list:
        bal_tree.insert(dig)

    # create unbalanced binary tree
    un_balanaced_list = [60, 40, 80, 30, 50, 35]
    unbal_tree = Tree()
    for num in un_balanaced_list:
        unbal_tree.insert(num)

    # Test your function get_height() for those trees
    print("Test Balanced Tree get_height()")
    print(bal_tree.get_height(60)) # root
    print(bal_tree.get_height(40))
    print(bal_tree.get_height(90))
    print(bal_tree.get_height(35)) # leaf
    print()
    print("Test Unbalanced Tree get_height()")
    print(unbal_tree.get_height(60)) # root
    print(unbal_tree.get_height(40))
    print(unbal_tree.get_height(30))
    print(unbal_tree.get_height(35)) # leaf
    print()

    # Test your function num_nodes() for those trees
    print("Test Balanced Tree num_nodes()")
    print(bal_tree.num_nodes(60)) # nodes starting at root
    print(bal_tree.num_nodes(40))
    print(bal_tree.num_nodes(35)) # nodes starting at leaf
    print()
    print("Test Unbalanced Tree num_nodes()")
    print(unbal_tree.num_nodes(60))
    print(unbal_tree.num_nodes(40))
    print(unbal_tree.num_nodes(50))
    print(unbal_tree.num_nodes(30))
    print()

    # Find the balance factors of the roots of those trees
    print("Test Balance Factor for Root of Balanced Tree")
    print(bal_tree.balance_factor(bal_tree.root))
    print()
    print("Test Balance Factor for Root of Unbalanced Tree")
    print(unbal_tree.balance_factor(unbal_tree.root))
    print()

    # Find if the trees are balanced or not
    print("Test if the Trees are Balanced")
    print(bal_tree.is_balanced(bal_tree.root))
    print(unbal_tree.is_balanced(unbal_tree.root))
    print()

    # Create a balanced binary search tree from a sorted list
    # check that it is balance
    print("Test Create a Binary Tree and Is Balanced")
    sorted_list = [2, 3, 4, 5, 8, 9, 11, 12, 15, 16, 19, 20]
    sorted_tree = Tree()
    sorted_tree.create_tree(sorted_list)
    print(sorted_tree.is_balanced(sorted_tree.root))
    print()


    # Print all the trees that you have breadth first
    print("Test Print Balanced Tree Breadth First")
    bal_tree.print_level()
    print()
    print("Test Print Unbalanced Tree Breadth First")
    unbal_tree.print_level()
    print()
    print("Test Print Balanced Tree From Sorted List")
    sorted_tree.print_level()

main()
