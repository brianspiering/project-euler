#! /usr/bin/env Rscript

# File description -------------------------------------------------------------
# Solutions to problem 1
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
#
# http://projecteuler.net/problem=1

rm(list=ls()) # Delete all variables

# Brute force
stop_number = 1000
sum = 0
for (i in 1:stop_number-1) {
  if (i %% 3 == 0 | i %% 5 ==0) {
    sum = sum + i
  }
}
cat("The sum of all multiples of 3 or 5 below", stop_number, "is", sum, ".")
