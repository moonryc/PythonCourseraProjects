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
    # Done

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
    def move_tile(self, row,col):
            """
            finds zero tile location and moves it to a target location
            """
            zero_pos = self.current_position(0,0)
            distance_to_target = (row - zero_pos[0], col- zero_pos[1])
            if distance_to_target[1] < 0:
                delta_x = abs(distance_to_target[1]) * 'l'
            else:
                delta_x = distance_to_target[1] * 'r'
            if distance_to_target[0] < 0:
                delta_y = abs(distance_to_target[0]) * 'u'
            else:
                delta_y =  distance_to_target[0] * 'd'

            final_move = delta_y + delta_x
            self.update_puzzle(final_move)

            return final_move

    ##################################################################

    def fetch_tile(self, target_row,target_col,target_pos):
        """
        Moves the target tile from where it is to its correct stop
        """
        distance_to_target = (target_pos[0] - target_row, target_pos[1] - target_col)
        vert_return = ''
        horiz_move = ''
        horiz_shift = ''
        delta_y = distance_to_target[0]
        delta_x = distance_to_target[1]
        shifts = abs(delta_x) - 1
        
        vert_move = abs(delta_y) * 'u'
        if delta_x < 0:  # left of vertical
            horiz_move = abs(delta_x) * 'l'
            if target_pos[0] == 0:  # in top row
                horiz_shift = shifts * 'drrul'
            else:
                horiz_shift = shifts * 'urrdl'
            if delta_y < 0: #not yet bottom row
                horiz_shift += 'dru'
        
        elif delta_x > 0:  #right of vertical
            horiz_move = abs(delta_x) * 'r'
            if delta_y < -1 or target_pos[0] == 0: #
                horiz_shift = shifts * 'dllur'
                horiz_shift += 'dlu'
            else:
                horiz_shift = shifts * 'ulldr'
                horiz_shift += 'ulld'
                if delta_y == -1: #row above target position
                    horiz_shift += 'dru'
        
        if delta_y < 0:
            vert_return = (abs(delta_y) - 1) * 'lddru'
            vert_return += 'ld'
        final_move = vert_move + horiz_move + horiz_shift + vert_return      
        return final_move
#I intend to come back and make this better
#        """
#            #finds the distance from where the target is to where the target belongs
#            distance_to_target = (target_pos[0]-target_row, target_pos[1]-target_col)
#            delta_x = distance_to_target[1]
#            delta_y = distance_to_target[0]
#            vert_return = ''
#            print 'target pos', target_pos
#            print 'target_row, target_col: ', target_row,',',target_col
#            print 'distance_to_target: ', distance_to_target
#            shift_x = abs(delta_x) -1
#            shift_y = abs(delta_y) -1
#
#            vert_move = abs(delta_y) * 'u'
#            if delta_y < 0:
#               vert_return = (shift_y * 'lddru') + 'ld'
#
#            # if target is left of 0
#            if delta_x < 0:
#                hori_move = abs(delta_x) * 'l'
#
#                hori_shift = (shift_x+1) * 'urrdl'
#
#
#            #if target is right of 0
#            else:
#                hori_move = delta_x * 'r'
#
#
#
#            final_move = hori_move + vert_move + vert_return + hori_shift
#            print final_move
#
#            return final_move
#        """

    ##################################################################
    # invarient methods
    # Done

    def this_cell_zero(self, target_row, target_col):
        """
        verifies that this cell contains zero
        """
        if self.get_number(target_row,target_col) != 0:
            print "0 is not in the correct spot, correct spot is: " + str((target_row, target_col))
            return False
        else:
            return True
    def lower_cells(self, target_row):
        """
        This checks the rows below the input target row to make sure they are correct
        """
        target_row_test = target_row+1 
        while target_row_test < self.get_height():
            col_index = 0
            while col_index < self._width:
                test_location = self.current_position(target_row_test,col_index)
                print test_location
                if self.get_number(test_location[0], test_location[1]) != self.get_number(target_row_test,col_index):
                    print 'Row below (i,j) has an error'
                    return False
                col_index +=1
            target_row_test+=1
        return True
    def row_correct(self, target_row, target_col):
        """
        checks to make sure the row to the right of 0 is correct
        """
        target_col_test=target_col+1
        while target_col_test < self.get_width()-1:
            if self.current_position(target_row,target_col_test) != (target_row,target_col_test):
                print 'Tile  in row i greater than j is not correct'
                return False
            target_col_test += 1
        return True

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

        if self.this_cell_zero(target_row,target_col) and \
            self.lower_cells(target_row) and \
            self.row_correct(target_row,target_col):
                    return True
        return False

    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string

        will solve for position j>0 and i>1
        """        
        assert self.lower_row_invariant(target_row,target_col), 'ERROR: AT interior tiles AT self.lower_row_invariant(target_row,target_col)'
        target_pos = self.current_position(target_row,target_col)
        final_move = self.fetch_tile(target_row,target_col,target_pos)
        self.update_puzzle(final_move)
        assert self.lower_row_invariant(target_row,target_col-1), 'ERROR: AT interior tiles AT self.lower_row_invariant(target_row,target_col-1)'        

        return final_move

    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        [2,4]=>[1,3]
        [3,1]=>[0,4]
        [0,5]=>[3,5]
        use ruldrdlurdluurddlur for answer
        """
        assert self.lower_row_invariant(target_row,0), 'ERROR: AT col0 tile AT self.lower_row_invariant(target_row,0)'        
        target_pos = self.current_position(target_row,0)
        delta_x = target_pos[1] - 0
        delta_y = target_pos[0] - target_row 
        solution_string = 'ur'

        if delta_y == -1 and delta_x == 0:
            solution_string += (self.get_width()-2) * 'r'
        elif delta_y == -1 and delta_x == 1:
            solution_string += 'l' + 'ruldrdlurdluurddlur' + (self.get_width()-2) * 'r'
        else:
            solution_string += self.fetch_tile(target_row-1,1,target_pos) + 'ruldrdlurdluurddlur' +(self.get_width()-2) * 'r'
        self.update_puzzle(solution_string)
        assert self.lower_row_invariant(target_row-1,self.get_width()-1)
        
        return solution_string
        
    #############################################################
    # Phase two methods

    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean
        
        zero must be the tile in (0,target_col)
        the rows below the 2nd row must be correct
        last 2 check that the coloumns to the right of these coloumns are correct 
        """

        print 'row0 invarient' 
        print 'self.row_correct(0,target_col)' + str(self.row_correct(0,target_col)  )
        print 'self.row_correct(0,target_col-1)'+ str(self.row_correct(0,target_col-1)) + str(target_col-1)

        # replace with your code
        if self.this_cell_zero(0,target_col) and \
            self.lower_cells(1) and \
            self.row_correct(0,target_col) and \
            self.row_correct(1,target_col-1):
                    return True
        return False

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean

        zero must be the tile in (0,target_col)
        the rows below the 2nd row must be correct
        check the last coloumn on the first row
        check the last coloumn on the 2nd row
        """
        if self.this_cell_zero(1,target_col) and \
            self.lower_cells(1) and \
            self.row_correct(0,target_col) and \
            self.row_correct(1,target_col):
                    return True
        return False

    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        """
        print 'need to redo this method myself'
        assert self.row0_invariant(target_col)
        target_pos = self.current_position(0, target_col)
        initial_move = 'ld'
        distance_to_target = (target_pos[0], target_pos[1] - target_col)
        if distance_to_target == (0, -1):
            tile_fetcher = ''
            homework_2by3_shifter = ''
        elif distance_to_target == (1, -1):
            tile_fetcher = 'uld'
            homework_2by3_shifter = 'urdlurrdluldrruld'
        else:
            tile_fetcher = self.fetch_tile(1, target_col - 1, target_pos)
            homework_2by3_shifter = 'urdlurrdluldrruld'
        final_move = initial_move + tile_fetcher + homework_2by3_shifter
        self.update_puzzle(final_move)
        assert self.row1_invariant(target_col - 1)
        return final_move

    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """
        target_pos = self.current_position(1,target_col)
        assert self.row1_invariant(target_col), 'ERROR: row0_invarient(target_col)'        
        solution_string = self.fetch_tile(1,target_col,target_pos) + 'ur'
        self.update_puzzle(solution_string)
        return solution_string

    ###########################################################
    # Phase 3 methods

    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string0
        """
        solution_string = ''
        assert self.row1_invariant(1), "row1_invarient on 2x2"
        if self.get_number(0,0) == 1:
            solution_string = 'ul'
        elif self.get_number(0,1) == 1:
           solution_string ='lu'
        else:
            solution_string = 'lurdlu'

        self.update_puzzle(solution_string)
        return solution_string

    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """
        solution_string= self.move_tile(self.get_width()-1,self.get_height()-1)
        for row in range(self.get_height() - 1, 1, -1):
            for col in range(self.get_width() - 1, 0, -1):
                solution_string += self.solve_interior_tile(row, col)
            solution_string += self.solve_col0_tile(row)
        for col in range(self.get_width() - 1, 1, -1):
            solution_string += self.solve_row1_tile(col)
            solution_string += self.solve_row0_tile(col)
        solution_string += self.solve_2x2()
        print solution_string
        return solution_string


            
#obj = Puzzle(4,4, [[5,4,1,3],[8,0,2,7],[10,13,6,11],[9,12,14,15]])
#obj = Puzzle(4,4, [[4,6,1,3],[5,2,7,0],[8,9,10,11],[12,13,14,15]])
#obj = Puzzle(4,4, [[5,4,1,3],[8,15,2,7],[10,13,6,11],[9,12,14,0]])

#obj = Puzzle(4, 5, [[7, 2, 0, 3, 4], [5, 6, 1, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]])
#obj.row0_invariant(2)
#obj = Puzzle(4,4)

#poc_fifteen_gui.FifteenGUI(obj)





