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

def logit(x_i:float, beta_0:float, beta_1:float): # expected output? (-1)
    return math.exp(beta_0 + beta_1 * x_i) / (1 + math.exp(beta_0 + beta_1 * x_i))

# Exercise 1

def matrix_inverse(mat_in):
    """ Calculates the inverse of a two-by-two matrix using two nested loops.
    
    >>> matrix_inverse(np.array([[4,7],[2,6]]))
    array([[0.6,-0.2],
           [-0.7,0.4]])
    >>> matrix_inverse(np.array([[1,2],[3,4]]))
    array([[-2.0,1.5],
           [1.0,-0.5]])
    >>> matrix_inverse(np.array([[2,3],[4,6]]))
    None
    >>> matrix_inverse(np.array([[1,1],[1,1]]))
    None
    """
    # Test cases calculations incorrect (-2)
    # Test cases do not match output. (-2)
     det = mat_in[0, 0] * mat_in[1, 1] - mat_in[0, 1] * mat_in[1, 0]
    if det == 0:
        print("Matrix is not invertible.")
        return None
    mat_out = np.array([[mat_in[1, 1], -mat_in[0, 1]],[-mat_in[1, 0], mat_in[0, 0]]]) / det
    return mat_out
 
 
np.linalg.inv(np.array([[4,7],[2,6]])) # this is how to check the function you created (see how it differs from test cases)
np.linalg.inv(np.array([[1,2],[3,4]]))     
           
# Exercise 2

def logit_like_sum(y:list , x:list , beta_0, beta_1): # expected output? (-1) Incorrect function name (-1)
    """  Calculates the sum of the log-likelihood across all obersvation, 
    returning the sum of either the log of the function l(x; beta_0; beta_1) if
    y_i = 1 or the log of the function (1 - l(x; beta_0; beta_1)) if y_i = 0,
    over all observation.
    
    >>> logit_likelihood_sum([1, 0, 1], [2, 3, 5], 0.5, -0.2)
    -2.12
    >>> logit_likelihood_sum([0, 1, 1], [1, 4, 6], -0.3, 0.7)
    -2.25
    >>> logit_likelihood_sum([1, 1, 0], [2, 2, 2], 0.1, -0.1)
    -2.08
    """
# missing cases to check for issues in length of vectors matching and issues with y list (-2)
    logit_likelihood_summed = 0
    for i in range(len(y)):
        logit = math.exp(beta_0 + x[i] * beta_1) / (1 + math.exp(beta_0 + x[i] * beta_1)) # could have called logit funtion, better yet, logit_like
        if y[i] == 1:
            logit_sum = math.log(logit)
        elif y[i] == 0:
            logit_sum = math.log(1-logit)    
        logit_likelihood_summed += logit_sum
        
    return logit_likelihood_summed

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
    
    grad_beta0 = 0
    grad_beta1 = 0
    
    for i in range(len(y)):
        logit_2 = logit(x[i], beta_0, beta_1)
        
        grad_beta0 += (y[i] - logit_2) # clever, but needs error handling in above (what happens if y is not 1 or 0)? (-1)
        grad_beta1 += x[i] * (y[i] - logit_2)
    return [grad_beta0, grad_beta1] # to match test case output (-1)
    
    #logit_link_function = np.exp(beta_0 + beta_1 * x) / (1 + np.exp(beta_0 + beta_1 * x))
   #probability_error = y - logit_link_function
    
    #return [round(probability_error.sum(), 1), round((probability_error * x).sum(), 1)]                                                  
    #return [round(probability_error.sum(), 2), round((probability_error * x).sum(), 2)]    
                                                   
    
# Exercise 4

def CESutility_multi(x, a, r): # expected input/output? (-2)
    """ Evaluates the consumers utiity for more than two goods, where x is a
    vector of quantities of goods consumed and a is a vector of weighted
    parameters for each good and the subscript i indicates the ith element of 
    each vector
    
    >>> CESutility_multi([2, 3], [0.5, 0.5], 0.5)
    2.4
    >>> CESutility_multi([1, 2, 3], [0.3, 0.4, 0.3], 1)
    2.0
    >>> CESutility_multi([1, -2, 3], [0.3, 0.4, -0.3], 0.5)
    None
    """
    # Test cases calculations incorrect (-2)
    # failed to check lengths of vectors (-1)
    for i in x:
        if i < 0:
            print("x must be a nonnegative")
            return None
    
    for i in a:
        if i < 0:
            print("a must be a nonnegative")
            return None
    
    if r <= 0:
        print("r must be positive.")
    else:
        inside=0
        for i in range(len(x)):
            inside += a[i]**(1-r) * x[i]**r # failed to include a^(1-r)  (-2)
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

if __name__ == "__main__":

    with open("my_A4_functions.out", "w") as f:
        print(doctest.testmod(verbose = True), file = f)

##################################################
# End
##################################################

# Did not provide full output of doctest, only the number of pass fails (-3)