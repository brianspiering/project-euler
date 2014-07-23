#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Solution to "Amicable numbers", aka Problem 21

http://projecteuler.net/problem=21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from collections import Counter

n = 10000

def factors(n):
    "Find factors of n."
    return [_ for _ in xrange(1,n) if n % _ == 0]

def calc_factor_sum(n):
    "Make a list of sum of all factors for each index below n."
    return [sum(factors(_)) for _ in xrange(1,n+1)]

def sum_amicable_numbers(n):
    "Find sum of amicable numbers below n."
    factor_sum = calc_factor_sum(n)
    print(factor_sum)
    # Sum key value pairs where key and pairs are the same.
    # eg:
    # factor_sum[220] = 284
    # factor_sum[284] = 220
    # something like - s.intersection_update(t), https://docs.python.org/2/library/sets.html
    return "'In Progress'"

if __name__ == "__main__":
    print("The sum of all the amicable numbers under {0} is {1}."
            .format(n, sum_amicable_numbers(n)))