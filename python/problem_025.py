#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Solution to "1000-digit Fibonacci number", Problem 25

http://projecteuler.net/problem=25

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?

"""

num_digits = 3 # 3 | 1000


def fib():
    a, b = 0, 1
    while True:
        a, b = b, a+b
        yield a

def calc_something(num_digits):
    return "'In Progress'"

if __name__ == "__main__":
    print("The first term in the Fibonacci sequence to contain {} digits is {}."
            .format(num_digits, calc_something(num_digits)))