#! /usr/bin/env Rscript

# File description -------------------------------------------------------------
# Solutions to problem 6, http://projecteuler.net/problem=6
#
# Sum square difference
# The sum of the squares of the first ten natural numbers is,
#    1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
#   (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of 
# the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of 
# the first one hundred natural numbers and the square of the sum.

# Setup ------------------------------------------------------------------------
cat("\014")         # Clear console
rm(list=ls())       # Delete all variables
stop_number <- 10
difference <- NA

# A brute force method -----------------------------------------------------

# Write out results ------------------------------------------------------------
cat("The difference between the sum of the squares of the first ", stop_number, 
    " natural numbers and the square of the sum is ", difference, ".", 
    sep="")

# =>