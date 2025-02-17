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
import sys
import doctest

##################################################
# Function Definitions
##################################################

# Only function definitions here - no other calculations. 

# Exercise 1

mat_in = np.array([[4,7], [2,6]])

def matrix_inverse(mat_in):
    """ Calculates the inverse of a two-by-two matrix using two nested loops.
    
    >>> matrix_inverse(np.array([[4, 7], [2, 6]]))
    array([[0.6, -0.7],
           [-0.2, 0.4]])
    >>> matrix_inverse(np.array([[1, 2], [3, 4]]))
    array([[-2.0, 1.0],
           [1.5, -0.5]])
    >>> matrix_inverse(np.array([[2, 3], [4, 6]]))
    None
    >>> matrix_inverse(np.array([[1, 1], [1, 1]]))
    None
    """
    
    det = mat_in[0,0] * mat_in[1,1] - mat_in[0,1] * mat_in[1,0]
    
    if det == 0:
        print("Error: Determined cannot be zero")
        return None
    else:
        mat_out = np.zeros((2,2))
        for i in range(2):
            for j in range(2):
                if i == 0 and j == 0:
                    mat_out[i, j] = mat_in[1,1] / det
                elif i == 0 and j == 1:
                    mat_out[i, j] = -mat_in[0,1] / det
                elif i == 1 and j == 0:
                    mat_out[i, j] = -mat_in[1,0] / det
                elif i == 1 and j == 1:
                    mat_out[i, j] = mat_in[0,0] / det
                
        return np.round(mat_out, 2)
                 
# Exercise 2

def logit_like(y, x, beta_0, beta_1):
    """Calculates the log-likelihood for a single observation.
    """
    probability = np.exp(beta_0 + beta_1 * x) / (1 + np.exp(beta_0 + beta_1 * x))
    
    if probability == 0:
        probability = 0.0000001  
    elif probability == 1:
        probability = 0.9999999  
    
    log_likelihood_function = y * np.log(probability) + (1 - y) * np.log(1 - probability)
    
    return log_likelihood_function 
    
def logit_like_sum(y, x, beta_0, beta_1):
    """  Calculates the sum of the log-likelihood across all obersvation, 
    returning the sum of either the log of the function l(x; beta_0; beta_1) if
    y_i = 1 or the log of the function (1 - l(x; beta_0; beta_1)) if y_i = 0,
    over all observation.
    
    >>> logit_like_sum([1, 0, 1], [2, 3, 5], 0.5, -0.2)
    -2.12
    >>> logit_like_sum([0, 1, 1], [1, 4, 6], -0.3, 0.7)
    -2.25
    >>> logit_like_sum([1, 1, 0], [2, 2, 2], 0.1, -0.1)
    -2.08
    """
    
    log_likelihood = 0
    
    for i in range(len(y)):
        log_likelihood += logit_like(y[i],x[i],beta_0,beta_1)
        
    return round(log_likelihood, 2)

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
    [-0.67, -2.0]
    """
    
    x = np.array(x)
    y = np.array(y)
    logit_link_function = np.exp(beta_0 + beta_1 * x) / (1 + np.exp(beta_0 + beta_1 * x))
    probability_error = y - logit_link_function
    gradient_beta_0 = round(np.sum(probability_error), 2)
    gradient_beta_1 = round(np.sum(probability_error * x), 2)
    
    return [gradient_beta_0, gradient_beta_1]                                                   
    
# Exercise 4

def CESutility_multi(x, a, r):
    """ Evaluates the consumer's utiity for more than two goods, where x is a
    vector of quantities of goods consumed and a is a vector of weighted
    parameters for each good and the subscript i indicates the ith element of 
    each vector
    
    >>> CESutility_multi([2, 3], [0.5, 0.5], 0.5)
    2.4
    >>> CESutility_multi([1, 2, 3], [0.3, 0.4, 0.3], 1)
    2.0
    >>> CESutility_multi([1, -2, 3], [0.3, 0.4, 0.3], 0.5)
    None
    """
    
    x = np.array(x)
    a = np.array(a)
    
    if min(x) < 0 or min(a) < 0:
        return None
    
    inside = sum(a[i] ** (1 - r) * x[1] ** r for i in range(len(x)))
        
    return round(inside ** (1/r), 1)

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

if __name__ == "__main__":
    with open("my_A4_functions.out", "w") as f:
        sys.stdout = f
        doctest.testmod(verbose = True)
        sys.stdout = sys.__stdout__
        
with open("my_A4_functions.out", "r") as f:
    print(f.read())

##################################################
# End
##################################################