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

num_digits = 1000 # 3 | 1000


def fib():
    "A Fibonacci sequence generator."
    a, b = 0, 1
    while True:
        a, b = b, a+b
        yield a

def find_fib_term(num_digits):
    "Find the 1st fib term that has the given number of digits."
    f = fib()
    counter = 0
    while True:
        current_fib = f.next()
        counter += 1
        if len(str(current_fib)) == num_digits:
            break
    return counter

if __name__ == "__main__":
    print("The first term in the Fibonacci sequence to contain {} digits is {}th term."
            .format(num_digits, find_fib_term(num_digits)))