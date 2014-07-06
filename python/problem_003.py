#!/usr/bin/env python

""" Solution to "Largest prime factor", aka Problem 3

http://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

n = 600851475143  # 13195 | 600851475143

def find_factors(n):
    "My attempt"
    return [i for i in xrange(1,n+1) if n % i == 0]

def is_prime(n):
    # XXX: Returns True for n = 1 (1 is not a prime number)
    return all(n % i for i in xrange(2, n))

def factors(n):    
    "From StackOverflow"
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def find_largest_prime_factor(n):
    return max(filter(is_prime, find_factors(n)))

if __name__ == "__main__":
    print("The largest prime factor of {0} is {1}."
            .format(n, find_largest_prime_factor(n)))