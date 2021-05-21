# this function takes as input a list v of positive integers
# it returns two lists s_v and b_v, containing the contents of
# the columns S(v) and B(v) as shown
def bottles_dp(v):

    # base case
    s_v = [v[0]] # add volume of first bottle to s_v

    # if second bottle has larger volume than first, append 2nd volume
    # if not, append the first bottle again
    if v[1] > v[0]:
        s_v.append(v[1])
    else:
        s_v.append(v[0])

    # find the possible sum at each index and append to s_v
    for i in range(2, len(v)):
        max = s_v[i - 1]
        if (s_v[i - 2] + v[i]) > max:
            max = s_v[i - 2] + v[i]
        s_v.append(max)

    b_v = [0] # initialize b_v
    i = 1
    while i < len(s_v):
        if s_v[i] == s_v[i - 1]:
            b_v.append(-1) # append -1 if adjacent indices have identical value in s_v
            i += 1
        else: # append index index is the first of identical adjacent indices in s_v
              # or if the value of the index in s_v is unique
            b_v.append(i)
            i += 1

    return s_v, b_v

# modification of subset function to determine which bottles
# were used to find the largest sum
def subsets (a, b, lo, v, largest_sum):
  hi = len(a)
  if (lo == hi):

      # if subset adds to largest sum and is valid
      if get_sum(b, v) == largest_sum and is_valid(b):

          # convert from indices to true value
          aList = []
          for num in b:
              aList.append(v[num])
          print("Numbers contributing to the sum = " + str(aList))
          return
  else:
    c = b[:]
    b.append (a[lo])
    subsets (a, c, lo + 1, v, largest_sum)
    subsets (a, b, lo + 1, v, largest_sum)

# returns the sum of a given list of indices of v
def get_sum(a, v):
    sum = 0
    for i in a:
        sum += v[i]
    return sum

# return true if numbers in list aren't adjacent in v
def is_valid(a):
    for i in range(1, len(a)):
        if a[i] == a[i - 1] + 1:
            return False
    return True

def main():
    # create empty list of bottles
    v = []

    # open file bottles.txt for reading
    in_file = open("./bottles.txt", "r")

    # read the number of bottles
    num_bottles = int(in_file.readline())

    # populate the list v with bottles
    for i in range (num_bottles):
        bottle = int(in_file.readline().strip("\n"))
        v.append(bottle)


    # close the file
    in_file.close()

    # find the greatest sum
    s_v, b_v = bottles_dp(v)

    # print the list s_v
    print("List s_v = " + str(s_v))
    print()

    # print the list b_v
    print("List b_v = " + str(b_v))
    print()

    # print the greatest sum
    print("Greatest sum = " + str(s_v[-1]))
    print()

    # print the bottles contributing to the largest sum
    # remove all -1 from b_v
    used_nums = []
    for i in b_v:
        if i != -1:
           used_nums.append(i)

    subsets(used_nums, [], 0, v, s_v[-1])



main()
