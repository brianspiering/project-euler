#!/usr/bin/env Rscript

# File description -------------------------------------------------------------
# Solutions to problem 1, http://projecteuler.net/problem=1
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
#
# => 233168

# Setup ------------------------------------------------------------------------
cat("\014")   # Clear console
rm(list=ls()) # Delete all variables
stop_number <- 1000

# Brute force method -----------------------------------------------------------
final_sum_method_1 <- 0
for (i in 1:stop_number-1) {
  if ((i %% 3 == 0) || (i %% 5 ==0)) {
    final_sum_method_1 <- final_sum_method_1 + i
  }
}

# A vectorized method ----------------------------------------------------------
sum_numbers_mod_3 <- sum(seq(0, stop_number-1, 3))
sum_numbers_mod_5 <- sum(seq(0, stop_number-1, 5))
sum_numbers_mod_15 <- sum(seq(0, stop_number-1, 15))
final_sum_method_2 <- sum_numbers_mod_3 + sum_numbers_mod_5 - sum_numbers_mod_15

# Another vectorized method ----------------------------------------------------
sequence <- (1:stop_number-1)
final_sum_method_3 <- (sum(sequence[sequence %% 3 == 0]) 
                     + sum(sequence[sequence %% 5 == 0])
                    - sum(sequence[sequence %% 15 == 0]))

# Write out results -----------------------------------------------------------
sums_from_all_methods <- c(final_sum_method_1,
                           final_sum_method_2, 
                           final_sum_method_3)
if (length(unique(sums_from_all_methods)) == 1) {
  print_sum <- final_sum_method_1
  cat("The sum of all multiples of 3 or 5 below", stop_number, "is", print_sum, ".")
} else {
  stop("Check methods")
}
