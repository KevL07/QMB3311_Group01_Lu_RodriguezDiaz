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

import numpy as np
import doctest

##################################################
# Previous Functions
##################################################

# CES_utility() from Assignment 2

def CESutility(x:float, y:float, r:float) -> float:
    """Returns the theoretical degree of satisfaction gained by a consumer from
    the consumption of a certain number of good x and y considering r, the 
    degree to which the two goods are complements or subsitutes.
   
    # needs either a precondition or checks to make sure that variables are not negative (-1) 
   
    >>> CESutility(1,2,5)
    2.01
    >>> CESutility(2,2,2)
    2.83
    >>> CESutility(3,2.5,4.25)
    3.28 
    """
    
    # utility = (x**r)+(y**r) ** (1/r)
    
    utility = (pow(x,r) + pow(y,r)) ** (1/r) ## uses pow function inconsistently, but this is fine.
    
    return round(utility, 2)

# CES_utility_valid() from Assignment 3

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
    """ # indent the above to match the indent of rest of chunk for readability
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
    
    ans = CESutility(x, y, r)
    return ans

# CES_utility_in_budget() from Assignment 3

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

# CESdemand_calc() Function
 
def CESdemand_calc(r: float, p_x: float, p_y: float, w: float) -> list:
    """Calculates the optimal x* and y* values that maximize the function 
    CES_utility_in_budget(), without returning a value of None.
    
    >>> CESdemand_calc(2, 4, 4, 20)
    [10.0, 10.0]
    >>> CESdemand_calc(3, 2, 3, 30)
    [17.16, 12.84]
    >>> CESdemand_calc(1, 5, 10, 50)
    [33.33, 16.67]
    """
    
    # x* = (p_x ** (-1/r) / (p_x ** (-1/r) + p_y ** (-1/r))) * w
    # y* = (p_y ** (-1/r) / (p_x ** (-1/r) + p_y ** (-1/r))) * w
    
    denominator = (p_x ** (-1/r)) + (p_y ** (-1/r))
    optimal_x = (p_x ** (-1/r)) / denominator * w
    optimal_y = (p_y ** (-1/r)) / denominator * w

    return [round(optimal_x, 2), round(optimal_y, 2)]
 
# maximize_CES() Function

def maximize_CES(x_min: float, x_max: float, y_min: float, y_max: float, step: float, r: float, p_x: float, p_y: float, w: float) -> list:
    """Function that finds values of x and y that maximize 
    CESutility_in_budget(x, y, r, p_x, p_y, w) for given r, p_x, p_y, and w.

    >>> maximize_CES(0, 10, 0, 10, 0.5, 2, 4, 4, 20)
    [10.0, 10.0]
    >>> maximize_CES(0, 5, 0, 5, 1, 1, 2, 3, 10)
    [5.0, 5.0]
    >>> maximize_CES(0, 6, 0, 6, 2, 3, 2, 2, 30)
    [6.0, 6.0]
    """
    x_list = np.arange(x_min, x_max + step, step)
    y_list = np.arange(y_min, y_max + step, step)

    max_CES = float('-inf')
    # indices for optimal (x, y)
    i_max, j_max = 0, 0  

    for i in range(len(x_list)):
        for j in range(len(y_list)):
            utility = CESutility_in_budget(x_list[i], y_list[j], r, p_x, p_y, w)

            if utility != None and utility > max_CES:
                max_CES = utility
                i_max, j_max = i, j
                
    return (round(x_list[i_max], 2), round(y_list[j_max], 2))

# Run exercises - doctest

if __name__ == "__main__":
    doctest.testmod()




















