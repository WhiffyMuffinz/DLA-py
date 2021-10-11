from ctypes import c_byte
from pyglet.gl import *
import numpy as np
from numba import jit
#import random

ANCHOR = np.array([0,0])
class Water:
    def __init__(self, cellSize, sizeX=256, sizeY=144, maxWalkers=1024):
        self.sizeX, self.sizeY = sizeX, sizeY #this is needed for when the window will be made 
        self.board = np.zeros((sizeX, sizeY), dtype=c_byte) #bytes can behave like booleans, but taking up less size
                                                                    #I think
        self.cellSize = cellSize
        self.maxWalkers = maxWalkers

        ANCHOR[0], ANCHOR[1] = (sizeX/2), (sizeY/2) #for now, the anchor will be at the center of the screen
        self.board[ANCHOR[0]][ANCHOR[1]] = 1
    
    def __repr__(self) -> str:
        out = "Water with width " + str(self.sizeX) + ", height " + str(self.sizeY) + ", and true values at:"

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 1:
                    strI, strJ = str(i), str(j)
                    out += '\n(' + strI + ',' + strJ + ')'
        
        return out

    def draw(self):
        for i in range(self.sizeX):
            for j in range(self.sizeY):
                if self.board[i][j] == 1:
                    #print('{},{}'.format((i * self.cellSize), (j * self.cellSize)))
                    glBegin(GL_QUADS)
                    glVertex2i(i * self.cellSize, j * self.cellSize)
                    glVertex2i(i * self.cellSize + self.cellSize, j * self.cellSize)
                    glVertex2i(i * self.cellSize + self.cellSize, j * self.cellSize + self.cellSize)
                    glVertex2i(i * self.cellSize, j * self.cellSize + self.cellSize)
                    glEnd()

    

