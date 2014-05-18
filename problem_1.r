#! /usr/bin/env Rscript

# File description -------------------------------------------------------------
# Solutions to problem 1
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
#
# http://projecteuler.net/problem=1
# => 233168

# Setup ------------------------------------------------------------------------
cat("\014")   # Clear console
rm(list=ls()) # Delete all variables
stop_number <- 1000

# Brute force method -----------------------------------------------------------
final_sum <- 0
for (i in 1:stop_number-1) {
  if ((i %% 3 == 0) || (i %% 5 ==0)) {
    final_sum <- final_sum + i
  }
}

# A vectorized method ----------------------------------------------------------
sum_numbers_mod_3 <- sum(seq(0, stop_number-1, 3))
sum_numbers_mod_5 <- sum(seq(0, stop_number-1, 5))
sum_numbers_mod_15 <- sum(seq(0, stop_number-1, 15))
final_sum <- sum_numbers_mod_3 + sum_numbers_mod_5 - sum_numbers_mod_15

# Another vectorized method ----------------------------------------------------
sequence <- (1:stop_number-1)
final_sum <- (sum(sequence[sequence %% 3 == 0]) 
              + sum(sequence[sequence %% 5 == 0])
              - sum(sequence[sequence %% 15 == 0]))

# Write out results ------------------------------------------------------------
cat("The sum of all multiples of 3 or 5 below", stop_number, "is", final_sum, ".")
