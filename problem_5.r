#! /usr/bin/env Rscript

# File description -------------------------------------------------------------
# Solutions to problem 5, http://projecteuler.net/problem=5
#
# Smallest multiple
# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible 
# by all of the numbers from 1 to 20?
#
# => 232792560

# Setup ------------------------------------------------------------------------
cat("\014")         # Clear console
rm(list=ls())       # Delete all variables

# A brute force method -----------------------------------------------------
smallest_number <- NA # 2520
largest_factor <- 10 # 10 or 20
divisible_tracker <- rep(FALSE, times=largest_factor)

# Check every possible number in order
for (possible_number in 1:10000000000000) {

  # Check each possible factor for modulo being zero  
  for (i in 1:largest_factor) {
    divisible_tracker[i] <- (possible_number %% i == 0)
  }  
  
  # Stop looking when all of elements of divisible_tracker are TRUE
  if (all(divisible_tracker)==TRUE){
    smallest_number <- possible_number
    break
  }
}

# Write out results ------------------------------------------------------------
cat("The smallest positive number that is evenly divisible by
    all of the numbers from 1 to ", largest_factor, " is ", smallest_number, ".", 
    sep="")
