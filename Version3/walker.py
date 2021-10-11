#walker.py
#Implements the walkers for DLA
#
#Version 3 -Daniel Benes-Magana 5/22/21


#from pyglet.gl import glBegin,GL_QUADS,glColor3f,glVertex2i
from random import randint


class Walker:
    def __init__(self, X, Y, cellSize):

        self.x, self.y = X, Y
        self.cellSize = cellSize

    def __repr__(self) -> str:
        return 'Walker with location ({}, {}) and size {}'.format(self.x, self.y, self.cellSize)
    
    def walk(self):
        '''moves the walker one unit in the 3x3 square surrounding it'''
        self.x += randint(-1, 1)
        self.y += randint(-1,1)

    def newPos(self, wat):
        '''gives the walker a new position on the edges of the board within a boundary 
        Params:
        (Water) wat: the Water object that this walker is attached to
        (int) offset: the offset from the edges the walker can "spawn" in'''

        #to avoid errors in the search() method, I keep a border one away from the edges
        self.x, self.y = randint(1, wat.sizeX-2), randint(1, wat.sizeY-2)

    def checkOut(self, wat):
        '''checks if the walker is outside the acceptable boundary
        Params:
        (Water) wat: the Water object that the walker is attached to'''

        if self.x >= wat.sizeX-1:
            return False
        if self.y >= wat.sizeY-1:
            return False
        if self.x < 1:
            return False
        if self.y < 1:
            return False
        return True

    def search(self, wat, minX, maxX, minY, maxY) -> bool:
        '''Searches walker's neighbourhood for the structure
        Params:
        (Water) wat: the water object that will be accessed
        (int) minX: bounding coordinate for the hitbox
        (int) maxX: bounding coordinate for the hitbox
        (int) minY: bounding coordinate for the hitbox
        (int) maxY: bounding coordinate for the hitbox'''
        
        if not self.checkOut(wat):
            self.newPos(wat)
            return False

        if (self.x <= minX and self.x >= maxX and self.y <= minY and self.y >= maxY):
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
            
        #print('SKIPPED!')
        return False

    def update(self, wat, minX, maxX, minY, maxY):
        '''updates the walker position and the array

           Params:
           (Water) wat: array that the walker will reference
           (int) hbX: the x coordinate of the hitbox's top left corner
           (int) hbY: the y coordinate
           (int) sizeX: the extension of the hitbox from the coordinate
           (int) sizeY: the extension of the hitbox from the coordinate'''

        while not(self.search(wat, minX, maxX, minY, maxY)):
            self.walk()
        #print("I am here")
        self.newPos(wat)