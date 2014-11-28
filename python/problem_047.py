#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Solution to "Distinct primes factors", Problem 47

https://projecteuler.net/problem=47

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors. 
What is the first of these numbers?

"""
from math import sqrt

n_distinct_prime_factors = 2 # 2 | 3 | 4

def distinct_prime_factors(n):
    prime_factors = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            prime_factors.append(d) 
            n /= d
        d += 1
    if n > 1:
       prime_factors.append(n)

    # Check for distinct factors   
    if len(set(prime_factors)) == len(prime_factors):
        return prime_factors
    else:
        return []

def find_consective_int_with_prime_factors(n_distinct_prime_factors):
    ""
    n = 2 # 2, 642
    record_of_distinct_primes = [False, False]

    while True:
        # Check if there are current number of distint primes
        record_of_distinct_primes.append(len(distinct_prime_factors(n)) == n_distinct_prime_factors)

        print n, distinct_prime_factors(n), record_of_distinct_primes

        if all(record_of_distinct_primes[n-1:]):
                return n
        
        n += 1

        # Manually stop
        if n == 18:
            break

if __name__ == "__main__":
    print("The first of first {0} consecutive integers to have "\
            "{1} distinct prime factors is {2}."
            .format(n_distinct_prime_factors,
                    n_distinct_prime_factors,
                    find_consective_int_with_prime_factors(n_distinct_prime_factors)-(n_distinct_prime_factors-1)))
