#! /usr/bin/env Rscript

# File description -------------------------------------------------------------
# Solutions to problem 2, http://projecteuler.net/problem=2
#
# Each new term in the Fibonacci sequence is generated by adding the previous 
# two terms. By starting with 1 and 2, the first 10 terms will be:
#    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not 
# exceed four million, find the sum of the even-valued terms.
#
# => 4613732

# Setup ------------------------------------------------------------------------
cat("\014")  # Clear console
rm(list=ls()) # Delete all variables
n_terms <- 10 #4000000000

# Brute force method -----------------------------------------------------------
# NOTE: It would be terrible idea to brute force for a sequence of 4 million
# Create Fibonacci sequence
fibv_seq <- numeric(n_terms)
fibv_seq[1] <- 1
fibv_seq[2] <- 1
for (i in 3:n_terms) { 
  fibv_seq[i] <- fibv_seq[i-1]+fibv_seq[i-2]
} 

# Get selected sums of within Fibonacci sequence
sum <- 0 
for (i in 1:length(fibv_seq)) {
  if (i %% 2 == 0) {
    sum <- sum + i
  }
}

# A vectorized method ----------------------------------------------------------
# Define a Fibonacci sequence
# Find even-numbered elements and sum them

# Write out results ------------------------------------------------------------
cat("The sum of the even-valued terms in a Fibonacci sequence below",
    n_terms, "is", sum, ".")
