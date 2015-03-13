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
from functools import reduce

n = 10000

def factors(n):
    "Find factors of n."
    return {_ for _ in range(1,n) if n % _ == 0}

def calc_factor_sum(n):
    "Make a list of sum of all factors for each index below n."
    return [sum(factors(_)) for _ in range(n+1)]

def sum_amicable_numbers(n):
    "Find sum of amicable numbers below n."
    sum_amicable_numbers = 0
    factor_sums = calc_factor_sum(n)
    for (i, current_factor_sum) in enumerate(factor_sums): 
        if current_factor_sum < n: # Avoid IndexError
            if (factor_sums[current_factor_sum] == i) and (i > 2) and (i != current_factor_sum):
                    sum_amicable_numbers += current_factor_sum
    return sum_amicable_numbers

if __name__ == "__main__":
    print("The sum of all the amicable numbers under {0:,} is {1:,}."
            .format(n, 
                    sum_amicable_numbers(n)))