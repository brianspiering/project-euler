#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Solution to "Highly divisible triangular number", aka Problem 12

http://projecteuler.net/problem=12

The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""

stop_n_divisors = 5 # 5 | 500

def sequence_triangle():
    "A generator for triangle numbers, running summing previous numbers."
    c = 0
    while True:
        c += 1
        yield sum(range(c + 1))
        
def factors(n):  
    "All factors of n"
    # From stackoverlow  
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def calc_triangle_divisor(stop_n_divisors):
    "Calucute first triangle number to have over n divisors"
    triangle_number = sequence_triangle() # Create generator
    current_triangle_number = next(triangle_number) # Get 1st value
    while len(factors(current_triangle_number)) <= stop_n_divisors:
        current_triangle_number = next(triangle_number)
    return current_triangle_number

if __name__ == "__main__":
    print("The value of the first triangle number to have over "\
            "{0} divisors is {1}."
            .format(stop_n_divisors, calc_triangle_divisor(stop_n_divisors)))