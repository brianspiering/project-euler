#!/usr/bin/env Rscript

# File description -------------------------------------------------------------
# Solutions to problem 1, http://projecteuler.net/problem=1
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
#

# Setup ------------------------------------------------------------------------
cat("\014")   # Clear console
rm(list=ls()) # Delete all variables
stop_number <- 1000

# A brute force method -----------------------------------------------------------
final_sum_method_1 <- 0
for (i in 1:stop_number-1) {
  if ((i %% 3 == 0) || (i %% 5 == 0)) {
    final_sum_method_1 <- final_sum_method_1 + i
  }
}

# A vectorized method ----------------------------------------------------
sequence <- (1:stop_number-1)
final_sum_method_3 <- (sum(sequence[sequence %% 3 == 0]) 
                     + sum(sequence[sequence %% 5 == 0])
                    - sum(sequence[sequence %% 15 == 0]))

# A vectorized method ----------------------------------------------------------
# This method uses less memory by creating only the parts of the sequence needed.
sum_numbers_mod_3 <- sum(seq(from=0, to=stop_number-1, by=3))
sum_numbers_mod_5 <- sum(seq(from=0, to=stop_number-1, by=5))
sum_numbers_mod_15 <- sum(seq(from=0, to=stop_number-1, by=15))
final_sum_method_2 <- sum_numbers_mod_3 + sum_numbers_mod_5 - sum_numbers_mod_15

# Write out results -----------------------------------------------------------
results_from_all_methods <- c(final_sum_method_1,
                              final_sum_method_2, 
                              final_sum_method_3)

if (length(unique(results_from_all_methods)) == 1) {
  results_final <- results_from_all_methods[1]
  cat("The sum of all multiples of 3 or 5 below", stop_number, 
      "is", results_final, ".")
} else {
  stop("Check methods")
}

# => 233168