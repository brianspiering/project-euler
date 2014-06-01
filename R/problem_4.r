#!/usr/bin/env Rscript

# File description -------------------------------------------------------------
# Solutions to problem 4, http://projecteuler.net/problem=4
#
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers 
# is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
#


# Setup ------------------------------------------------------------------------
cat("\014")         # Clear console
rm(list=ls())       # Delete all variables

# List of packages for session
.packages = c("stringr") 

# Install required CRAN packages (if not already installed)
.inst <- .packages %in% installed.packages()
if(length(.packages[!.inst]) > 0) install.packages(.packages[!.inst])

# Load packages into session 
lapply(.packages, require, character.only=TRUE)

# Define functions
strReverse <- function(x){
  # From strsplit docs
  sapply(lapply(strsplit(x, NULL), rev), paste, collapse = "") 
}

is_palidrome <- function(number){
  # Check if number supply is the same forward and backwards
  isTRUE(as.character(number) == strReverse(as.character(number)))
}

# A (slightly clever) brute force method ---------------------------------------

# Define variables
max <- 999
min <- 100
max_palindrome <- 0

# Compare products of 2 numbers (x & y) to be palidrome
# Start at largest possible digit
# Walk down y till no solution is possible, 
# then walk down x till no solution is possible
cat("Finding the largest palindrome from the product of two 3-digit numbers...\n\n")
x <- max
while (x > min){
  y <- max
  while (y > min){
    product <-  x * y
    if (product > max_palindrome) {
      if (is_palidrome(product)==TRUE) {
        max_palindrome <- product 
      }
    } else{
      # Stop looking in current row if current product is smaller than 
      # current max palindrome
      y <- min
    }
    y <- y - 1    
  }
  x <- x - 1
}

# Write out results ------------------------------------------------------------
cat("The largest palindrome made from the product of two 3-digit numbers ", 
    max_palindrome, ".", sep="")

# => 906609