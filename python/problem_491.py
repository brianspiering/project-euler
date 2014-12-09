#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Solution to "Double pandigital number divisible by 11", aka Problem 491

https://projecteuler.net/problem=491

We call a positive integer double pandigital if it uses all the digits 0 to 9 
exactly twice (with no leading zero). 
For example, 40561817703823564929 is one such number.

How many double pandigital numbers are divisible by 11?
"""

from itertools import permutations, izip

def n_double_pandigital_mod_11():
    """"Find the number of double pandigital numbers are divisible by 11:
            1. Create an interator object of all permutations.
            2. Convert each tuple to a integer.
            3. Sum integers that are modulus 11 with list comprehension."""
    double_pandigitals = permutations(range(10)+range(10))

    # NOTE: It might be faster to elimate many contenders by ...
    # Take the alternating sum of the digits from left to right. 
    # If that is divisible by 11, so is the original number.
    # (sum(int(e) for e in str(n)[::2]) - sum(int(e) for e in str(n)[1::2])) % 11 == 0

    return sum(reduce(lambda n1, n2: n1*10+n2, current_tuple) % 11 == 0 
                for current_tuple in double_pandigitals)

if __name__ == "__main__":
    print("The number of double pandigital numbers are divisible by 11 is: {0}"
            .format(n_double_pandigital_mod_11()))
