#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Solution to "Sum square difference", aka Problem 6

http://projecteuler.net/problem=6

The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

n = 10 # 10 | 100

def find_sum_square_difference(n):
    return 2640

if __name__ == "__main__":
    print("The difference between the sum of the squares of the first one "
          "{0} natural numbers and the square of the sum is {1}."
          .format(n, find_sum_square_difference(n)))