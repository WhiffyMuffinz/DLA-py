import numpy as np, random, pyglet
from pyglet.libs.win32.constants import NULL
from numba import jit
from water import Water
from walker import Walker
from pyglet.gl import *
from pyglet.window import key


CELL_SIZE = 3

def printIntro():
    out = "\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n"
    out += "\nDiffusion Limited Aggregation(DLA) is a simulation of the formation of "
    out += "clusters by passing particles through a medium that jostles them as they move. \n"
    print(out)

def createWater():
    '''prompts the user for the size screen they would like, and makes a 2d array of that size/CELL_SIZE, which is a field'''
    width = NULL
    flag = False
    while not flag:
        try:
            width = int(input('What width window would you like? '))
            flag = True
        except:
            print('your input: '+ width + ' was bad and you shoud feel bad. Put something better')
    #print('w:', width)
    height = int(9/16 * width)
    #print('h:', height)
    return Water(CELL_SIZE, abs(width//CELL_SIZE), abs(height//CELL_SIZE))



def createWalkerList(width, height, num = 10):
    walkers = []

    for i in range(num):
        walkers.append(Walker(random.randint(0, width), random.randint(0,height), cellSize=CELL_SIZE))
    return walkers


def getWindowConfig():
    disp = pyglet.canvas.get_display()
    screen = disp.get_default_screen()

    template = Config(double_buffer=True, samples=4, sample_buffers=1)
    try:
        config = screen.get_best_config(template)
    except pyglet.window.NoSuchConfigException:
        template = Config()
        config = screen.get_best_config(template)
    return config



def run():
    printIntro()
    bo = createWater()
    walkerList = createWalkerList(bo.sizeX, bo.sizeY)
    w, h = bo.sizeX * CELL_SIZE, bo.sizeY*CELL_SIZE
    
    conf = getWindowConfig()
    window = pyglet.window.Window(width=w, height=h, config=conf, caption='DLA')

    #glEnable(GL_BLEND)
    #glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    
    def update(dt):
        for walker in walkerList:
            walker.update(bo.board)

    pyglet.clock.schedule(update)

    @window.event
    def on_draw():
        window.clear()
        glLoadIdentity()
        bo.draw()

        
    
    pyglet.app.run()