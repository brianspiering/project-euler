#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Solution to "Factorial digit sum", aka Problem 20

http://projecteuler.net/problem=20

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

from math import factorial

n = 100 # 10 | 100

def calc_sum_factorial(n):
    "Find the sum the sum of the digits in the number n!"
    return reduce(lambda x, y: x+y, [int(_) for _ in str(factorial(n))])

if __name__ == "__main__":
    print("The sum of the digits in the number {0}! is {1}."
            .format(n, calc_sum_factorial(n)))