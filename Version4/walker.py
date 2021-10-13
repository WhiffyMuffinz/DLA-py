#walker.py
#Implements the walkers for DLA
#
#Version 4 -Daniel Benes-Magana 10/13/21

from random import randint


class Walker:
    def __init__(self, x, y, cell_size):

        self.x, self.y = x, y
        self.cell_size = cell_size

    def __repr__(self) -> str:
        return 'Walker with location ({}, {}) and size {}'.format(self.x, self.y, self.cellSize)
    
    def walk(self, board):
        '''determines where the center of the board is and walks toward it with a chance of deviating'''
        center = board.center

        if self.x > center[0]:
            self.x = self.x - 1
        elif self.x < center[0]:
            self.x = self.x + 1
        
        if self.y > center[1]:
            self.y = self.y - 1
        elif self.y < center[1]:
            self.y = self.y + 1
        
        self.x += randint(-1, 1)
        self.y += randint(-1, 1)

    def new_pos(self, wat):
        '''gives the walker a new position on the edges of the board within a boundary 
        Params:
        (Water) wat: the Water object that this walker is attached to
        (int) offset: the offset from the edges the walker can "spawn" in'''

        #to avoid errors in the search() method, I keep a border one away from the edges
        self.x, self.y = randint(1, wat.size_x-2), randint(1, wat.size_y-2)

    def check_out(self, wat):
        '''checks if the walker is outside the acceptable boundary
        Params:
        (Water) wat: the Water object that the walker is attached to'''

        if self.x >= wat.size_x-1:
            return False
        if self.y >= wat.size_y-1:
            return False
        if self.x < 1:
            return False
        if self.y < 1:
            return False
        return True

    def search(self, wat, min_x, max_x, min_y, max_y) -> bool:
        '''Searches walker's neighbourhood for the structure
        Params:
        (Water) wat: the water object that will be accessed
        (int) min_x: bounding coordinate for the hitbox
        (int) max_x: bounding coordinate for the hitbox
        (int) min_y: bounding coordinate for the hitbox
        (int) max_y: bounding coordinate for the hitbox'''
        
        if not self.check_out(wat):
            self.new_pos(wat)
            return False

        if (self.x <= min_x and self.x >= max_x and self.y <= min_y and self.y >= max_y):
            return False
        
        if(wat.board[self.x - 1][self.y + 1] == 1):
            wat.board[self.x][self.y] = 1
            return True
        if(wat.board[self.x][self.y + 1] == 1):
            wat.board[self.x][self.y] = 1
            return True
        if(wat.board[self.x + 1][self.y + 1] == 1):
            wat.board[self.x][self.y] = 1
            return True
        if(wat.board[self.x - 1][self.y] == 1):
            wat.board[self.x][self.y] = 1
            return True
        if(wat.board[self.x + 1][self.y] == 1):
            wat.board[self.x][self.y] = 1
            return True
        if(wat.board[self.x - 1][self.y - 1] == 1):
            wat.board[self.x][self.y] = 1
            return True
        if(wat.board[self.x - 1][self.y] == 1):
            wat.board[self.x][self.y] = 1
            return True
        if(wat.board[self.x - 1][self.y + 1] == 1):
            wat.board[self.x][self.y] = 1
            return True
            
        return False

    def update(self, wat, min_x, max_x, min_y, max_y):
        '''updates the walker position and the array

           Params:
           (Water) wat: array that the walker will reference
           (int) hbX: the x coordinate of the hitbox's top left corner
           (int) hbY: the y coordinate
           (int) size_x: the extension of the hitbox from the coordinate
           (int) size_y: the extension of the hitbox from the coordinate'''

        while not(self.search(wat, min_x, max_x, min_y, max_y)):
            self.walk(wat)
        #print("I am here")
        self.new_pos(wat)