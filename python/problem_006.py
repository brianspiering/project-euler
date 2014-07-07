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

n = 100 # 10 | 100

def find_sum_square_difference(n):
    "Use functional programming"
    sum_of_squares = reduce(lambda x, y: x + y**2, xrange(1,n+1))
    square_of_sum = (reduce(lambda x, y: x + y, xrange(1,n+1)))**2
    return square_of_sum - sum_of_squares

if __name__ == "__main__":
    print("The difference between the sum of the squares of the first one "
          "{0} natural numbers and the square of the sum is {1}."
          .format(n, find_sum_square_difference(n)))