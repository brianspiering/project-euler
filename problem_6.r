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

# Define functions
square <- function(x) {
    x ^ 2
}

# Define variables
n_terms <- 10 # 10 | 100

# A brute force method ---------------------------------------------------------
sum_of_squares <- 0
sum_of_numbers <- 0

for (i in 1:n_terms) {
  sum_of_squares <- sum_of_squares + i^2 
  sum_of_numbers <- sum_of_numbers + i
}

square_of_sum <- sum_of_numbers^2
difference_sum_squares_method_1 <- square_of_sum-sum_of_squares

# A vectorized method ----------------------------------------------------------
sum_of_squares_method_2 <- tail(cumsum(square(1:n_terms)), n=1)
square_of_sum_method_2 <- sum_of_numbers^2
difference_sum_squares_method_2 <- square_of_sum_method_2 - sum_of_squares_method_2

# Write out results ------------------------------------------------------------
results_from_all_methods <- c(difference_sum_squares_method_1,
                              difference_sum_squares_method_2)

if (length(unique(results_from_all_methods)) == 1) {
  results_final <- results_from_all_methods[1]
  cat("The difference between the sum of the squares of the first ", n_terms, 
      " natural numbers and the square of the sum is ", results_final, ".", 
      sep="")
} else {
  stop("Check methods")
}

# => 25164150