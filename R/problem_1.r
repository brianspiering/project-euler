#!/usr/bin/env Rscript

# File description -------------------------------------------------------------
# Solutions to "Multiples of 3 and 5"
# Problem 1, http://projecteuler.net/problem=1
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

# Setup ------------------------------------------------------------------------
rm(list=ls()) # Delete all variables
cat("\014")   # Clear console

# Define functions
source("benchmark_method.r")

# Define variables
stop_number <- 1000 # 10 | 1000

# A brute force method ---------------------------------------------------------
calc_multiples_3_and_5_method_1 <- function(stop_number){
  sum_multiples <- 0
  for (i in 1:stop_number-1) {
    if ((i %% 3 == 0) || (i %% 5 == 0)) {
      sum_multiples <- sum_multiples + i
    }
  }
  return(sum_multiples)
}

# Calculate answer
sum_method_1 <- calc_multiples_3_and_5_method_1(stop_number) 

# Benchmark method
benchmark_method(method_number=1, 
                 method_function=calc_multiples_3_and_5_method_1,
                 method_argument=stop_number) 

# A vectorized method ----------------------------------------------------------
calc_multiples_3_and_5_method_2 <- function(stop_number){
  sequence <- (1:stop_number-1)
  sum_multiples <- (sum(sequence[sequence %% 3 == 0]) 
                         + sum(sequence[sequence %% 5 == 0])
                         - sum(sequence[sequence %% 15 == 0])) 
  return(sum_multiples)
}

# Calculate answer
sum_method_2 <- calc_multiples_3_and_5_method_2(stop_number)

# Benchmark method
benchmark_method(method_number=2, 
                 method_function=calc_multiples_3_and_5_method_2,
                 method_argument=stop_number) 

# Another vectorized method ----------------------------------------------------
# This method uses less memory by creating only the parts of the sequence needed
calc_multiples_3_and_5_method_3 <- function(stop_number){
  sum_numbers_mod_3 <- sum(seq(from=0, to=stop_number-1, by=3))
  sum_numbers_mod_5 <- sum(seq(from=0, to=stop_number-1, by=5))
  sum_numbers_mod_15 <- sum(seq(from=0, to=stop_number-1, by=15))
  sum_multiples <- sum_numbers_mod_3 + sum_numbers_mod_5 - sum_numbers_mod_15
  return(sum_multiples)
}

# Calculate answer
sum_method_3 <- calc_multiples_3_and_5_method_3(stop_number)

# Benchmark method
benchmark_method(method_number=3, 
                 method_function=calc_multiples_3_and_5_method_3,
                 method_argument=stop_number) 

# Write out results -----------------------------------------------------------
results_from_all_methods <- c(sum_method_1,
                              sum_method_2, 
                              sum_method_3)

if (length(unique(results_from_all_methods)) == 1) {
  results_final <- results_from_all_methods[1]
  cat("\nThe sum of all multiples of 3 or 5 below ", stop_number, 
      " is ", results_final, ".\n\n", sep="")
} else {
  stop("Check methods")
}

# => 233168