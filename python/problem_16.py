#!/usr/bin/env python

""" Solution to "Power digit sum", aka Problem 16

http://projecteuler.net/problem=16

21^5 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

i = 1 # 0 = test, 1 = final
number_and_power = ((2,15), #base, power
                    (2, 1000))

def calc_sum_digits(n):
    "Sum individual digits of given number."
    sum_digits = 0
    for digit in str(n):
        sum_digits += int(digit)

    return sum_digits

sum_digits = calc_sum_digits((number_and_power[i][0]**number_and_power[i][1]))

if __name__ == "__main__":
    print("The sum of all the digits in the number {0}^{1} is {2}."
            .format(number_and_power[i][0], 
                    number_and_power[i][1],
                    sum_digits))