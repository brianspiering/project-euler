#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Solution to "Special Pythagorean triplet", aka Problem 9

http://projecteuler.net/problem=9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.

Find the product abc.
"""

sum_stop = 1000 # 12 | 1000

def is_pythagorean_triplet(a, b, c):
    return a**2 + b**2 == c**2 

def product_pythagorean_triplet(sum_stop):
    """Find the product of a Pythagorean triplet that equals given sum.
    Use brute force checking"""
    for a in xrange(1, sum_stop):
        for b in xrange(1, sum_stop-a):
            c = sum_stop-a-b
            if is_pythagorean_triplet(a, b, c):
                return {'a':a, 'b':b, 'c':c, 'product':a*b*c}
    print('No product of a Pythagorean triplet possible for given sum.')
 
if __name__ == "__main__":
    print("The Pythagorean triplet for which a + b + c = " +
           "{} is a = {}, b = {}, c = {}. \nThe product abc is {}."
          .format(sum_stop, 
                  product_pythagorean_triplet(sum_stop)['a'], 
                  product_pythagorean_triplet(sum_stop)['b'],
                  product_pythagorean_triplet(sum_stop)['c'],
                  product_pythagorean_triplet(sum_stop)['product']))