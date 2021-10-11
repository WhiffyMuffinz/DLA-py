import numpy as np
from random import randint, choice
from pyglet.gl import *
from pyglet.window import key

from water import Water
from walker import Walker

CELL_SIZE = 5

def printIntro():
    '''prints the introduction'''
    print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
    print('Diffusion Limited Aggregation (DLA) is a simulation of')
    print('clusters by passsing particles through a meduim that jostles them as they move.')
    print("")

def waterOptions():
    '''helper function that prints the options for the screen size'''
    print('Your screensize options are:')
    print('1: 1920x1080')
    print('2: [1280x720]')
    print('3: 854x480')
    print('4: 427x240')
    print('5: 256x144')

def createWater():
    '''creates the board based off user input. there is a default choice if input is bad'''
    waterOptions()
    
    try:
        inp = int(input())
    except:
        inp = 2
    
    if inp == 1:
        return Water(1920//CELL_SIZE, 1080//CELL_SIZE, CELL_SIZE)
    if inp == 2:
        return Water(1280//CELL_SIZE, 720//CELL_SIZE, CELL_SIZE)
    if inp == 3:
        return Water(854//CELL_SIZE, 480//CELL_SIZE, CELL_SIZE)
    if inp == 4:
        return Water(427//CELL_SIZE, 240//CELL_SIZE, CELL_SIZE)
    if inp == 5:
        return Water(256//CELL_SIZE, 144//CELL_SIZE, CELL_SIZE)

def betterRandom(smallLower, smallUpper, bigLower, bigUpper):
    '''generates random numbers between two ranges
    Params:
       (int) smallLower: lower bound of the smaller range 
       (int) smallUpper: upper bound of the smaller range
       (int) bigLower:   lower bound of the bigger range
       (int) bigUpper:   upper bound of the bigger range
    '''
    r=choice([(smallLower, smallUpper),(bigLower, bigUpper)])
    return(randint(*r))


def createWalkerList(width, height, xOff = 10, yOff = 10, num = 10):
    '''creates a list of walkers that will traverse the board
    Params:
    (int) width:  width of the board
    (int) height: height of the board
    (int) xOff:   offset inward from the size of the board where the walkers will spawn
    (int) yOff:   offset inward from the size of the board where the walkers will spawn'''
    walkers = []

    for i in range(num):
        walkers.append(Walker(betterRandom(0, xOff, width-xOff, width), betterRandom(0, yOff, height-yOff, height), CELL_SIZE))
    return walkers

def getWindowConfig():
    '''creates an openGL context'''
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
    '''runs the simulation'''
    #making the objs
    printIntro()
    bo = createWater()
    #print(bo.__repr__())
    walkerList = createWalkerList(bo.sizeX, bo.sizeY, CELL_SIZE)
    w, h = bo.sizeX * CELL_SIZE, bo.sizeY * CELL_SIZE
    
    #graphics
    conf = getWindowConfig()
    window = pyglet.window.Window(width = w, height = h, config = conf, caption = 'DLA. By bakas, for bakas')

    #update the objects
    def update(dt):
        bo.update()
        for walker in walkerList:
            walker.update(bo, bo.minX, bo.maxX, bo.minY, bo.maxY)

    pyglet.clock.schedule_interval(update, 0.0001)   
    #pyglet.clock.schedule(update)

    #display them to the user
    @window.event
    def on_draw():
        window.clear()
        glLoadIdentity()
        bo.draw(True)

    pyglet.app.run()