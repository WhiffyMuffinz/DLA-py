#Simulation.py
#All the code that runs the algorithm.
#
#Version 4 -Daniel Benes-Magana 10/13/21

import numpy as np
from random import randint, choice
import pyglet
from pyglet.gl import Config, glLoadIdentity
from pyglet.window import key

from water import Water
from walker import Walker

CELL_SIZE = 1

def print_intro():
    '''prints the introduction'''
    print('-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-')
    print('Diffusion Limited Aggregation (DLA) is a simulation of')
    print('clusters by passsing particles through a meduim that jostles them as they move.')
    print("")

def water_options():
    '''helper function that prints the options for the screen size'''
    print('Your screensize options are:')
    print('1: 1920x1080')
    print('2: [1280x720]')
    print('3: 854x480')
    print('4: 427x240')
    print('5: 256x144')

def create_water():
    '''creates the board based off user input. there is a default choice if input is bad'''
    water_options()
    
    #default behaviour
    try:
        inp = int(input())
    except Exception:
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

def better_random(small_lower, small_upper, big_lower, big_upper):
    '''generates random numbers between two ranges
    Params:
       (int) small_lower: lower bound of the smaller range 
       (int) small_upper: upper bound of the smaller range
       (int) big_lower:   lower bound of the bigger range
       (int) big_upper:   upper bound of the bigger range
    '''
    r=choice([(small_lower, small_upper),(big_lower, big_upper)])
    return(randint(*r))


def create_walker_list(width, height, num = 10):
    '''creates a list of walkers that will traverse the board
    Params:
    (int) width:  width of the board
    (int) height: height of the board'''
    walkers = []

    for _ in range(num):
        walkers.append(Walker(randint(0, width), randint(0, height), CELL_SIZE))
    return walkers

def get_window_config():
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
    print_intro()
    bo = create_water()
    #print(bo.__repr__())
    hit_box_draw = False

    walker_list = create_walker_list(bo.sizeX, bo.sizeY, CELL_SIZE)
    w, h = bo.sizeX * CELL_SIZE, bo.sizeY * CELL_SIZE
    
    #graphics
    conf = get_window_config()
    window = pyglet.window.Window(width = w, height = h, config = conf, caption = 'DLA. By bakas, for bakas')

    #update the objects
    def update(dt):
        bo.update()
        for walker in walker_list:
            walker.update(bo, bo.minX, bo.maxX, bo.minY, bo.maxY)

    pyglet.clock.schedule_interval(update, 0.0001)   
                                            #^this is to make the clock update faster

    #display them to the user
    @window.event
    def on_draw():
        window.clear()
        glLoadIdentity()
        bo.draw(hit_box_draw)

    @window.event
    def on_key_press(symbol, mods):
        
        if symbol == key.D:
            nonlocal hit_box_draw
            hit_box_draw = not hit_box_draw

        if symbol == key.Q:
            pyglet.app.exit()
            
    pyglet.app.run()