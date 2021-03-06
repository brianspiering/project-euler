#! /usr/bin/env Rscript

# File description -------------------------------------------------------------
# Solutions to problem 3, http://projecteuler.net/problem=3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
# 

# Setup ------------------------------------------------------------------------
cat("\014")   # Clear console
rm(list=ls()) # Delete all variables
number <- 13195 # 600851475143

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

# A brute force method -----------------------------------------------------------
prime_factors <- numeric()

for (i in 1:number) {
  if ((is_factor(i, number) == TRUE) && (is_prime(i) == TRUE)) {
    prime_factors <- c(prime_factors, i)
  } 
}

largest_prime_factor_method_1 <- tail(prime_factors, n=1)

# A package method --------------------------------------------------------------
# List of packages for session
.packages = c("numbers") 

# Install required CRAN packages (if not already installed)
.inst <- .packages %in% installed.packages()
if(length(.packages[!.inst]) > 0) install.packages(.packages[!.inst])

# Load packages into session 
lapply(.packages, require, character.only=TRUE)

largest_prime_factor_method_2 <- tail(primeFactors(number), n=1)

# Write out results ------------------------------------------------------------
results_from_all_methods <- c(largest_prime_factor_method_1,
                              largest_prime_factor_method_2)

if (length(unique(results_from_all_methods)) == 1) {
  results_final <- sample(results_from_all_methods, size=1)
  cat("The largest prime factor of ", number, " is ", results_final, ".", sep="")
} else {
  stop("Check methods")
}

# => 6857