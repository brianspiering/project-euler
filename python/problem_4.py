#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Solution to "Largest palindrome product", aka Problem 4

http://projecteuler.net/problem=4

A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

low, high = 10, 99  # 10, 99 | 100, 999

n = 9009  

def is_palindrom(n):
    return str(n) == str(n)[::-1]

if __name__ == "__main__":
    print("The largest palindrome made from the product of two {0}-digit numbers is {1}.".format(len(str(low)), n))