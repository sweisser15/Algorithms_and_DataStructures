#  File: Queens.py

#  Description: Compute the number of solutions to the Queens Problem on a chess board of size 1x1 - 16x16.

class Queens(object):
    # initialize the board
    def __init__(self, n=8):
        self.board = []
        self.n = n
        self.solutions = 0 # counter to keep track of number of solutions

        for i in range(self.n):
            row = []
            for j in range(self.n):
                row.append('*')
            self.board.append(row)

    # check if no queen captures another
    def is_valid(self, row, col):
        for i in range(self.n):
            if (self.board[row][i] == 'Q' or self.board[i][col] == 'Q'):
                return False
        for i in range(self.n):
            for j in range(self.n):
                row_diff = abs(row - i)
                col_diff = abs(col - j)
                if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
                    return False
        return True

    # do a recursive backtracking solution
    def recursive_solve(self, col):
        if (col == self.n):
            self.solutions += 1
            return True
        else:
            for i in range(self.n):
                if (self.is_valid(i, col)):
                    self.board[i][col] = 'Q'
                    self.recursive_solve(col + 1) # check the next column with queen in current position
                    self.board[i][col] = '*' # continue checking through current column with queen not in position
            return False

    # print out the number of solutions for the size of the board
    def solve(self):
        self.recursive_solve(0) # begin recursion from column 0
        print("Number of solutions: " + str(self.solutions))


def main():

    userInput = eval(input("Enter the size of board: "))
    print(" ")
    while userInput < 1 or userInput > 16:
        userInput = eval(input("Enter the size of board (1 - 16 inclusive): "))
        print(' ')

    # create a regular chess board
    game = Queens(userInput)

    # place the queens on the board
    game.solve()


main()
