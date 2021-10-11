from numpy import array, zeros
from ctypes import c_byte
from pyglet.gl import glBegin, GL_QUADS, glVertex2i, glEnd, glColor3f
from pyglet.gl.gl import GL_LINE_LOOP
from numba import jit


ANCHOR = array([0,0])
class Water:
    def __init__(self, sizeX, sizeY, cellSize):
        self.sizeX, self.sizeY = sizeX, sizeY
        self.board = zeros((sizeX, sizeY), dtype=c_byte)
        self.cellSize = cellSize

        ANCHOR[0], ANCHOR[1] = (sizeX/2),(sizeY/2)
        self.board[ANCHOR[0]][ANCHOR[1]] = 1

        self.minX, self.minY, self.maxX, self.maxY = ANCHOR[0], ANCHOR[1], ANCHOR[0], ANCHOR[1]
        

    def __repr__ (self) -> str:
        out = "Water with width {}, height {}, a hitbox bounded by ({}, {}) and ({},{}) true values at:".format(self.board.size, self.board[0].size, self.maxX, self.maxY, self.minX, self.minY)

        for i in range(self.sizeX):
            for j in range(self.sizeY):
                if(self.board[i][j]) == 1:
                    out += '\n({},{})'.format(i,j)
        
        return out
    
    @jit(forceobj=True)
    def update(self):
        '''Looks for the largest and smallest true values on each axis and updates the hitBox attributes'''
        for i in range(self.sizeX):
            for j in range(self.sizeY):
                if self.board[i][j] == 1:
                    self.minX = min(i, self.minX)
                    self.minY = min(j, self.minY)
                    self.maxX = max(i, self.maxX)
                    self.maxY = max(j, self.maxY)


    def draw(self, drawHitbox = False):
        '''draws the structure in the "water"
        Params:
        (bool) drawHitbox: whether or not to draw the hitbox'''
        cs = self.cellSize
        for i in range(self.sizeX):
            for j in range(self.sizeY):
                if self.board[i][j] == 1:
                    glColor3f(0.7,0.7,0.7)
                    glBegin(GL_QUADS)
                    glVertex2i(i*cs, j*cs)
                    glVertex2i(i*cs+cs, j*cs)
                    glVertex2i(i*cs+cs,j*cs+cs)
                    glVertex2i(i*cs, j*cs+cs)
                    glEnd()
                    glColor3f(0,0,0)
                    glBegin(GL_LINE_LOOP)
                    glVertex2i(i*cs, j*cs)
                    glVertex2i(i*cs+cs, j*cs)
                    glVertex2i(i*cs+cs,j*cs+cs)
                    glVertex2i(i*cs, j*cs+cs)
                    glEnd()

        if drawHitbox:
            glColor3f(0,1,0)
            glBegin(GL_LINE_LOOP)
            glVertex2i(cs * self.minX, cs * self.minY)
            glVertex2i(cs * self.maxX + cs, cs * self.minY)
            glVertex2i(cs * self.maxX + cs, cs * self.maxY + cs)
            glVertex2i(cs * self.minX, cs * self.maxY + cs)
            glEnd()