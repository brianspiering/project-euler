#!/usr/bin/env Rscript

# File description -------------------------------------------------------------
# benchmark_methods
# A function to benchmark methods for solving Project Euler problems

# Setup ------------------------------------------------------------------------
# List of packages for session
.packages = c("rbenchmark") 

# Install required CRAN packages (if not already installed)
.inst <- .packages %in% installed.packages()
if(length(.packages[!.inst]) > 0) install.packages(.packages[!.inst])

# Load packages into session 
lapply(.packages, require, character.only=TRUE)

cat("\014")   # Clear console

# Define benchmark methods function ------------------------------------------- 
benchmark_methods <- function(method_number, method_function){
  # Get the benchmarks for current function
  benchmark_methods <- benchmark(method_function(stop_number))
  # Print benchmarks results
  cat("Method ", method_number, " takes ", benchmark_methods$elapsed, 
      " seconds.\n", sep="")
}
