from pyglet.gl.base import Config
from walker import Walker
from water import Water
from numpy import array, zeros
from ctypes import c_byte
from simulation import getWindowConfig
import pyglet
from pyglet.gl import *
from random import randint, choice

w = Water(16, 9, 150)

w.board[0][0] = 1
w.board[8][4] = 1

w.update()
conf = getWindowConfig()

window = pyglet.window.Window(fullscreen = True, config = conf)

@window.event
def on_draw():
    window.clear()
    glLoadIdentity()
    w.draw(True)

pyglet.app.run()