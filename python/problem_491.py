#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Solution to "Double pandigital number divisible by 11", aka Problem 491

https://projecteuler.net/problem=491

We call a positive integer double pandigital if it uses all the digits 0 to 9 exactly twice (with no leading zero). For example, 40561817703823564929 is one such number.

How many double pandigital numbers are divisible by 11?
"""

from itertools import permutations

# Find the number of single pandigital numbers are divisible by 11 to warmup
def n_single_pandigital_mod_11():
    single_pandigitals = permutations(range(10))
    return sum([int(''.join(str(x) for x in current_tuple)) % 11 == 0 for current_tuple in single_pandigitals])

def n_double_pandigital_mod_11():
        return 'In Progress'

if __name__ == "__main__":
    print("The number of double pandigital numbers are divisible by 11 is: {0}\n"+  
            "(fyi: The number of single pandigital numbers are divisible by 11 is: {1}"
            .format(n_double_pandigital_mod_11(), n_single_pandigital_mod_11()))
