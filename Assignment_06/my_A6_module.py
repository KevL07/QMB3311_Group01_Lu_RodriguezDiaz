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
import warnings

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
    Traceback (most recent call last):
        ...
    ValueError: z must be positive and not equal to 0
    """
    if z <= 0:
        raise ValueError("z must be positive and not equal to 0")
        
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
    Traceback (most recent call last):
        ...
    ValueError: z must be positive and not equal to 0
    >>> exp_x_diff(0, 0)
    Traceback (most recent call last):
        ...
    ValueError: z must be positive and not equal to 0
    """
    if z <= 0:
        raise ValueError("z must be positive and not equal to 0")
    
    return math.exp(x) - z


def ln_z_bisect(z: float, a_0: float, b_0: float, num_iter: int) -> float:
    """
    Produces an algorithm for calculating the natural logarithm of z. 

    >>> round(ln_z_bisect(2, 0, 2, 20), 3)
    0.693
    >>> round(ln_z_bisect(5, 1, 3, 30), 3)
    1.609
    >>> ln_z_bisect(2, 2, 3, 20)
    Traceback (most recent call last):
        ...
    ValueError: exp_x_diff must have opposite signs at the interval end points
    >>> ln_z_bisect(-1, 0, 2, 20)
    Traceback (most recent call last):
        ...
    ValueError: z must be positive and not equal to 0
    """
    f_a = exp_x_diff(a_0, z)
    f_b = exp_x_diff(b_0, z)

    if f_a * f_b >= 0:
        raise ValueError("exp_x_diff must have opposite signs at the interval end points")

    for _ in range(num_iter):
        m_i = (a_0 + b_0) / 2
        f_m = exp_x_diff(m_i, z)

        if f_m * f_a < 0:
            b_0 = m_i
            f_b = f_m
        else:
            a_0 = m_i
            f_a = f_m

    return round((a_0 + b_0) / 2, 3)


def exp_x_diff_prime(x: float, z: float) -> float:
    """
    Returns the derivative of exp_x_diff(x, z) with respect to x

    >>> round(exp_x_diff_prime(1, 2), 3)
    2.718
    >>> round(exp_x_diff_prime(2, 5), 3)
    7.389
    >>> exp_x_diff_prime(1, -2)
    Traceback (most recent call last):
        ...
    ValueError: z must be positive and not equal to 0
    >>> exp_x_diff_prime(0, 0)
    Traceback (most recent call last):
        ...
    ValueError: z must be positive and not equal to 0
    """
    if z <= 0:
        raise ValueError("z must be positive and not equal to 0")
    
    return math.exp(x)


def ln_z_newton(z: float, x0: float, tol: float, num_iter: int) -> float:
    """
    Approximates the natural log of z, ln(z), using Newton's method.

    >>> round(ln_z_newton(2, 1, math.pow(10, -10), 20), 3)
    0.693
    >>> round(ln_z_newton(5, 2, math.pow(10, -10), 20), 3)
    1.609
    >>> ln_z_newton(-1, 1, math.pow(10, -10), 20)
    Traceback (most recent call last):
        ...
    ValueError: z must be positive and not equal to 0
    """
    if z <= 0:
        raise ValueError("z must be positive and not equal to 0")

    for _ in range(num_iter):
        fx = exp_x_diff(x0, z)
        dfx = exp_x_diff_prime(x0, z)

        if abs(fx) < tol:
            return round(x0, 3)

        x0 = x0 - fx / dfx

    warnings.warn("Reached max iterations before exp_x_diff(x_i, z) < tol", RuntimeWarning)
    return round(x0, 3)


def exp_x_fp_fn(x: float, z: float) -> float:
    """
    Returns the value g_x for a given value of z.

    >>> round(exp_x_fp_fn(0.5, 2), 3)
    0.651
    >>> round(exp_x_fp_fn(1, 5), 3)
    1.041
    >>> exp_x_fp_fn(1, -2)
    Traceback (most recent call last):
        ...
    ValueError: z must be positive and not equal to 0
    >>> exp_x_fp_fn(0, 0)
    Traceback (most recent call last):
        ...
    ValueError: z must be positive and not equal to 0
    """
    if z <= 0:
        raise ValueError("z must be positive and not equal to 0")

    return 0.5 * (z - math.exp(x) + 2 * x)


def ln_z_fixed_pt(z: float, x0: float, tol: float, num_iter: int) -> float:
    """
    Approximates the natural log of z, ln(z), using the fixed point method.

    >>> round(ln_z_fixed_pt(2, 1, math.pow(10, -10), 30), 3)
    0.693
    >>> round(ln_z_fixed_pt(5, 1.5, math.pow(10, -10), 30), 3)
    1.609
    >>> ln_z_fixed_pt(-1, 1, math.pow(10, -10), 30)
    Traceback (most recent call last):
        ...
    ValueError: z must be positive and not equal to 0
    """
    if z <= 0:
        raise ValueError("z must be positive and not equal to 0")

    for _ in range(num_iter):
        xi_plus1 = exp_x_fp_fn(x0, z)

        if abs(xi_plus1 - x0) < tol:
            return round(xi_plus1, 3)

        x0 = xi_plus1

    warnings.warn("Reached max iterations before fixed point was found.", RuntimeWarning)
    return round(x0, 3)


if __name__ == "__main__":
    doctest.testmod()