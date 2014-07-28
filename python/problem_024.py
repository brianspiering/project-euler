#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Solution to "Lexicographic permutations", Problem 24

http://projecteuler.net/problem=24

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

"""

from __future__ import print_function
import itertools

digits = range(3) #  range(3) | range(10)

# {n_elements (place_number, place_name}
perm_picker = { 3: (6, 'sixth'),
                10: (1000000, "millionth")}

def calc_something(digits):
    return "'In Progress'"

if __name__ == "__main__":
    print("The {} lexicographic permutation of the digits ".format(perm_picker[len(digits)][1]), end="")
    for i, digit in enumerate(digits):
        if i < len(digits)-2:
            print("{}".format(digit), end=", ")
        elif i == len(digits)-2:
            print("{}".format(digit), end=", and ")
        else:
            print("{}".format(digit), end=" ")
    print("is {}.".format(calc_something(digits)))