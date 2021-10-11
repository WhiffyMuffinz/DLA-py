from random import randint
from numba import jit
from numba.core.types.scalars import Boolean
from pyglet.gl import *
from numpy import array

class Walker:
    def __init__(self, startX, startY, cellSize):
        '''makes a new walker with given positions
        
        Parameters:
        (int) startX: starting x position for the walker
        (int) startY: starting y position for the walker
        (int) cellSize: the size of the walker in pixels'''
        self.X, self.Y = startX, startY
        self.cellSize = cellSize

    def __repr__(self) :
        return 'Walker with location ({}, {}) and size {}'.format(self.X, self.Y, self.cellSize)

    def walk(self):
        '''moves the walker in a random direction one unit'''
        dirX, dirY = randint(-1,1), randint(-1,1)
        self.X += dirX 
        self.Y += dirY

    
    def draw(self):
        '''used in the visualization loop to make the cells visible'''
        glBegin(GL_QUADS)
        glVertex2i(self.X, self.Y)
        glVertex2i(self.X + self.cellSize, self.Y)
        glVertex2i(self.X + self.cellSize, self.Y + self.cellSize)
        glVertex2i(self.X, self.Y + self.cellSize)
        glEnd()

    def newPos(self, arr):
        self.X, self.Y = randint(1, arr.size-2), randint(1, arr[0].size-2)
    
    
    def search(self, arr) -> Boolean:
        '''searches the walker's neighbourhood(defined as the space a king can move on the chessboard) for a part of the seed
        
        can be optimized by omiting what was searched by the walker in the last step
        and by giving the seed a hitbox that the walker can skip if it is outside of

        Parameters:
        (2d numpy array) arr: array to search
        
        Returns:
        (bool) if the seed is in the walker's neighbourhood and the walker attached to it'''
        
        dims = arr.shape
        if self.X >= dims[0]-2 or self.X <= 1 or self.Y >= dims[1]-2 or self.Y <= 1:
            self.newPos(arr)
            return False 
        
        
        for i in range(self.X-1, self.X+2):
            for j in range(self.Y-1, self.Y+2):
                if(arr[int(i)][int(j)] == 1):
                    arr[self.X][self.Y] = 1
                    self.newPos(arr)
                    return True
        return False
        
        
        '''x, y = arr.size, arr[0].size
        if (self.X >= x-2) or (self.X <= 1) or (self.Y >= y-2) or (self.Y <= 1):
            self.newPos(arr)
            print('reset to {},{}'.format(self.X, self.Y)) 
            return False 

        print('x:{}, y:{}'.format(self.X, self.Y))

        if arr[int(self.X - 1)][int(self.Y + 1)] == 1:
            arr[int(self.X)][int(self.Y)] = 1
            return True
        if arr[int(self.X)][int(self.Y + 1)] == 1:
            arr[int(self.X)][int(self.Y)] = 1
            return True
        if arr[int(self.X + 1)][int(self.Y + 1)] == 1:
            arr[int(self.X)][int(self.Y)] = 1
            return True
        if arr[int(self.X - 1)][int(self.Y)] == 1:
            arr[int(self.X)][int(self.Y)] = 1
            return True
        if arr[int(self.X + 1)][int(self.Y)] == 1:
            arr[int(self.X)][int(self.Y)] = 1
            return True
        if arr[int(self.X - 1)][int(self.Y - 1)] == 1:
            arr[int(self.X)][int(self.Y)] = 1
            return True
        if arr[int(self.X)][int(self.Y - 1)] == 1:
            arr[int(self.X)][int(self.Y)] = 1
            return True
        if arr[int(self.X + 1)][int(self.Y - 1)] == 1:
            arr[int(self.X)][int(self.Y)] = 1
            return True
        
        return False''' 

    
    def update(self, arr):
        '''updates the walker's position and if the seed is in the neighborhood,
        alters its address on the main array to reflect its addition to the aggregate
        
        Params:
        arr: array that is uesd in the search function (see 'search.__doc__' for more)
        
        Returns:
        none'''
        
        while not(self.search(arr)):
            self.walk()

        self.newPos(arr)
