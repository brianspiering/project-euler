#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Solution to "Names scores", aka Problem 22

http://projecteuler.net/problem=22

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

import string

def process_file(file_name):
     # Load file
    with open(file_name) as f:
        lines = f.read().split(",")

    lines = [line[1:-1] for line in lines] # Strip extra set of quotes

    return lines

def total_names():
    "Find total of all the name scores."
    names = process_file('names.txt') # Load names
    names.sort() # Alphabeticalize
    letters = list(string.ascii_uppercase) # Get list of letters
    total_name_scores = 0
    for i, name in enumerate(names):
        total_letter = sum([letters.index(letter)+1 for letter in name]) # Get total of letters
        name_score = total_letter * i+1
        total_name_scores += name_score
    return total_name_scores

if __name__ == "__main__":
    print("The total of all the name scores in the file is {}."
            .format(total_names()))