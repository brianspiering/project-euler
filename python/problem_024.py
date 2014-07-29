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

# {range_argument: {place_number, place_name}}
perm_picker = { 3: (6, 'sixth'),
                10: (1000000, "millionth")}

range_argument = 10 # 3 = demo; 10

def find_permutation(range_argument, place):
    "Find the specific (place) lexicographic permutation for give range argument."
    perm_tuple = list(itertools.permutations(xrange(range_argument)))[place-1]
    perm_string = "".join([str(n) for n in perm_tuple])
    return perm_string

if __name__ == "__main__":
    digits = range(range_argument)
    print("The {} lexicographic permutation of the digits ".format(perm_picker[range_argument][1], end=""))
    for digit in digits[:-2]:
        print("{}".format(digit), end=", ")
    print("{}".format(digits[-2]), end=", and ")
    print("{}".format(digits[-1]), end=" ")
    print("is {}.".format(find_permutation(range_argument, perm_picker[range_argument][0])))