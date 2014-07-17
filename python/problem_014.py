#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Solution to "Longest Collatz sequence", aka Problem 14

http://projecteuler.net/problem=14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

n = 1000000 # 13 #=> 20 | 1000000

def calc_collatz_seq(n, collatz_hash = {1:1}):
    """Recursive function to define a Collatz sequence. Hash previous values."""
    if n in collatz_hash:
        return collatz_hash[n]
    if n % 2 == 0:
        counter = 1 + calc_collatz_seq((n/2))
    else:
        counter = 1 + calc_collatz_seq((3*n+1))
    collatz_hash[n] = counter
    return counter

def find_longest_collatz_seq(n):
    """Find longest Collatz sequence under given number."""
    return max([calc_collatz_seq(_) for _ in xrange(1,n)])

def find_n_with_longest_seq(n, len_seq):
    """Find the number associated with the longest sequence."""
    for e in xrange(1,n):
        if calc_collatz_seq(e) == len_seq:
            return e

if __name__ == "__main__":
    print("The starting number, under one million, produces the "\
            "longest Collatz sequence chain is {0}."
            .format(find_n_with_longest_seq(n, find_longest_collatz_seq(n))))