from random import randint

from pyglet.gl import glColor3f, glBegin, glEnd, glVertex2i, GL_QUADS


class Walker:
    def __init__(
        self,
        position: "tuple[int, int]",
        maxes: "tuple[int, int]",
        cell_size: int,
        state: bool = False,
    ):
        self.position = position
        self.state = state
        self.maxes = maxes
        self.cell_size = cell_size

    def walk(self):
        if not self.state:
            self.position[0] += randint(-1, 1)
            self.position[1] += randint(-1, 1)

            if self.position[0] < 0:
                self.position[0] = 0
            if self.position[1] < 0:
                self.position[1] = 0
            if self.position[0] > self.maxes[0]:
                self.position[0] = self.maxes[0]
            if self.position[1] > self.maxes[1]:
                self.position[1] = self.maxes[1]

    def search(self, bo: "list[list[bool]]"):
        x, y = self.position[0], self.position[1]

        if bo[x - 1][y - 1]:
            return True
        if bo[x][y - 1]:
            return True
        if bo[x + 1][y - 1]:
            return True
        if bo[x - 1][y]:
            return True
        if bo[x + 1][y]:
            return True
        if bo[x - 1][y + 1]:
            return True
        if bo[x][y + 1]:
            return True
        if bo[x + 1][y + 1]:
            return True

        return False

    def draw(self):

        cs = self.cell_size
        x, y = self.position[0] * cs, self.position[1] * cs

        glColor3f(0.7, 0.7, 0.7)

        glBegin(GL_QUADS)
        glVertex2i(x, y)
        glVertex2i(x + cs, y)
        glVertex2i(x + cs, y + cs)
        glVertex2i(x, y + cs)
        glEnd()

    def update(self, bo: "list[list[bool]]"):

        self.walk()

        if self.search(bo):
            self.state = False
            bo[self.position[0]][self.position[1]] = True
