#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Solution to "Summation of primes", aka Problem 10

http://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

n = 2000000 # 10 | 2000000

def prime_sieve(n):
    "Return a list of prime integers up to n"
    pass

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

def calc_sum_primes(n):
    "Sum primes below n"
    sum_primes = 0
    primes = gen_primes()
    current_prime = next(primes)
    while current_prime < n:
        sum_primes += current_prime
        current_prime = next(primes)
    return sum_primes
 
if __name__ == "__main__":
    print("The sum of all the primes below {0} is {1}."
          .format(n, calc_sum_primes(n)))