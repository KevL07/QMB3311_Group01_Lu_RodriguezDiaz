# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 3311: Python for Business Analytics
#
# Name: Frances Rodriguez Diaz and Kevin Lu
#
# Date: 2/17/2025
# 
##################################################
#
# Sample Script for Assignment 4: 
# Function Definitions
#
##################################################
"""


##################################################
# Import Required Modules
##################################################

# import name_of_module

import numpy as np
import math
import doctest

##################################################
# Function Definitions
##################################################

# Only function definitions here - no other calculations. 

# Exercise 1

mat_in = np.array([[4,7],[2,6]])

def matrix_inverse(mat_in):
    """ Computes the inverse of a 2x2 matrix.
    
>>> matrix_inverse(np.array([[4, 7], [2, 6]]))
    array([[0.6, -0.7],
           [-0,2, 0.4]])
>>> matrix_inverse(np.array([[1, 2], [3, 4]]))
    array([[-2, 1 ]
           1.5, -0.5]])
>>> matrix_inverse(np.array([[2, 3], [4, 6]]))
    None
    """
          
    det = mat_in[0,0] * mat_in[1,1] - mat_in[0,1] * mat_in[1,0]
    
    if det == 0:
        print("Error: Determined cannot be zeero")
        return None
    else:
        mat_out = np.zeros((2,2))
        for i in range(2):
            for j in range(2):
                mat_out[i,j] = ((-1) ** (i+j) * mat_in[1-i,1-j])/det
                
        return mat_out
    
    matrix_inverse(mat_in)
    
    np.linalg.inv(mat_in)
                 
# Exercise 2

def logit_like_sum(y,x,beta_0,beta_1):
    
    log_likelihood = 0
    for i in range(len(y)):
        log_likelihood += logit_like(y[i],x[i],beta_0,beta_1)

# Exercise 3

def logit_like_grad(y: list, x: list, beta_0: float, beta_1: float) -> float:
    """Calculates the gradient vector of the likelihood function
    for the bivariate logistic regression model
    for sevaral pairs of observations in the lists x and y,
    coefficients beta_0 and beta_1.
    
    Notice if you are missing the space after the >>>, 
    it causes an error.
    Also, an example without the >>> does not get run with doctest.
    
    >>> logit_like_grad([1, 1, 0, 0], [15.0, 5.0, 15.0, 5.0], 0.0, 0.0)
    [0.0, 0.0]
    >>> logit_like_grad([1, 1, 0, 0], [15.0, 5.0, 15.0, 5.0], math.log(3), 0.0)
    [-1.0, -10.0]
    >>> logit_like_grad([1, 1, 0, 0], [15.0, 5.0, 15.0, 5.0], math.log(7), 0.0)
    [-1.5, -15.0]
    >>> logit_like_grad([1, 0, 1], [1, 1, 1], 0.0, math.log(2))
    [0.0, 0.0]
    >>> logit_like_grad([1, 0, 1], [1, 1, 1], 0.0, math.log(5))
    [-0.5, -0.5]
    >>> logit_like_grad([1, 0, 1], [3, 3, 3], 0.0, math.log(2))
    [-2/3, -2.0]
    """
    
    return None

# Exercise 4

def CESutility_multi(x,a,r):
    
    inside = 0
    for i in range(len(x)):
        inside += a[i]**(1-r)*x[i]**r
        
    return inside ** (1/r)

# Only function definitions above this point. 


##################################################
# Test the examples in your docstrings
##################################################


# Question 2: Test using the doctest module. 


# Make sure to include exampes in your docstring
# with the proper formatting. 

# Test all functions with three examples each. 

# Choose good examples that will test interesting cases. 
# Make sure they all work correctly. 




##################################################
# End
##################################################

