#!/usr/bin/env python

""" Solutions to "Multiples of 3 and 5", aka Problem 1

http://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

n = 1000 # 10 | 1000

def sum_multiples():
    "Sum of all the multiples of 3 or 5 below n."
    return (sum(xrange(0,n,3)) + sum(xrange(0,n,5)) - sum(xrange(0,n,15)))

if __name__ == "__main__":
    print(sum_multiples(n))
