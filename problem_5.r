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
largest_factor <- 10 # 20
smallest_multiple <- 2520

# Write out results ------------------------------------------------------------
cat("The smallest positive number that is evenly divisible by
    all of the numbers from 1 to ", largest_factor, " is ", smallest_multiple, ".", 
    sep="")
