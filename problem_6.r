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
source("benchmark_method.r")
square <- function(x) {
    x ^ 2
}

# Define variables
n_terms <- 100 # 10 | 100

# A brute force method ---------------------------------------------------------
calc_difference_sum_squares_method_1 <- function(n_terms){
  sum_of_squares <- 0
  sum_of_numbers <- 0
  
  for (i in 1:n_terms) {
    sum_of_squares <- sum_of_squares + i^2 
    sum_of_numbers <- sum_of_numbers + i
  }
  
  square_of_sum <- sum_of_numbers^2
  difference_sum_squares <- square_of_sum-sum_of_squares
  
  return(difference_sum_squares)
}

# Calculate answer
difference_sum_squares_method_1 <- calc_difference_sum_squares_method_1(n_terms)

# Benchmark method
benchmark_method(method_number=1, 
                 method_function=calc_difference_sum_squares_method_1,
                 method_argument=n_terms) 

# A vectorized method ----------------------------------------------------------
calc_difference_sum_squares_method_2 <- function(n_terms){
  sum_of_squares <- tail(cumsum(square(1:n_terms)), n=1)
  square_of_sum <- tail(cumsum(1:n_terms), n=1)^2
  difference_sum_squares <- square_of_sum - sum_of_squares

  return(difference_sum_squares)
}

# Calculate answer
difference_sum_squares_method_2 <- calc_difference_sum_squares_method_2(n_terms)

# Benchmark method
benchmark_method(method_number=2, 
                 method_function=calc_difference_sum_squares_method_2,
                 method_argument=n_terms) 

# Write out results ------------------------------------------------------------
results_from_all_methods <- c(difference_sum_squares_method_1,
                              difference_sum_squares_method_2)

if (length(unique(results_from_all_methods)) == 1) {
  results_final <- results_from_all_methods[1]
  cat("\nThe difference between the sum of the squares of the first ", n_terms, 
      " natural numbers and the square of the sum is ", results_final, ".", 
      sep="")
} else {
  stop("Check methods")
}

# => 25164150