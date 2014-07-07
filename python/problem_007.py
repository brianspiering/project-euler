#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Solution to "10001st prime", aka Problem 7

http://projecteuler.net/problem=7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

n = 10001 # 6 | 10001

ordinal_number_suffixes = {6:'th', 10001:'st'}

def gen_primes():
    "Generator function for prime numbers"
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

if __name__ == "__main__":
    primes = gen_primes()
    print("The {0}{1} prime number is {2}."
          .format(n, ordinal_number_suffixes[n], [primes.next() for _ in xrange(n)][-1]))