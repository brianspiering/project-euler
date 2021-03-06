#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Solution to "Smallest multiple", aka Problem 5

http://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

n = 10 # 10 | 20

def find_smalles_mulitple(n):
    "Brute force method"
    for i in xrange(n,100000000):
        if all([i % _ == 0 for _ in xrange(1,n+1)]):
            break
    return i

if __name__ == "__main__":
    print("The smallest positive number that is evenly divisible by " +
          "all of the numbers from 1 to {0} is {1}."
          .format(n, find_smalles_mulitple(n)))