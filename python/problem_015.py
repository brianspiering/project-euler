#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Solution to "Lattice paths", aka Problem 15

http://projecteuler.net/problem=15

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

[SEE https://projecteuler.net/project/images/p015.gif]

How many such routes are there through a 20×20 grid?
"""

from math import factorial

grid_size = 20 # 2 | 20

def cal_n_routes_in_a_grid(grid_size):
    "Assuming grid is square, find the central binomial coefficient."
    return factorial(2*grid_size)/(factorial(grid_size)*factorial(grid_size))

if __name__ == "__main__":
    print("The number of routes through a {0}x{1} grid is {2}."
            .format(grid_size, grid_size, cal_n_routes_in_a_grid(grid_size)))