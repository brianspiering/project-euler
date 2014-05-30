#! /usr/bin/env Rscript

# File description -------------------------------------------------------------
# Solutions to problem 6, http://projecteuler.net/problem=6
#
# Sum square difference
# The sum of the squares of the first ten natural numbers is,
#    1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
#   (1 + 2 + ... + 10)^2 = 55^2 = 3025
#
# Hence the difference between the sum of the squares of 
# the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of 
# the first one hundred natural numbers and the square of the sum.

# Setup ------------------------------------------------------------------------
cat("\014")         # Clear console
rm(list=ls())       # Delete all variables

# Define variables
stop_number <- 100 # 10 | 100

# A brute force method -----------------------------------------------------
sum_of_squares <- 0
sum_of_numbers <- 0

for (i in 1:stop_number) {
  sum_of_squares <- sum_of_squares + i^2 
  sum_of_numbers <- sum_of_numbers + i
}

square_of_sum <- sum_of_numbers^2
difference_sum_squares <- square_of_sum-sum_of_squares

# Better ideas -----
# try cumsum()

# Write out results ------------------------------------------------------------
cat("The difference between the sum of the squares of the first ", stop_number, 
    " natural numbers and the square of the sum is ", difference_sum_squares, ".", 
    sep="")

# => 25164150