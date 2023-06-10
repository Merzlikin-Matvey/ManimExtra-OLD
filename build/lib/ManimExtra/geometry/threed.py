from manimlib import *
import numpy as np

def cube_vertices(cube: Cube):
    square_1 = cube[0]
    square_2 = cube[1]
    vertices = np.concatenate((square_1.get_vertices(),square_2.get_vertices()))
    return vertices

def cube_sides(cube: Cube):
    sides = (cube[0],cube[1],cube[2],cube[3],cube[4],cube[5])
    return sides

