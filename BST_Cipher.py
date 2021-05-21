class Node(object):
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

class Tree (object):
  # the init() function creates the binary search tree with the
  # encryption string. If the encryption string contains any
  # character other than the characters 'a' through 'z' or the
  # space character drop that character.
  def __init__ (self, encrypt_str):
      self.root = None
      self.values = [] # keep track of data already inserted in tree
      encrypt_str = str(encrypt_str).lower() # convert string to lower case
      for char in encrypt_str: # if char is lower case letter or space
          if (ord(char) >= 97 and ord(char) <= 122) or ord(char) == 32:
              self.insert(char)


  # the insert() function adds a node containing a character in
  # the binary search tree. If the character already exists, it
  # does not add that character. There are no duplicate characters
  # in the binary search tree.
  def insert (self, ch):
      if ch in self.values: # if ch already inserted in tree
          return
      newNode = Node(ch) # create new node
      if (self.root == None): # empty tree
          self.root = newNode
      else:
          current = self.root
          parent = self.root
          # move down the tree until current is none and parent is leaf
          while (current != None):
              parent = current
              if (ch < current.data):
                  current = current.lchild
              else:
                  current = current.rchild
          if (ch < parent.data): # if ch less than parent, make it left node
              parent.lchild = newNode
              self.values.append(ch) # add ch to values to keep track
          else:
              parent.rchild = newNode
              self.values.append(ch) # add ch to values to keep track



  # the search() function will search for a character in the binary
  # search tree and return a string containing a series of lefts
  # (<) and rights (>) needed to reach that character. It will
  # return a blank string if the character does not exist in the tree.
  # It will return * if the character is the root of the tree.
  def search (self, ch):
      current = self.root
      enc_str = ""
      # add < or > to enc_str until ch is found or node is None
      while ((current != None) and (current.data != ch)):
          if (ch < current.data):
              current = current.lchild
              enc_str += "<" # add left to string
          else:
              current = current.rchild
              enc_str += ">" # add right to string
      # return blank string if ch not found
      if current == None:
          return ''
      # return * if ch is root
      if current == self.root:
            enc_str += '*'
      return  enc_str

  # the traverse() function will take string composed of a series of
  # lefts (<) and rights (>) and return the corresponding
  # character in the binary search tree. It will return an empty string
  # if the input parameter does not lead to a valid character in the tree.
  def traverse (self, st):
      current = self.root
      for i in st:
            if i == "<":
              current = current.lchild # move to left child
            elif i == ">":
              current = current.rchild # move to right child
            elif i == "*":
              current = self.root # move to root
      char = current.data
      return char

  # the encrypt() function will take a string as input parameter, convert
  # it to lower case, and return the encrypted string. It will ignore
  # all digits, punctuation marks, and special characters.
  def encrypt (self, st):
      encr_str = ''
      word = str(st).lower()
      # add delimiter in between nodes in st
      for letter in word:
          encr_val =  self.search(str(letter))
          encr_str = encr_str + str(encr_val) + "!"
      fin_str = encr_str[0:len(encr_str) - 1] # remove final delimiter
      print(fin_str)
      return fin_str

  # the decrypt() function will take a string as input parameter, and
  # return the decrypted string.
  def decrypt (self, st):
      decr_str = ''
      # create list where elements are strings between delimiter
      word = str(st).split("!")
      for sign in word:
            letter = self.traverse(str(sign)) # traverse to find ch
            decr_str = decr_str + str(letter) # add ch to decr_str
      print(decr_str)
      return decr_str

def main():

    key = input("Enter encryption key: ")
    print()
    bst = Tree(key) # create BST with encryption key
    enc_str = input("Enter string to be encrypted: ")
    print("Encrypted string:", end = ' ')
    bst.encrypt(enc_str) # encrypt message using already created BST
    print()
    dec_str = input("Enter string to be decrypted: ")
    print("Decrypted string:", end = ' ')
    bst.decrypt(dec_str) # decrypt message using already created BST


main()

