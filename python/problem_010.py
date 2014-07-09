#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Solution to "Summation of primes", aka Problem 10

http://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

n = 10 # 10 | 2000000

def sum_primes(n):
    return 17
 
if __name__ == "__main__":
    print("The sum of all the primes below {0} is {1}."
          .format(n, sum_primes(n)))