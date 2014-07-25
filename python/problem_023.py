#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Solution to "Non-abundant sums", Problem 23

http://projecteuler.net/problem=23

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

"""

def factors(n):
    "Find factors of n."
    return [_ for _ in xrange(1,n) if n % _ == 0]

def is_abundant_num(n):
    "Check if a number is abundant - the sum of factors of n exceeds n itself."
    return sum(factors(n)) > n

def abundant_nums():
    "A generator for abundant - the sum of factors of n exceeds n itself."
    pass

def abundant_num_sum_sieve():
    "A sieve for integers that are not sums of abundant numbers."
    a = [False]*28123 # Set all possible to the limit of the sieve

def total_nonabundant_num_sum(a):
    
    # Rough code 
    a = [True, False, True, False] # Sample data
    total_nonabundant_num_sum = sum([i+1 for i,e in enumerate(a) if e == False])

    return "'In Progress'"

if __name__ == "__main__":
    print("The sum of all the positive integers which cannot be written " \
            "as the sum of two abundant numbers is {}."
            .format(calc_something()))