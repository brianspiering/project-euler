#! /usr/bin/env Rscript

# File description -------------------------------------------------------------
# Solutions to problem 3, http://projecteuler.net/problem=3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
# 
# => 6857

# Setup ------------------------------------------------------------------------
cat("\014")   # Clear console
rm(list=ls()) # Delete all variables
number <- 600851475143

is_prime <- function(number) {
  # Test if a number is a prime
  if (number == 2) {
    TRUE
  } else if (any(number %% 2:(number-1) == 0)) {
    FALSE
  } else { 
    TRUE
  }
}

is_factor <- function(possible_factor, number) {
  if ((number %% possible_factor == 0) && (possible_factor > 1)) {
    TRUE
  } else {
    FALSE
  }
}

# Brute force method -----------------------------------------------------------
prime_factors <- numeric()

for (i in 1:number) {
  if ((is_factor(i, number) == TRUE) && (is_prime(i) == TRUE)) {
    prime_factors <- c(prime_factors, i)
  } 
}

largest_prime_factor <- tail(prime_factors, n=1)

# Write out results ------------------------------------------------------------
cat("The largest prime factor of the number", number, "is",
    largest_prime_factor, ".")
