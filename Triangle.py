#  File: Triangle.py

#  Description: Find largest path through triangle using brute force, greed algorithm, divide and conquer, and dynamic programinng


from timeit import timeit


# returns the greatest path sum using exhaustive search
def brute_force (grid):
    n = len(grid)
    max = 0
    all_paths = brute_force_help(grid) # create a list of all possible paths
    for path in all_paths:
        pSum = 0
        for j in range(n): # determines the sum of values in path
         x = grid[j][path[j]]
         pSum += x
         if max < pSum: # if sum of path greater than the largest sum of previous paths
                    # then assign it as the path of the maximum sum
            max = pSum
    return max

# returns a list of all possible paths through the triangle
def brute_force_help(grid):
  possible_paths = [[0]] # row index at the starting point

  for i in range(1, len(grid) + 1):
     temp_paths = []
     for path in possible_paths:
        col = path[-1] # last index in path
        # path 1 becomes new path including the value left in the row below
        p1 = path[:]
        p1.append(col)
        temp_paths.append(p1)
        # path 2 becomes new path including the value right in the row below
        p2 = path[:]
        p2.append(col+1)
        temp_paths.append(p2)

     possible_paths = temp_paths # assign all possible paths to the most recent list of paths

  return possible_paths

# returns the greatest path sum using greedy approach
def greedy (grid):
    n = len(grid)
    col = 0
    sum = 0
    for i in range(n - 1):
        if grid[i + 1][col] > grid[i + 1][col + 1]: #if value left below greater than value right below
            sum += grid[i][col] # add current value to sum
            col = col # path stays in same column row below
        else: # if value right below greater or equal to value left below
            sum += grid[i][col] # add current value to sum
            col += 1 # path moves one column right in row below
    sum += grid[n - 1][col] # add larger value in the last row
    return sum


# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer (grid):
        # return max value in the list of sums of all possible paths
        return max(divide_conquer_help(grid, 0,0,0))

# function creates a list of sums for all possible paths
def divide_conquer_help(grid, row, col, tot):
        if row >= len(grid): # base case when row is greater than index of final row
            return [tot]
        elif row == len(grid) - 1: # last row of the triangle
            cur = grid[row][col]
            # add final value to the path
            return divide_conquer_help(grid, row + 1, col, tot + cur) # recursion will hit base case
        else:
            cur = grid[row][col]
            # return both possible paths moving forward
            return divide_conquer_help(grid, row + 1, col, tot + cur) + divide_conquer_help(grid, row + 1, col + 1, tot + cur)

# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):
        return dynamic_prog_helper(grid, 0, 0)

# recursively finds the value
def dynamic_prog_helper (grid, row, col):
    if row >= len(grid): # base case when row is greater than index of final row
        return 0
    else:
        cur = grid[row][col] # current position
        x = cur + dynamic_prog_helper(grid, row + 1, col + 1) # recursion for value right and below current position
        y = cur + dynamic_prog_helper(grid, row + 1, col) # recursion for value left and below current position
        return max(x,y) # return the higher valued branch at current position

# reads the file and returns a 2-D list that represents the triangle
def read_file ():

  # open file for reading
  in_file = open ("triangle.txt", "r")

  # read the number of rows
  line = in_file.readline()
  line = line.strip()
  num_rows = int (line)

  # create an empty list of rows
  tri_list = []

  # read the list of boxes from the file
  for i in range (num_rows):
    line = in_file.readline()
    line = line.strip()
    value = line.split()
    for j in range (len(value)):
      value[j] = int (value[j])
    tri_list.append (value)
  return tri_list



def main ():
  # read triangular grid from file
  grid = read_file()

  # output greatest path from exhaustive search
  times = timeit ('brute_force({})'.format(grid), 'from __main__ import brute_force', number = 10)
  times = times / 10
  # print time taken using exhaustive search
  print("The greatest path sum through exhaustive search is " + str(brute_force(grid)) + ".")
  print("The time taken for exhaustive search is " +str(times) + " seconds.")
  print()

  # output greatest path from greedy approach
  times = timeit ('greedy({})'.format(grid), 'from __main__ import greedy', number = 10)
  times = times / 10
  # print time taken using greedy approach
  print("The greatest path sum through greedy search is " + str(greedy(grid)) + ".")
  print("The time taken for greedy approach is " + str(times) + " seconds.")
  print()

  # output greatest path from divide-and-conquer approach
  times = timeit ('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number = 10)
  times = times / 10
  # print time taken using divide-and-conquer approach
  print("The greatest path sum through recursive search is " + str(divide_conquer(grid)) + ".")
  print("The time taken for recursive search is " + str(times) + " seconds.")
  print()

  # output greatest path from dynamic programming
  times = timeit ('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number = 10)
  times = times / 10
  # print time taken using dynamic programming
  print("The greatest path sum through dynamic programming is " + str(dynamic_prog(grid)) + ".")
  print("The time taken for dynamic programming is " + str(times) + " seconds.")
  print()


if __name__ == "__main__":
  main()
