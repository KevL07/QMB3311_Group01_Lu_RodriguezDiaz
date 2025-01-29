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




##################################################
# Function Definitions
##################################################

# Only function definitions here - no other calculations. 

# Exercise 1
    
def CESutility_valid(x:float, y:float, r:float) -> float:
    """Returns the theoretical degree of satisfaction gained by a consumer from
    the consumption of a non-negative amount of good x and y considering r, the
    positive degree to which the two goods are complements or subsitutes.
    
>>> CESutility_valid(-1,2,5)
    None
>>> CESutility_valid(2,-2,2)
    None
>>> CESutility_valid(3,2.5,0)
    None
>>> CESutility_valid(3,2.25,4.25)
    3.19
    """
    if x < 0:
        print("x cannot be negative. Please enter a non-negative amount.")
        return None
    elif y < 0:
        print("y cannot be negative. Please enter a non-negative amount.")
        return None
    elif r <=0:
        print("r cannot be negative or zero. Please enter a positive number.")
        return None 
    
    utility = (pow(x,r) + pow(y,r)) ** (1/r)
    return round(utility, 2)
    #print(CESutility_valid())

    # utility = (x**r)+(y**r) ** (1/r)

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
    >>> CESutility_in_budget(1,2,4,4,4,20)
    
    """
    # Checks if prices are negative
    if p_x < 0 or p_y < 0:
        return None
    # Checks if the consumer basket of goods costs more than wealth
    if(p_x * x + p_y * y) > w:
        return None
    
    return CESutility_valid(x, y, r)
    
# Only function definitions above this point. 


##################################################
# Run the examples to test these functions
##################################################


# Code goes here.
#Exercise 1 examples and results

print("#" + 50*"-")
print("Testing my Examples for Exercise 1.")
print("#" + 50*"-")
print("Exercise 1, Example 1:")
print("Evaluating CESutility_valid(-1,2,5)")
print("Expected: " + str("x cannot be negative. Please enter a non-negative number."))
print("Got: " + str(CESutility_valid(-1,2,5)))

print("#" + 50*"-")
print("Exercise 1, Example 2:")
print("Evaluating CESutility_valid(2,-2,2)")
print("Expected: " + str("y cannot be negative. Please enter a non-negative number."))
print("Got: " + str(CESutility_valid(2,-2,2)))

print("#" + 50*"-")
print("Exercise 1, Example 3:")
print("Evaluating CESutility_valid(3,2.5,0)")
print("Expected: " + str("r cannot be negative or zero. Please enter a positive number."))
print("Got: " + str(CESutility_valid(3,2.5,0)))

print("#" + 50*"-")
print("Exercise 1, Example 4:")
print("Evaluating CESutility_valid(3,2.25,4.25)")
print("Expected: " + str(3.19))
print("Got: " + str(CESutility_valid(3,2.25,4.25)))


##################################################
# End
##################################################