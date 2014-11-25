#!/usr/bin/env python

""" Solution to "Number letter counts", aka Problem 17

http://projecteuler.net/problem=17

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
"""

stop_number = 5 # 5 | 1000

# Arabic Number: English Word
number_dict = { 1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',
            8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',
            14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',
            18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'forty',
            50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',
            100:'hundred',1000:'thousand'}

def gen_letter_count(number_dict):
    "For each value in a given dict, count number of letters"
    return {_[0]:len(_[1]) for _ in number_dict.items()}

def count_letters(stop_number, letter_count_dict):
    "Count number of letters in words from 1 to n"
    sum_letters = 0
    for n in range(1,stop_number+1):
        if len(str(n)) == 1:
            sum_letters += letter_count_dict[n]
        elif len(str(n)) == 2:
            pass
        elif len(str(n)) == 3:
            pass

    return sum_letters
    
if __name__ == "__main__":
    letter_count_dict = gen_letter_count(number_dict)
    print("The number of letters in the numbers from 1 to {0} is {1}."
            .format(stop_number, count_letters(stop_number, letter_count_dict)))