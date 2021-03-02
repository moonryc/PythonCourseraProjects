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

    def fetch_tile(self, target_row,target_col,target_pos):
        """
        Moves the target tile from where it is to its correct stop
        """

        #finds the distance from where the target is to where the target belongs
        distance_to_target = (target_pos[0]-target_row, target_pos[1]-target_col)
        delta_x = distance_to_target[1]
        delta_y = distance_to_target[0]
        print 'target pos', target_pos
        print 'target_row, target_col: ', target_row,',',target_col
        print 'distance_to_target: ', distance_to_target
        shift_x = abs(delta_x) -1
        shift_y = abs(delta_y) -1

        vert_move = abs(delta_y) * 'u'
        if delta_y < 0:
           vert_return = (shift_y * 'lddru') + 'ld'

        # if target is left of 0
        if delta_x < 0:
            hori_move = abs(delta_x) * 'l'

            hori_shift = shift_x * 'urrdl'


        #if target is right of 0
        else:
            hori_move = delta_x * 'r'

        

        final_move = hori_move + vert_move + vert_return + hori_shift
        print final_move
 
        #self.update_puzzle(final_move)
        return final_move

    
    ##################################################################

    def this_cell_zero(self, target_row, target_col):
        if self.get_number(target_row,target_col) != 0:
            print "0 is not in the correct spot, correct spot is: " + str((target_row, target_col))
            return False
        else:
            return True
    def lower_cells(self, target_row):
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

        if self.this_cell_zero(target_row,target_col) and self.lower_cells(target_row) and self.row_correct(target_row,target_col):
                    return True
        return False

        print self.this_cell_zero(target_row,target_col)
        print self.lower_cells(target_row)
        print self.row_correct(target_row,target_col)

        """
        #Makes sure  Tile is positioned at (i,j)
        if self.get_number(target_row,target_col) != 0:
            print "0 is not in: " + str((target_row, target_col))
            return False

        #tests rows below (i,j)
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
            
        #Makes sure all tiles in rows greater than j
        target_col_test=target_col+1
        while target_col_test < self.get_width()-1:
            if self.current_position(target_row,target_col_test) != (target_row,target_col_test):
                print 'Tile  in row i greater than j is not correct'
                return False
            target_col_test += 1
        """
        return True

    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string

        will solve for position j>0 and i>1
        """
        assert self.lower_row_invariant(target_row,target_col)
        target_pos = self.current_position(target_row,target_col)
        final_move = self.fetch_tile(target_row,target_col,target_pos)
        self.update_puzzle(final_move)
        #assert self.lower_row_invariant(target_row,target_col-1)        

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
        assert self.row1_invariant(1)
        if self.get_number(0,0) == 1:
            final_move = 'ul'
        elif self.get_number(0,0) == 2:
           final_move ='lu'
        elif self.get_number(0,0) == 3:
            final_move = 'uldru'

        self.update_puzzle(final_move)
        return final_move

    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """
        solution_string= self.move_tile(self.get_width()-1,self.get_height()-1)
        solution_string += self.solve_interior_tile(self.get_width()-1,self.get_height()-1)
        #for row in range(self.get_height()-1,1,-1):
        #    for col in range(self.get_width()-1,0,-1):
        #        solution_string+= self.solve_interior_tile(row,col)
        #    self.solve_col0_tile(row)
        #for col in range(self.get_width() -1, 1, -1):
        #    solution_string += self.solve_row1_tile(col)
        #    solution_string  += self.solve_col0_tile(col)
        #solution_string += self.solve_2x2()
        #print solution_string
        return solution_string


            
#obj = Puzzle(4,4, [[5,4,1,3],[8,0,2,7],[10,13,6,11],[9,12,14,15]])
obj = Puzzle(4,4, [[5,4,1,3],[8,15,2,7],[10,13,6,11],[9,12,14,0]])




poc_fifteen_gui.FifteenGUI(obj)





