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

def is_prime(n):
    "Find if given number is a prime"
    if n < 2:
        return False
    else:
        return all([n % i != 0 for i in xrange(2, n)])

def distinct_factors(n):
    "Find a list of factors of given number."
    factors = [[i, n//i] for i in range(1, int(sqrt(n)) + 1) if n % i == 0]
    return filter(lambda x: len(set(x)) == len(x), factors) # Remove non-distinct

def find_consective_int_with_prime_factors(n_distinct_prime_factors):
    ""
    n = 2
    previous_n_has_distinct_primes = False

    while True:
        # Check if there are current number of distint primes
        has_distinct_primes = any([sum(map(is_prime, i)) == n_distinct_prime_factors
                                     for i in distinct_factors(n)])
        
        if has_distinct_primes:
            if previous_n_has_distinct_primes:
                return n
            else:
                previous_n_has_distinct_primes = True
        else:
            previous_n_has_distinct_primes = False

        print n, distinct_factors(n), has_distinct_primes
    
        n += 1

if __name__ == "__main__":
    print("The first of first {0} consecutive integers to have "\
            "{1} distinct prime factors is {2}."
            .format(n_distinct_prime_factors,
                    n_distinct_prime_factors,
                    find_consective_int_with_prime_factors(n_distinct_prime_factors)-1))
