"""
Clone of 2048 game.
"""
import random

#import poc_2048_gui

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    """
    This is for combinding the number in the array from right to left 2048
    """
    new_line = list(line)
    answer_line = []
    for zero_check in line:
        if zero_check == 0:
            new_line.remove(0)
    value = 0
    while value <= len(new_line):
        if value == len(new_line)-1:
            answer_line.append(new_line[value])
            break
        if value == len(new_line):
                break
        elif new_line[value] == new_line[value+1]:
            answer_line.append(new_line[value]*2)
            value += 2
        else:
            answer_line.append(new_line[value])
            value+=1

    for dummy_zero in range(len(line) - len(answer_line)):
        answer_line.append(0)
    #print answer_line
    return answer_line

class TwentyFortyEight:
    """
    Class to run the game logic.
    """
    def __init__(self, grid_height, grid_width):
        # replace with your code
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # replace with your code
        self.board =[[]]
        for dummy_width in range(self.get_grid_width()):
            self.board[0].append(0)
        for dummy_height in range(self.get_grid_height()-1):
            self.board.append(list(self.board[0])) 
        self.new_tile()
        self.new_tile()
       # self.board = [ [0,0,0,0] , [0,0,0,0] , [0,0,0,0] , [0,0,0,0]]

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        #return str(self.board[0]) + "\n"+ str(self.board[1]) + "\n" + str(self.board[2])+ "\n" + str(self.board[3])
        return str(self.board)

    def get_grid_height(self):
        """
        Get height of the board 
        """
        return self.grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.grid_width

    def move(self, direction):
         
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        self.does_board_change=[]
        

        #UP
        if direction == 1:
            for dummy_rows_needed in range(self.get_grid_height()):
                self.does_board_change.append([])
            for col_1 in range(self.get_grid_width()):
                col_line = []
                for row in range(self.get_grid_height()):
                    col_line.append(self.board[row][col_1])
                merged = merge(col_line)
                for col_2 in range(self.get_grid_height()):
                    self.does_board_change[col_2].append(merged[col_2])


        #DOWN
        if direction == 2:
            for dummy_rows_needed in range(self.get_grid_height()):
                self.does_board_change.append([])
            for col_1 in range(self.get_grid_width()):
                col_line = []
                for row in range(self.get_grid_height()):
                    col_line.append(self.board[row][col_1])
                col_line.reverse()
                merged = merge(col_line)
                merged.reverse()
                for col_2 in range(self.get_grid_height()):
                    self.does_board_change[col_2].append(merged[col_2])            

        #LEFT
        if direction == 3:
            for row in range(self.get_grid_height()):
                self.does_board_change.append(merge(self.board[row]))
        #RIGHT
        if direction == 4:
            for row in range(self.get_grid_height()):
                right_row = list(self.board[row])
                right_row.reverse()
                merged = merge(right_row)
                merged.reverse()
                self.does_board_change.append(merged)

        
        #test if tile should be added
        if self.does_board_change != self.board:
            self.board= self.does_board_change
            self.new_tile()
            print('new tile was created')
        print (self.board)
        pass

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        location_value = 1
        while location_value != 0:
            height = random.randint(0,self.get_grid_height()-1)
            width = random.randint(0,self.get_grid_width()-1)
            location_value = self.board[height][width]
            if self.board[height][width] == 0:
                self.board[height][width]=random.choice([2,2,2,2,2,2,2,2,2,4])
                break        

    def set_tile(self, row, col, value):
        self.board[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self.board[row][col]

#Pygame tools for VS testing below
import pygame

# initialising pygame
pygame.init()

window_width = 600
window_height = 700


window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("2048 test")
test = TwentyFortyEight(3,4)
print (test)
running = True
while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if keys[pygame.K_ESCAPE]:
            running = False
        elif keys[pygame.K_r]:
            print('Reset')
            test.reset()
            print (test)
        elif keys[pygame.K_LEFT]:
            print('LEFT')
            test.move(3)
        elif keys[pygame.K_RIGHT]:
            print('RIGHT')
            test.move(4)
        elif keys[pygame.K_UP]:
            print('UP')
            test.move(1)
        elif keys[pygame.K_DOWN]:
            print('DOWN')
            test.move(2)
        #else:
        #    print(event)
            
pygame.quit()

#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
