---
layout: page
title: Numerical Analysis
author: Chinmay H
tags: [ "math", "numericalmethods",]
categories: [ "notes" ]
date: 2020-01-20
description: Table of Contents Sheet / Course Map for Numerical Analysis
---


### Resources

- [Jacob Bishop's Tutorials](https://www.youtube.com/user/kvyi/playlists) Part 5-7 covers most topics
- [Gauss Quadrature Vs Newton Cotes' Visualization](https://www.youtube.com/watch?v=EG62xCOdLLA)
- Check Calculator function input for Iterative Approximation Methods( Newton-Rhapson, Fixed Point Iteration etc.)

## Basic Analysis

- Catastrophic Cancellation
- Significant Digits Vs Decimal points
- Sum for minimal error, rounding/chopping
- Taylor Series' Approximation and Error

### Iterative Methods

1. Bisection
2. Regula Falsi (Method of Chords)
3. Secant
    - Swap to whichever is close
4. Fixed Point Iteration
    - Order of convergences
    - Uniqueness
    - Error Analysis
5. Newton Raphson
    - Order of convergences

### Matrix Techniques

- Pivoting (Partial Pivoting = Every Step)
- Scaling
    - First before Pivoting
- Matrix Norms
    - Norm_1(A) = max(col sum)
    - Norm_inf(A) = max(row sum)
    - Norm_2(A) = Spectral Norm = $\sqrt \lambda$ for eigenvalue
    - Norm_F(A) = root of(Sum of all a_ij^2) = Frobenius Norm
- Conditional No. = ||A|| * ||A^-1||

### Matrix Iterative Methods
In order to solve, systems of equation we have Gauss-El-M, Gauss-Jacobi and Gauss-Siedel. Jacobi and Siedel is mostly used for sparse arrays where G-El-M is highly ineffecient.
Newton-Raphson, Fixed Point are iterative methods also work while finding solution.

- Gaussian Elimination
- G-Jacobi's
- G-Jacobi's Matrix Version
- G-Siedel
- G-Siedel Matrix Version
- Fixed Point (Matrix)
- Newton-Raphson (Matrix)

Points to note

- Matrix must be Diagonally Dominant (see thm) for Jacobi/Gauss-Siedel

### Interpolation Methods

- Polynomial
- Lagrange
    - Error
- Newton Divided Difference
- Newton Forward Difference*
- Newton Backward Difference*
- Hermite
- Oscullatory (generalized Hermite)

* NBD, NFD is only for equally spaced

#### Table for N.D.D-like Interpolation

- NDD : $frac{f_2 - f_1}{ x_2 - x_1 }$ for each el
- NFD: $f_2 -f_1$ Only
- NBD: Start Reverse and Take Bottom Row; Same table as NFD $f_2 - f_1$;
- HERM: Repeat each entry twice; $frac{f_2 - f_1}{x_2 - x_1} if different or differentiation if same
- OSC: Repeat based on no. of available vals in x, y, y' ..; $f_2 - f_1$


## Approximation for Integration
In order of specific to generalized.

- Newton Cotes' Formula - Approximate function as polynomial and find area.
    - Trapezoid Rule        (n = 1 approx:2 data points linear Pn)
    - Simpson's 1/3 Rule    (n = 2 approx:3 data points quadratic Pn)
    - Simpson's 3/8 Rule    (n = 3 approx:4 data points cubic Pn)
    - Generalized Newton Cotes'
- Gaussian Quadrature Method (Method of Undetermined Coeffecients) - Choose points that make the equivalent polygon (may not be contained)
    - Gauss-Chebyshev, Gauss-Legendre, Gauss-Hermite with different weight functions

## Approximations for Initial Value Problems

Use Taylor Series to derive the equations!
Useful predictor methods also,

- Euler's Method (RK 1st Order)
- Modified Euler Method (RK with 2nd Order AKA Heun's Method)
- Runge Kutta(RK) Schemes: Move along the slope(which is approximated by the order) from one point to the next point
- Taylor Series Expansion

See Use of Butcher Table also and RK in 2 variable (using 2 variable Taylor Series)!

- Multi-Step Method
    - Predictor: Adams-Bashforth (Derived from previous m+1 points NBD Polynomial approx)
    - Corrector: Adams-Moulton  (Derived from previous(and including) m +2 points NBD Polynomial)

- Milne's Predictor Formula (Generalized Adams-Besforth by changing limits of integration)

## Approximating System of ODEs
- Runge-Kutta 2 variable method
- Implicit Euler's
- Milne's Method


## Approximations for Boundary Value Problems

- Finite Difference Method
- Finite Element Methods
    - Collocation Method
    - Rayleigh Ritz Method
    - Galerekin's Weighting Function Method
