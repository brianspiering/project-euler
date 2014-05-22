#!/usr/bin/env Rscript

# File description -------------------------------------------------------------
# Solutions to problem 2, http://projecteuler.net/problem=2
#
# Each new term in the Fibonacci sequence is generated by adding the previous 
# two terms. By starting with 1 and 2, the first 10 terms will be:
#    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ... 
#    (The sum of even-valued terms of the sequences is 44)
#
# By considering the terms in the Fibonacci sequence whose values do not 
# exceed four million, find the sum of the even-valued terms.
#
# => 4613732

# Setup ------------------------------------------------------------------------
cat("\014")  # Clear console
rm(list=ls()) # Delete all variables
n_terms <- 10 #4000000000

# A brute force method -----------------------------------------------------------
# NOTE: It would be terrible idea to brute force for a sequence of 4 million
# Create Fibonacci sequence

fib_seq <- numeric(n_terms)
fib_seq[1] <- 1
fib_seq[2] <- 2
for (i in 3:n_terms) { 
  fib_seq[i] <- fib_seq[i-1]+fib_seq[i-2]
} 

# Get selected sums of within Fibonacci sequence
total_method_1 <- 0 
for (i in 1:length(fib_seq)) {
  if (fib_seq[i] %% 2 == 0) {
    total_method_1 <- total_method_1 + fib_seq[i]
  }
}

# Another brute force method ---------------------------------------------------
# Slighty better but still horrible big O
counter <- 1
total_method_2 <- 0
previous <- 0
current <- 1

while (TRUE) {
  # Update Fibonacci
  old_current <- current
  current <- previous + current
  previous <- old_current
  
  # Test how many terms
  if (counter >= n_terms) {
    break
  } else {
    counter <- counter +1 
  }
  
  # Update running total
  if (current %% 2 == 0) total_method_2 = total_method_2 + current
}

# A vectorized method ----------------------------------------------------------
# Define a Fibonacci sequence
# Find even-numbered elements and sum them

# A functional method ----------------------------------------------------------
# fib <- function(n){
#   # HT: http://bit.?ly/1iVRHLE
#   a=0
#   b=1
#   for(i in 1:n){
#     t=b
#     b=a
#     a=a+t
#     }
#   a
# } 

# Uses packages ---------------------------------------------------------------
# require("numbers")
# fib_seq <- fibonacci(n_terms, sequence = TRUE)

# Write out results ------------------------------------------------------------
total_print <- total_method_2
cat("The sum of the even-valued terms in a Fibonacci sequence below",
    n_terms, "is", total_print, ".")
