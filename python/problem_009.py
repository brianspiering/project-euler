#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Solution to "Special Pythagorean triplet", aka Problem 9

http://projecteuler.net/problem=9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.

Find the product abc.
"""

sum_goal = 12 # 12 | 1000
a, b, c = 3, 4, 5

def is_pythagorean_triplet(a, b,c,):
    pass 

if __name__ == "__main__":
    print("The Pythagorean triplet for which a + b + c = " +
           "{} is a = {}, b = {}, c = {}. \nThe product abc is {}."
          .format(sum_goal, a, b, c, a*b*c))