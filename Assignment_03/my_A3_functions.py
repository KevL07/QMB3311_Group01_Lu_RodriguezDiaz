# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 3311: Python for Business Analytics
#
# Name: Kevin Lu and Frances Rodriguez Diaz 
#
# Date: 2/3/2025
# 
##################################################
#
# Sample Script for Assignment 3: 
# Function Definitions
#
##################################################
"""


##################################################
# Import Required Modules
##################################################

# import name_of_module

import math



##################################################
# Function Definitions
##################################################

# Only function definitions here - no other calculations. 

# Exercise 1
def CESutility_valid(x:float, y:float,r:float) -> float:
    """Returns the theoretical degree of satisfaction gained by a consumer from
    the consumption of a non-negative amount of good x and y considering r, the
    positive degree to which the two goods are complements or subsitutes.
    
>>> CESutility_valid(-1,2,5)
    None
>>> CESutility_valid(2,-2,2)
    None
>>> CESutility_valid(3,2.5,0)
    None
>>> CESutility_valid(3,2.5,4.25)
    3.28
    """
    error = False
    if x < 0:
        error = True
        print("x cannot be negative.")
    if y < 0:
        error = True
        print("y cannot be negative.")     
    if r <= 0:
        error = True
        print("r must be positive.")
    if error == True:
        return None
    
    ans = (pow(x,r) + pow(y,r)) ** (1/r)
    return round(ans,2)
    
    # utility = (x**r) + (y**r) ** (1/r)
    # print(CESutility_valid())
    

# ...

# Define the rest of your functions for Exercises 2-4.

def CESutility_in_budget(x:float, y:float, r:float, p_x:float, p_y:float, w:float) -> float:
    """Evaluates whether a consumer's mix of goods x and y are in budget 
    considering the specific customer's wealth (w) alongside prices p_x and p_y.
    
>>> CESutility_in_budget(2,3,3,-1,2,20)
    None
>>> CESutility_in_budget(0,2,4,1,-3,20)
    None
>>> CESutility_in_budget(1,2,-5,3,4,20)
    None
>>> CESutility_in_budget(10,15,3,6,6,20)
    None
>>> CESutility_in_budget(1.25,2,4,4,4,20)
    2.07
    """
    # Checks if prices are negative
    if p_x < 0 or p_y < 0:
        print("Price cannot be negative.")
        return None
    # Checks if the consumer basket of goods costs more than wealth
    if(p_x * x + p_y * y) > w:
        print("The consumer basket of goods cannot cost more than wealth.")
        return None
    
    return CESutility_valid(x, y, r)
    
    # utility = (x**r)+(y**r) ** (1/r)
    
from math import exp

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
    logit_function = exp(logit_function_exponent) / (1 + exp(logit_function_exponent))
    
    return round(logit_function, 2)

    # logit_function = e ** (beta_0 + beta_1 * x) / (1 + e ** (beta_0 + beta_1 * x))

from math import log

def log_likelihood(y_i:float, x_i:float, beta_0:float, beta_1:float) -> float:
    """Calculates the log-likelihood of observation (y; x), returning
 the log of the function "logit" if y = 1 or the log of the function 
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
        return round(log(logit_probability), 2)
    # if y = 0
    elif y_i  == 0:
         return round(log(1 - logit_probability), 2)
    else:
         print("y_i must equal 1 or 0; Event is likely to happen (1) or not (0)")
         return None

    # e ** (beta_0 + beta_1 * x_i) / (1 + e ** (beta_0 + beta_1 * x_i)) = a
    # if y_i = 0
    # log(1-(a))
    # if y_i = 1
    # log(a)
    
# Only function definitions above this point. 

##################################################
# Run the examples to test these functions
##################################################


# Code goes here.
# Exercise 1 examples and results

print("#" + 50*"-")
print("Testing my Examples for Exercise 1.")
print("#" + 50*"-")
print("Exercise 1, Example 1:")
print("Evaluating CESutility_valid(-1,2,5)")
print("Expected: " + str("x cannot be negative."))
print("Got: " + str(CESutility_valid(-1,2,5)))

print("#" + 50*"-")
print("Exercise 1, Example 2:")
print("Evaluating CESutility_valid(2,-2,2)")
print("Expected: " + str("y cannot be negative."))
print("Got: " + str(CESutility_valid(2,-2,2)))

print("#" + 50*"-")
print("Exercise 1, Example 3:")
print("Evaluating CESutility_valid(3,2.5,0)")
print("Expected: " + str("r must be positive."))
print("Got: " + str(CESutility_valid(3,2.5,0)))

print("#" + 50*"-")
print("Exercise 1, Example 4:")
print("Evaluating CESutility_valid(3,2.5,4.25)")
print("Expected: " + str(3.28))
print("Got: " + str(CESutility_valid(3,2.5,4.25)))

# Exercise 2 examples and results
    
print("#" + 50*"-")
print("Testing my Examples for Exercise 2.")
print("#" + 50*"-")
print("Exercise 2, Example 1:")
print("Evaluating CESutility_in_budget(2,3,3,-1,2,20)")
print("Expected: " + str("Price cannot be negative."))
print("Got: " + str(CESutility_in_budget(2,3,3,-1,2,20)))

print("#" + 50*"-")
print("Exercise 2, Example 2:")
print("Evaluating CESutility_in_budget(0,2,4,1,-3,20)")
print("Expected: " + str("Price cannot be negative."))
print("Got: " + str(CESutility_in_budget(0,2,4,1,-3,20)))

print("#" + 50*"-")
print("Exercise 2, Example 3:")
print("Evaluating CESutility_in_budget(1,2,-5,3,4,20)")
print("Expected: " + str("r must be positive"))
print("Got: " + str(CESutility_in_budget(1,2,-5,3,4,20)))

print("#" + 50*"-")
print("Exercise 2, Example 4:")
print("Evaluating CESutility_in_budget(10,15,3,6,6,20)")
print("Expected: " + str("The consumer basket of goods cannot cost more than wealth."))
print("Got: " + str(CESutility_in_budget(10,15,3,6,6,20)))

print("#" + 50*"-")
print("Exercise 2, Example 5:")
print("Evaluating CESutility_in_budget(1.25,2,4,4,4,20)")
print("Expected: " + str("2.07"))
print("Got: " + str(CESutility_in_budget(1.25,2,4,4,4,20)))

# Exercise 3 examples and results

print("#" + 50*"-")
print("Testing my Examples for Exercise 3.")
print("#" + 50*"-")
print("Exercise 3, Example 1:")
print("Evaluating logit(3,-2,0.7)")
print("Expected: " + str("0.52"))
print("Got: " + str(logit(3,-2,0.7)))

print("#" + 50*"-")
print("Exercise 3, Example 2:")
print("Evaluating logit(1,0,1)")
print("Expected: " + str("0.73"))
print("Got: " + str(logit(1,0,1)))

print("#" + 50*"-")
print("Exercise 3, Example 3:")
print("Evaluating logit(-1,0.5,-0.8)")
print("Expected: " + str("0.79"))
print("Got: " + str(logit(-1,0.5,-0.8)))
      
# Exercise 4 examples and results
    
print("#" + 50*"-")
print("Testing my Examples for Exercise 4.")
print("#" + 50*"-")
print("Exercise 4, Example 1:")
print("Evaluating log_likelihood(1,3,-2,0.7)")
print("Expected: " + str("-0.7"))
print("Got: " + str(log_likelihood(1,3,-2,0.7)))

print("#" + 50*"-")
print("Exercise 4, Example 2:")
print("Evaluating log_likelihood(0,1,2,1)")
print("Expected: " + str("-3.0"))
print("Got: " + str(log_likelihood(0,1,2,1)))
    
print("#" + 50*"-")
print("Exercise 4, Example 3:")
print("Evaluating log_likelihood(1,2,3,4.5)")
print("Expected: " + str("0.0"))
print("Got: " + str(log_likelihood(1,2,3,4.5)))
    
print("#" + 50*"-")
print("Exercise 4, Example 4:")
print("Evaluating log_likelihood(2,3,0.4,-0.6)")
print("Expected: " + str("y_i must equal 1 or 0; Event is likely to happen (1) or not (0)"))
print("Got: " + str(log_likelihood(2,3,0.4,-0.6)))
    
##################################################
# End
##################################################