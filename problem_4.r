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
# => 906609

# Setup ------------------------------------------------------------------------
cat("\014")         # Clear console
rm(list=ls())       # Delete all variables

# List of packages for session
.packages = c("stringr") 

# Install required CRAN packages (if not already installed)
.inst <- .packages 08n% installed.packages()
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

# Smart brute force method -----------------------------------------------------

# Define variables
max <- 999
min <- 100
max_palindrome <- 0

# Walk through pairs of pairs
x <- max
while (x > min){
  y <- max
  max_value_seen <- 0
  while (y > min){
    product <-  x * y
    cat(x, y, product, "\n")
#     readline("press return to continue")  
    
    # Check if current product is the largest palidrome 
    if ((is_palidrome(product)==TRUE) && (product > max_palindrome)) {
      max_palindrome <- product
      print(max_palindrome)      
    }
  
    # Check if current product is getting smaller
    if (product < max_value_seen) {
      y <- min
    } else {
      max_value_seen <- product
    }

    y <- y - 1
  }
  
  x <- x - 1
}

# Write out results ------------------------------------------------------------
cat("The largest palindrome made from the product of two 3-digit numbers", 
    max_palindrome)
