#!/usr/bin/env python

""" Solution to "Power digit sum", aka Problem 16

http://projecteuler.net/problem=16

21^5 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

i = 1 # 0 = test, 1 = final
base_exp = ((2, 15), # base, exponent
            (2, 1000))

def calc_sum_digits(n):
    "Sum individual digits of given number."
    return sum([int(_) for _ in str(n)])

if __name__ == "__main__":
    print("The sum of all the digits in the number {0}^{1} is {2}."
            .format(base_exp[i][0], 
                    base_exp[i][1],
                    calc_sum_digits((base_exp[i][0]**base_exp[i][1]))))