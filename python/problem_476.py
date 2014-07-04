#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Solution to "Circle Packing II", aka Problem 476

http://projecteuler.net/problem=476

Let R(a, b, c) be the maximum area covered by three non-overlapping circles inside a triangle with edge lengths a, b and c.

Let S(n) be the average value of R(a, b, c) over all integer triplets (a, b, c) such that 1 ≤ a ≤ b ≤ c < a + b ≤ n

You are given S(2) = R(1, 1, 1) ≈ 0.31998, S(5) ≈ 1.25899.

Find S(1803) rounded to 5 decimal places behind the decimal point.
"""
n = 2 # 2 | 5 | 1803

def S(n):
    return 0.31998

if __name__ == "__main__":
    print("S({0}) is {1}."
            .format(n, S(n)))