#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Solution to "Arranged probability", aka Problem 100

http://projecteuler.net/problem=100

If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2. The next such arrangement, for which there is exactly 50 percent chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 10^12 = 1,000,000,000,000 discs in total, determine the number of blue discs that the box would contain.
"""

from __future__ import division

box = { 'blue': 15,
        'red' : 6}

def calc_probability_two_blue(box):
    probability_two_blue = ((box['blue']/(box['blue']+box['red'])) * 
                            ((box['blue']-1)/(box['blue']+box['red']-1)))
    return probability_two_blue

if __name__ == "__main__":
    print("The probability of taking 2 blue discs is {0} ".format(
            calc_probability_two_blue(box)) +
            "given a box with {0} red discs and {1} blue discs."
            .format(box['red'], box['blue']))