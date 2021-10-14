import numpy as np

from random import choice, randint

import pyglet
from pyglet.gl import Config, glLoadIdentity
from pyglet.window import key

from aggregate import aggregate
from walker import Walker

CELL_SIZE = 3
NUM_WALKERS = 1000


def print_intro():
    """prints the introduction"""
    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
    print("Diffusion Limited Aggregation (DLA) is a simulation of")
    print(
        "clusters by passsing particles through a meduim that jostles them as they move."
    )
    print("")


def water_options():
    """helper function that prints the options for the screen size"""
    print("Your screensize options are:")
    print("1: 1920x1080")
    print("2: [1280x720]")
    print("3: 854x480")
    print("4: 427x240")
    print("5: 256x144")


def create_aggregate():
    """creates the board based off user input. there is a default choice if input is bad"""
    water_options()

    # default behaviour
    try:
        inp = int(input())
    except Exception:
        inp = 2

    if inp == 1:
        return aggregate((1920 // CELL_SIZE, 1080 // CELL_SIZE), CELL_SIZE)
    if inp == 2:
        return aggregate((1280 // CELL_SIZE, 720 // CELL_SIZE), CELL_SIZE)
    if inp == 3:
        return aggregate((854 // CELL_SIZE, 480 // CELL_SIZE), CELL_SIZE)
    if inp == 4:
        return aggregate((427 // CELL_SIZE, 240 // CELL_SIZE), CELL_SIZE)
    if inp == 5:
        return aggregate((256 // CELL_SIZE, 144 // CELL_SIZE), CELL_SIZE)


def create_walker_list(shape, num):
    walkers = []

    for _ in range(num):
        walkers.append(
            Walker(
                position=(randint(0, shape[0]), randint(0, shape[1])),
                maxes=shape,
                cell_size=CELL_SIZE,
            )
        )
    return walkers


def debug_summary(ag: aggregate, w_list: "list[Walker]"):
    ag_count = 0
    lock_walk_count = 0

    for i in range(len(ag.arr)):
        for j in range(len(ag.arr[i])):
            if ag.arr[i][j]:
                ag_count += 1

    for walker in w_list:
        if walker.state:
            lock_walk_count += 1

    print(
        "aggregate had {} cells, thare were {} locked walkers".format(
            ag_count - 1, lock_walk_count
        )
    )


def get_window_config():
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
    print_intro()
    bo = create_aggregate()

    hit_box_draw = False

    walker_list = create_walker_list(bo.shape, NUM_WALKERS)

    w, h = bo.shape[0] * CELL_SIZE, bo.shape[1] * CELL_SIZE

    conf = get_window_config()
    window = pyglet.window.Window(
        width=w, height=h, config=conf, caption="DLA for bakas"
    )

    def update(dt):
        bo.update()
        for walker in walker_list:
            walker.update(bo.arr)

    pyglet.clock.schedule_interval(update, 0.0001)

    @window.event
    def on_draw():
        window.clear()
        glLoadIdentity()
        bo.draw(hit_box_draw)
        for walker in walker_list:
            walker.draw()

    @window.event
    def on_key_press(symbol, mods):
        if symbol == key.D:
            nonlocal hit_box_draw
            hit_box_draw = not hit_box_draw

        if symbol == key.Q:
            if hit_box_draw:
                debug_summary(bo, walker_list)
            pyglet.app.exit()

    pyglet.app.run()


if __name__ == "__main__":
    run()
