from walker import Walker
from water import Water
import tkinter as tk
import math

def owo(uwu):
    '''Squares an int

    Parameters:a
    uwu (int): an integer to be squared

    Returns:
    uwu squared'''
    
    return math.pow(uwu, 2)


def main():
    w = Water(sizeX=11, sizeY=11, cellSize=1)
    wal = Walker(0,0,5)
    w.board[0][0] = 1
    print(w.__repr__())
    print(w.board)

main()