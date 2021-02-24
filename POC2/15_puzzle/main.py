"""
Loyd's Fifteen puzzle - solver and visualizer
Note that solved configuration has the blank (zero) tile in upper left
Use the arrows key to swap this tile with its neighbors
"""

import poc_fifteen_gui

class Puzzle:
    """
    Class representation for the Fifteen puzzle
    """

    def __init__(self, puzzle_height, puzzle_width, initial_grid=None):
        """
        Initialize puzzle with default height and width
        Returns a Puzzle object
        """
        self._height = puzzle_height
        self._width = puzzle_width
        self._grid = [[col + puzzle_width * row
                       for col in range(self._width)]
                      for row in range(self._height)]

        if initial_grid != None:
            for row in range(puzzle_height):
                for col in range(puzzle_width):
                    self._grid[row][col] = initial_grid[row][col]

    def __str__(self):
        """
        Generate string representaion for puzzle
        Returns a string
        """
        ans = ""
        for row in range(self._height):
            ans += str(self._grid[row])
            ans += "\n"
        return ans

    #####################################
    # GUI methods

    def get_height(self):
        """
        Getter for puzzle height
        Returns an integer
        """
        return self._height

    def get_width(self):
        """
        Getter for puzzle width
        Returns an integer
        """
        return self._width

    def get_number(self, row, col):
        """
        Getter for the number at tile position pos
        Returns an integer
        """
        return self._grid[row][col]

    def set_number(self, row, col, value):
        """
        Setter for the number at tile position pos
        """
        self._grid[row][col] = value

    def clone(self):
        """
        Make a copy of the puzzle to update during solving
        Returns a Puzzle object
        """
        new_puzzle = Puzzle(self._height, self._width, self._grid)
        return new_puzzle

    ########################################################
    # Core puzzle methods

    def current_position(self, solved_row, solved_col):
        """
        Locate the current position of the tile that will be at
        position (solved_row, solved_col) when the puzzle is solved
        Returns a tuple of two integers        
        """
        solved_value = (solved_col + self._width * solved_row)
        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == solved_value:
                    return (row, col)
        assert False, "Value " + str(solved_value) + " not found"

    def update_puzzle(self, move_string):
        """
        Updates the puzzle state based on the provided move string
        """
        zero_row, zero_col = self.current_position(0, 0)
        for direction in move_string:
            if direction == "l":
                assert zero_col > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col - 1]
                self._grid[zero_row][zero_col - 1] = 0
                zero_col -= 1
            elif direction == "r":
                assert zero_col < self._width - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col + 1]
                self._grid[zero_row][zero_col + 1] = 0
                zero_col += 1
            elif direction == "u":
                assert zero_row > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row - 1][zero_col]
                self._grid[zero_row - 1][zero_col] = 0
                zero_row -= 1
            elif direction == "d":
                assert zero_row < self._height - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row + 1][zero_col]
                self._grid[zero_row + 1][zero_col] = 0
                zero_row += 1
            else:
                assert False, "invalid direction: " + direction

    ##################################################################
    # Phase one methods

    def lower_row_invariant(self, target_row, target_col):
        """
        Check whether the puzzle satisfies the specified invariant
        at the given position in the bottom rows of the puzzle (target_row > 1)
        Returns a boolean

        Tile zero is positioned at (i, j).
        
        All tiles in rows i+1 or below are positioned at their solved location.
        
        All tiles in row i to the right of position (i, j) are positioned at their solved location.
        """

        #Makes sure  Tile is positioned at (i,j)
        target_row_test = target_row
        while target_row_test < self.get_height():
            col_index = 0
            while col_index < self.get_width():          
                if self.current_position(target_row_test,target_col) != (target_row_test,target_col):
                    #assert False, 'Issue with the row below'    
                    return False
                col_index += 1
            target_row_test+=1
        
        #Makes sure all tiles in rows i to the rightare at the solved location
        target_col_test=target_col+1
        while target_col_test < self.get_width()-1:
            if self.current_position(target_row,target_col_test) != (target_row,target_col_test):
                #assert False, 'Tile ' + str((target_row,target_col_test)) + ' is not correct'
                return False
            target_col_test += 1

        return True

    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        """
        # replace with your code
        self.lower_row_invariant(target_row,target_col)
        return ""

    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        """
        # replace with your code
        return ""

    #############################################################
    # Phase two methods

    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean
        """
        # replace with your code

        return False

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """
        # replace with your code
        return False

    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        """
        # replace with your code
        return ""

    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """
        # replace with your code
        return ""

    ###########################################################
    # Phase 3 methods

    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string0
        """
        # replace with your code
        return ""

    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """
        # replace with your code
        self.solve_interior_tile(2,2)

        return ""


obj = Puzzle(3, 3, [[8, 7, 6], [5, 4, 3], [2, 1, 0]])
 #expected False but received True

#obj = Puzzle(3, 3, [[0, 1, 2], [3, 4, 5], [6, 7, 8]]) 
#obj.row0_invariant(0) expected True but received False


#obj = Puzzle(3, 3, [[4, 3, 2], [1, 0, 5], [6, 7, 8]]) 
#obj.row1_invariant(1) expected True but received False


#obj = Puzzle(3, 3, [[4, 3, 2], [1, 0, 5], [6, 7, 8]]) 
#obj.solve_2x2() returned incorrect move string ''


#obj = Puzzle(3, 3, [[3, 2, 1], [6, 5, 4], [0, 7, 8]]) 
#obj.solve_col0_tile(2) returned incorrect move string ''


#obj = Puzzle(3, 3, [[8, 7, 6], [5, 4, 3], [2, 1, 0]]) 
#obj.solve_interior_tile(2, 2) returned incorrect move string ''


#obj = Puzzle(3, 3, [[8, 7, 6], [5, 4, 3], [2, 1, 0]]) 
#obj.solve_puzzle() returned incorrect move string ''


#obj = Puzzle(3, 3, [[4, 1, 0], [2, 3, 5], [6, 7, 8]]) 
#obj.solve_row0_tile(2) returned incorrect move string ''


#obj = Puzzle(3, 3, [[2, 5, 4], [1, 3, 0], [6, 7, 8]]) 
#obj.solve_row1_tile(2) returned incorrect move string ''

poc_fifteen_gui.FifteenGUI(obj)





