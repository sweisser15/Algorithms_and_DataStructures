#  File: ExpressionTree.py

#  Description: Create expression tree, evaluate tree, and print tree in pre and post order traversal.

#  Student Name: Simon Weisser

#  Student UT EID: saw3548

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 4/16/19

#  Date Last Modified: 4/17/19

# implementation of Stack class
class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append (item)

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check the item on top of the stack
  def peek (self):
    return self.stack[-1]

  # check if the stack is empty
  def is_empty (self):
    return (len (self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len (self.stack))

class Node(object):
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

class Tree(object):
    def __init__(self):
        self.root = Node(None) # initialize root as empty node

    def create_tree(self, expr):
        stack = Stack() # create an empty stack
        operators = ['+', '-', '*', '/', '//', '%', '**']
        current = self.root # set position to root of tree

        for char in expr:
            if char == '(':
                stack.push(current) # push node
                current.lchild = Node(None) # set left child node null
                current = current.lchild # move position to left child
            elif char in operators:
                current.data = str(char) # update data at node
                stack.push(current) # push node
                current.rchild = Node(None) # set right child null
                current = current.rchild # move position to right child
            # if str(char) is a digit or contains a decimal point
            elif ("." in char) or (char.isdigit()):
                current.data = char # update data at node
                current = stack.pop() # move position to node at top of
                                      # stack, remove node from stack
            elif char == ')':
                if not stack.is_empty():
                    current = stack.pop() # move position to node at top of stack,
                                          #  remove node from stack

    # recursively evaluate values at nodes by performing operand in parent node
    # on respective child nodes
    def evaluate(self, aNode):
        if aNode.data == "+":
            return self.evaluate(aNode.lchild) + self.evaluate(aNode.rchild)
        elif aNode.data == "-":
            return self.evaluate(aNode.lchild) - self.evaluate(aNode.rchild)
        elif aNode.data == "/":
            return self.evaluate(aNode.lchild) / self.evaluate(aNode.rchild)
        elif aNode.data == "*":
            return self.evaluate(aNode.lchild) * self.evaluate(aNode.rchild)
        elif aNode.data == "//":
            return self.evaluate(aNode.lchild) // self.evaluate(aNode.rchild)
        elif aNode.data == "%":
            return self.evaluate(aNode.lchild) % self.evaluate(aNode.rchild)
        elif aNode.data == "**":
            return self.evaluate(aNode.lchild) ** self.evaluate(aNode.rchild)
        elif (aNode.data.isdigit() == True) or ("." in aNode.data):
            # if data is digit, eval to distinguish between float and int
            return eval(aNode.data)


    # print nodes of expression tree in pre-order traversal
    def pre_order(self, aNode):
        if (aNode != None):
            print(aNode.data, end = ' ')
            self.pre_order(aNode.lchild)
            self.pre_order(aNode.rchild)

    # print nodes of expression tree in post-order traversal
    def post_order(self, aNode):
        if (aNode != None):
            self.post_order(aNode.lchild)
            self.post_order(aNode.rchild)
            print (aNode.data, end = ' ')

def main():

    file = open("expression.txt", "r") # open file
    user_expr = file.readline() # read line from file
    file.close() # close file

    # create list of characters in expression, removing spaces
    final_expr = user_expr.split(" ")

    expr_tree = Tree() # initialize empty tree
    expr_tree.create_tree(final_expr) # create tree with characters in expression list

    print(str(user_expr) + " = " + str(expr_tree.evaluate(expr_tree.root))) # evaluate
    print()
    print("Prefix Expression:", end = ' ')
    expr_tree.pre_order(expr_tree.root) # pre order traversal
    print()
    print()
    print("Postfix Expression:", end = ' ') # post order traversal
    expr_tree.post_order(expr_tree.root)

main()