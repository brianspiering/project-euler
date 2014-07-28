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

digits = range(1,10)#  [3, 1, 2, 4] | range(1,10)

def calc_something(digits):
    return "'In Progress'"

if __name__ == "__main__":
    print("The millionth lexicographic permutation of the digits ", end="")
    for i, digit in enumerate(digits):
        if i < len(digits)-2:
            print("{}".format(digit), end=", ")
        elif i == len(digits)-2:
            print("{}".format(digit), end=", and ")
        else:
            print("{}".format(digit), end=" ")
    print("is {}.".format(calc_something(digits)))