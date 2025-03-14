# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 3311: Python for Business Analytics
#
# Name: Kevin Lu and Frances Rodriguez Diaz 
#
# Date: 3/14/2025
# 
##################################################
#
# Script for Assignment 5: 
#
##################################################
"""


##################################################
# Import Required Modules
##################################################

# import name_of_module

import math

##################################################
# Previous Functions
##################################################

# logit() from Assignment 3

def logit(x:float, beta_0:float, beta_1:float) -> float:
    """Calculates the logit link function

>>> logit(3,-2,0.7)
    0.52
>>> logit(1,0,1)
    0.73
>>> logit(-1,0.5,-0.8)
    0.79
    """
    logit_function_exponent = beta_0 + x * beta_1  
    logit_function = math.exp(logit_function_exponent) / (1 + math.exp(logit_function_exponent))
    
    return round(logit_function, 2)

    # logit_function = e ** (beta_0 + beta_1 * x) / (1 + e ** (beta_0 + beta_1 * x))

# logit_like() from Assignment 3

def log_likelihood(y_i:float, x_i:float, beta_0:float, beta_1:float) -> float:
    """Calculates the log-likelihood of observation (y; x), returning
 the natural log of the function "logit" if y = 1 or the log of the function 
 1 minus "logit" if y = 0
 
>>> log_likelihood(1,3,-2,0.7)
    -0.7
>>> log_likelihood(0,1,2,1)
    -3.0
>>> log_likelihood(1,2,3,4.5)
    0.0
>>> log_likelihood(2,3,0.4,-0.6)
    None
"""     
    logit_probability = logit(x_i, beta_0, beta_1)
     
    # if y = 1
    if y_i == 1:
        return math.log(logit_probability)
    # if y = 0
    elif y_i  == 0:
         return math.log(1 - logit_probability)
    else:
         print("y_i must equal 1 or 0; Event is likely to happen (1) or not (0)")
         return None

    # e ** (beta_0 + beta_1 * x_i) / (1 + e ** (beta_0 + beta_1 * x_i)) = a
    # if y_i = 0
    # log_e(1-(a))
    # if y_i = 1
    # log_e(a)

# logit_like_sum() from Assignment 4

def logit_like_sum(y:list , x:list , beta_0, beta_1): # expected output? (-1) Incorrect function name (-1)
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
# missing cases to check for issues in length of vectors matching and issues with y list (-2)
    y_error == False
    length_error == False
    for i in y:
        if i != 1 and i != 0:
            y_error == True
    if y_error == True:
        print("Y must be 0 or 1")
    if len(x) != len(y):
        print("X and Y list must match in length")
        length_error == True
    if y_error == True or length_error == True:
        return None
    logit_likelihood_summed = 0
    for i in range(len(y)):
        if y[i] in [0,1]:
            logit_likelihood_summed_i = logit_like(y[i], x[i], beta_0, beta_1)
            logit_likelihood_summed  =  logit_likelihood_summed + logit_likelihood_summed_i
    return logit_likelihood_summed 

# helper function 






















