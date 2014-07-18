#!/usr/bin/env python

""" Solution to "Counting Sundays", aka Problem 19

http://projecteuler.net/problem=19

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

from calendar import day_name, monthrange

start_year = 1901
end_year = 2000
weekdays = {day:i for i,day in enumerate(day_name)}

def count_first_sundays(start_year, end_year):
    "For each year and each month, find the first day of the month. Add to counter"
    total_sundays = 0
    for year in xrange(start_year, end_year+1):
        for month in xrange(1,13):
            if monthrange(year,month)[0] == weekdays["Sunday"]:
                total_sundays += 1
    return total_sundays

if __name__ == "__main__":
    print("The number of Sundays falling on the first of the month "\
            "during the twentieth century is {0}."
            .format(count_first_sundays(start_year, end_year)))