# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 17:25:58 2025

@author: Frankie15
##################################################
#
# QMB 3311: Python for Business Analytics
#
# Name: Frances Rodriguez Diaz 
#
# Date: 3/31/2025
# 
##################################################
#
# Script for Assignment 6: 
#
##################################################
"""

##################################################
# Import Required Modules
##################################################

# import name_of_module

import doctest
import math

##################################################
# Functions
##################################################

def ln_taylor(z: float, n: float) -> float:
    """
    Estimates ln(z) by summing the first n terms of the Taylor Series 
    when z is close to 1.
        
    >>> round(ln_taylor(1.5, 10), 3)
    0.405
    >>> round(ln_taylor(1.1, 10), 3)
    0.095
    >>> round(ln_taylor(1, 10), 3)
    0.0
    >>> ln_taylor(0, 10)
    Error: z must be positive and not equal to 0
    """
    if z <= 0:
        print("Error: z must be positive and not equal to 0")
        return None
        
    result = 0 
    for k in range(1, n + 1):
        n_term = ((-1) ** (k - 1)) * ((1/k) * ((z - 1) ** k))
        result += n_term
    return result


def exp_x_diff(x: float, z: float) -> float:
    """
    Returns the value of e ** x - z

    >>> round(exp_x_diff(1, 2), 3)
    0.718
    >>> round(exp_x_diff(2, 5), 3)
    2.389
    >>> exp_x_diff(1, -2)
    Error: z must be positive
    >>> exp_x_diff(0, 0)
    Error: z must be positive
    """
    if z <= 0:
        print("Error: z must be positive")
        return None
    return round(math.exp(x) - z, 3)
    
    return math.exp(x) - z


def ln_z_bisect(z: float, a_0: float, b_0: float, num_iter: int) -> float:
    """
    Produces an algorithm for calculating the natural logarithm of z. 

    >>> round(ln_z_bisect(2, 0, 2, 20), 3)
    0.693
    >>> round(ln_z_bisect(5, 1, 3, 30), 3)
    1.609
    >>> ln_z_bisect(2, 2, 3, 20)
    Error: exp_x_diff must have opposite signs at the interval end points
    >>> ln_z_bisect(-1, 0, 2, 20)
    Error: z must be positive
    """
    if exp_x_diff(a_0, z) == None or exp_x_diff(b_0, z) == None:
        return None
    
    if exp_x_diff(a_0, z) * exp_x_diff(b_0, z) >= 0:
        print("Error: exp_x_diff must have opposite signs at the interval end points")
        return None

    for _ in range(num_iter):
        mid = (a_0 + b_0) / 2
        if exp_x_diff(mid, z) * exp_x_diff(a_0, z) < 0:
            b_0 = mid
        else:
            a_0 = mid
    return (a_0 + b_0) / 2


def exp_x_diff_prime(x: float, z: float) -> float:
    """
    Returns the derivative of exp_x_diff(x, z) with respect to x

    >>> round(exp_x_diff_prime(1, 2), 3)
    2.718
    >>> round(exp_x_diff_prime(2, 5), 3)
    7.389
    >>> exp_x_diff_prime(1, -2)
    Error: z must be positive
    >>> exp_x_diff_prime(0, 0)
    Error: z must be positive
    """
    if z <= 0:
        print("Error: z must be positive")
        return None
    
    return math.exp(x)


def ln_z_newton(z: float, x_0: float, tol: float, num_iter: int) -> float:
    """
    Approximates the natrual log of z, ln(z), using Newton's method.

    >>> round(ln_z_newton(2, 1, math.pow(10, -10), 20), 3)
    0.693
    >>> round(ln_z_newton(5, 2, math.pow(10, -10), 20), 3)
    1.609
    >>> ln_z_newton(-1, 1, math.pow(10, -10), 20)
    Error: z must be positive
    """
    if z <= 0:
        print("Error: z must be positive")
        return None

    for _ in range(num_iter):
        fx = exp_x_diff(x_0, z)
        dfx = exp_x_diff_prime(x_0, z)

        if fx == None or dfx == None:
            return None

        if abs(fx) < tol:
            return round(x_0, 3)

        x_0 = x_0 - fx / dfx
        
    print("Warning: Reached max iterations before exp_x_diff(x_i, z) < tol")
    return round(x_0, 3)


def exp_x_fp_fn(x: float, z: float) -> float:
    """
    Returns the value g(x) for a given value of z.

    >>> round(exp_x_fp_fn(0.5, 2), 3)
    0.651
    >>> round(exp_x_fp_fn(1, 5), 3)
    1.041
    >>> exp_x_fp_fn(1, -2)
    Error: z must be positive
    >>> exp_x_fp_fn(0, 0)
    Error: z must be positive
    """
    if z <= 0:
        print("Error: z must be positive")
        return None
    
    return 0.5 * (z - math.exp(x) + 2 * x)


def ln_z_fixed_pt(z, x0, tol, num_iter):
    """
    Approximates ln(z) using the fixed-point method.

    >>> round(ln_z_fixed_pt(2, 1, 1e-10, 50), 5)
    0.69315
    """
    for _ in range(num_iter):
        x1 = exp_x_fp_fn(x0, z)
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    print("Warning: Did not converge within the specified number of iterations.")
    return x0

if __name__ == "__main__":
    import doctest
    doctest.testmod()
        >>> 
    """