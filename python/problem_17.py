#!/usr/bin/env python

""" Solution to "Number letter counts", aka Problem 17

http://projecteuler.net/problem=17

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
"""

n = 5 # 5 | 1000

number_dict = { '1': 'one', # Arabic Number: English Word
                '2': 'two',
                '3': 'three',
                '4': 'four',
                '5': 'five'}

def gen_letter_count(number_dict):
    "For each value in a given dict, count number of letters"
    return {_[0]:len(_[1]) for _ in number_dict.items()}


def count_letters(n, letter_count_dict):
    "Count number of letters in words from 1 to n"
    return sum([letter_count_dict[str(_)] for _ in xrange(1,n+1)])

if __name__ == "__main__":
    letter_count_dict = gen_letter_count(number_dict)
    print("The number of letters in the numbers from 1 to {0} is {1}."
            .format(n, count_letters(n, letter_count_dict)))