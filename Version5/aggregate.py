import numpy as np

from pyglet.gl import glBegin, glEnd, glVertex2i, glColor3f, GL_LINE_LOOP, GL_QUADS


class aggregate:
    def __init__(self, shape: "tuple[int, int]", cell_size):
        self.arr = np.zeros(shape, bool)
        self.cell_size = cell_size
        self.shape = shape
        self.anchor = [shape[0] // 2, shape[1] // 2]

        self.min_x, self.min_y, self.max_x, self.max_y = (
            self.anchor[0],
            self.anchor[1],
            self.anchor[0],
            self.anchor[1],
        )

        x, y = self.anchor[0], self.anchor[1]
        self.arr[x][y] = True

    def update(self):
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                if self.arr[i][j]:
                    self.min_x = min(i, self.min_x)
                    self.min_y = min(j, self.min_y)
                    self.max_x = max(i, self.max_x)
                    self.max_y = max(j, self.max_y)

    def draw(self, draw_hitbox: bool = False):
        cs = self.cell_size

        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                if self.arr[i][j]:
                    glColor3f(0.7, 0.7, 0.7)
                    glBegin(GL_QUADS)
                    glVertex2i(i * cs, j * cs)
                    glVertex2i(i * cs + cs, j * cs)
                    glVertex2i(i * cs + cs, j * cs + cs)
                    glVertex2i(i * cs, j * cs + cs)
                    glEnd()

        if draw_hitbox:
            glColor3f(0, 1, 0)
            glBegin(GL_LINE_LOOP)
            glVertex2i(cs * self.min_x, cs * self.min_y)
            glVertex2i(cs * self.max_x + cs, cs * self.min_y)
            glVertex2i(cs * self.max_x + cs, cs * self.max_y + cs)
            glVertex2i(cs * self.min_x, cs * self.max_y + cs)
            glEnd()
