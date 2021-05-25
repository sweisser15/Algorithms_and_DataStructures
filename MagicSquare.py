#  File: MagicSquare.py

#  Description: Compute the number of magic squares of order 4 that the user inputs.

import sys

count = [] # store the number of squares printed as a global variable

# keep track of the number of squares printed
def counter(num_squares):
    count.append(1)
    if len(count) == num_squares:
        sys.exit()

def permute (a, lo, num_squares, n):
  hi = len(a)
  if (lo == hi):
      if magic_square_rows(a[lo - n:lo]): # if the final row adds up to the correct value.

          # convert 1d list into a 2d list
          a_2d = []
          for i in range(len(a)):
              if i % n == 0:
                  a_2d.append(a[i:i + n])
          if magic_square_columns_diagnols(a_2d): # if all diagonals and columns add up to correct value

              # output magic square in the correct format
              for i in a_2d:
                  for j in i:
                      print(j, end=" ")
                  print()
              counter(num_squares)
              print('')

  # Check if each row adds up to the magic number. If it does, continue permutating. If not, do nothing.
  elif (lo % n == 0):
      if magic_square_rows(a[lo - n:lo]):
          for i in range(lo, hi):
              a[lo], a[i] = a[i], a[lo]
              permute(a, lo + 1, num_squares, n)
              a[lo], a[i] = a[i], a[lo]
  else:
    for i in range (lo, hi):
      a[lo], a[i] = a[i], a[lo]
      permute(a, lo + 1, num_squares, n)
      a[lo], a[i] = a[i], a[lo]

# check if rows add up to magic number, used within permutation function
def magic_square_rows(row):
    n = len(row)
    magic_num = n * (n * n + 1) // 2
    rowSum = 0
    for j in range(len(row)):
        rowSum += row[j]
    if rowSum != magic_num:
        return False
    else:
        return True

# check if columns and diagonals each add up to magic number, used after permutation completed
def magic_square_columns_diagnols (a):
  # check dimension of 2-D list
  n = len(a)

  # calculate the canonical sum
  canon_sum = n * (n * n + 1) // 2

  # check sum of each column
  for j in range (len(a[0])):
    sum_col = 0
    for i in range (len(a)):
      sum_col += a[i][j]

    # check that the sum_col is equal to the canonical sum
    if (sum_col != canon_sum):
      return False

  # check sum of diagonal left to right
  sum_lr = 0
  for i in range (len(a)):
    sum_lr += a[i][i]

  # check that the sum_lr is equal to the canonical sum
  if (sum_lr != canon_sum):
    return False

  # check sum of diagonal right to left
  sum_rl = 0
  for i in range (len(a)):
    sum_rl += a[i][len(a) - 1 - i]

  # check that the sum_rl is equal to the canonical sum
  if (sum_rl != canon_sum):
    return False

  return True

def main ():

    nums = []
    for i in range(1, 17):  # create list of integers 1 - 16 inclusive
        nums.append(i)
    print(nums)
    num_squares = eval(input("Enter number of magic squares (2 - 20): "))
    print('')
    while num_squares < 2 or num_squares > 20: # make sure user input is in range
        num_squares = eval(input("Enter number of magic squares (2 - 20): "))
        print(' ')
    permute(nums,0, num_squares, 4)


main()
