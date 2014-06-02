#!/usr/bin/env python

""" Solution to "Multiples of 3 and 5", aka Problem 1

http://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

from random import choice

n = 1000  # 10 | 1000

def sum_multiples_method_1(n):
    "Sum of all the multiples of 3 or 5 below n."
    
    # Check each value, one at time
    sum_multiples = 0
    for i in xrange(n):
        if i % 3 == 0 or i % 5 == 0: sum_multiples += i

    return sum_multiples

def sum_multiples_method_2(n):
    "Sum of all the multiples of 3 or 5 below n."
   
    # Generate a sequence of only needed values then sum them
    return (sum(xrange(0,n,3)) + sum(xrange(0,n,5)) - sum(xrange(0,n,15)))

if __name__ == "__main__":
    print("The sum of all the multiples of 3 or 5 below {0} is {1}."
            .format(n, 
                choice([sum_multiples_method_1(n), sum_multiples_method_2(n)])))
