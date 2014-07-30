#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division

""" Solution to "Reciprocal cycles", Problem 26

http://projecteuler.net/problem=26

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2 =   0.5
1/3 =   0.(3)
1/4 =   0.25
1/5 =   0.2
1/6 =   0.1(6)
1/7 =   0.(142857)
1/8 =   0.125
1/9 =   0.(1)
1/10    =   0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

"""

d = 10 # 10 | 1000

def len_cycle(n):
    "Find length of repeating cycle."
    # Use recursion

def longest_decimal_cycle(d):
    longest_cycle = 0
    for n in xrange(2,d+1):
        mantissa = str(1/n).split('.')[1]
        # current_cycle = len_cycle(mantissa)
        # if current_cycle > longest_cycle:
        #     longest_cycle = len_cycle
    return "'In Progress'" # longest_cycle

if __name__ == "__main__":
    print("The value of d < {0} for which 1/d contains the longest recurring cycle in its decimal fraction part is {1}."
            .format(d, longest_decimal_cycle(d)))