#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Solution to "10001st prime", aka Problem 7

http://projecteuler.net/problem=7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?
"""

from itertools import islice

n = 10001 # 6 | 10001

ordinal_number_suffixes = {6:'th', 
                           10001:'st'}

def gen_primes():
    "A generator function for prime numbers"
    n = 2
    primes = set()
    while True:
        for p in primes:
            if n % p == 0:
                break
        else:
            primes.add(n)
            yield n
        n += 1

def nth(iterable, n, default=None):
    "Returns the nth item or a default value"
    return next(islice(iterable, n, None), default)

if __name__ == "__main__":
    print("The {0:,}{1} prime number is {2}."
          .format(n,
                  ordinal_number_suffixes[n],
                  nth(gen_primes(), n-1)))