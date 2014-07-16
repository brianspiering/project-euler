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

n = 1000000

def collatz_seq(n, chain_length=1):
    if n == 1:
        return chain_length
    elif n % 2 == 0:
        chain_length += 1
        return collatz_seq(n/2, chain_length)
    elif n % 2 != 0:
        chain_length += 1
        return collatz_seq(3*n +1, chain_length)

def find_longest_collatz_seq_v1():
    "Brute force checking"
    return None

def find_longest_collatz_seq_v2():
    """Store all chains in a hash."""
    return None


if __name__ == "__main__":
    print("The starting number, under one million, produces the "\
            "longest Collatz sequence chain is {0}."
            .format(find_longest_collatz_seq()))