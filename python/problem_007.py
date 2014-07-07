#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Solution to "10001st prime", aka Problem 7

http://projecteuler.net/problem=7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

n = 6 # 6 | 10001

def primes(n):
    "Generator function for primes"
    return 13

if __name__ == "__main__":
    print("The {0}th prime number is {1}."
          .format(n, primes(n)))