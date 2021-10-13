#water.py
#The board the walkers walk on. Also has a method to draw itself.  
#
#Version 4 -Daniel Benes-Magana 10/13/21

from numpy import array, zeros
from ctypes import c_byte
from pyglet.gl import glBegin, GL_QUADS, glVertex2i, glEnd, glColor3f, GL_POINTS
from pyglet.gl.gl import GL_LINE_LOOP


ANCHOR = array([0,0])

class Water:
    def __init__(self, size_x, size_y, cell_size):
        self.size_x, self.size_y = size_x, size_y
        self.board = zeros((size_x, size_y), dtype=c_byte)
        self.cell_size = cell_size

        ANCHOR[0], ANCHOR[1] = (size_x/2),(size_y/2)
        self.board[ANCHOR[0]][ANCHOR[1]] = 1

        self.min_x, self.min_y, self.max_x, self.max_y = ANCHOR[0], ANCHOR[1], ANCHOR[0], ANCHOR[1]

        self.center = ANCHOR[0], ANCHOR[1]
        

    def __repr__ (self) -> str:
        out = "Water with width {}, height {}, a hitbox bounded by ({}, {}) and ({},{}) true values at:".format(self.board.size, self.board[0].size, self.max_x, self.max_y, self.min_x, self.min_y)

        for i in range(self.size_x):
            for j in range(self.size_y):
                if(self.board[i][j]) == 1:
                    out += '\n({},{})'.format(i,j)
        
        return out
    
    def update(self):
        '''Looks for the largest and smallest true values on each axis and updates the hitBox attributes'''
        for i in range(self.size_x):
            for j in range(self.size_y):
                if self.board[i][j] == 1:
                    self.min_x = min(i, self.min_x)
                    self.min_y = min(j, self.min_y)
                    self.max_x = max(i, self.max_x)
                    self.max_y = max(j, self.max_y)


    def draw(self, draw_hitbox = False):
        '''draws the structure in the "water"
        Params:
        (bool) draw_hitbox: whether or not to draw the hitbox'''
        cs = self.cell_size

        if cs != 1:
            for i in range(self.size_x):
                for j in range(self.size_y):
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
        
        else:
            for i in range(self.size_x):
                for j in range(self.size_y):
                    if self.board[i][j] == 1:
                        glColor3f(0.7,0.7,0.7)
                        glBegin(GL_POINTS)
                        glVertex2i(i*cs, j*cs)
                        glEnd()


        if draw_hitbox:
            glColor3f(0,1,0)
            glBegin(GL_LINE_LOOP)
            glVertex2i(cs * self.min_x, cs * self.min_y)
            glVertex2i(cs * self.max_x + cs, cs * self.min_y)
            glVertex2i(cs * self.max_x + cs, cs * self.max_y + cs)
            glVertex2i(cs * self.min_x, cs * self.max_y + cs)
            glEnd()