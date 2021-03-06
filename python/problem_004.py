#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Solution to "Largest palindrome product", aka Problem 4

http://projecteuler.net/problem=4

A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

low, high = 100, 999  # 10, 99 | 100, 999

def find_largest_palindrome(low, high):
    """(slightly) clever brute force method"""
    largest_palindrome = 0
    for x in xrange(high,low-1,-1):
       for y in xrange(high,low-1,-1):
            if is_palindrome(x*y) and (x*y > largest_palindrome):
                largest_palindrome = x*y    
    return largest_palindrome

def is_palindrome(n):
    return str(n) == str(n)[::-1]

if __name__ == "__main__":
    print("The largest palindrome made from the product of " + 
          "two {0}-digit numbers is {1}."
          .format(len(str(low)), find_largest_palindrome(low, high)))