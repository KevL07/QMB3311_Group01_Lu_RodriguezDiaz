# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 3311: Python for Business Analytics
#
# Name: Kevin Lu and Frances Rodriguez Diaz
#
# Date:1/20/2025
#
##################################################
#
# Sample Script for Assignment 2:
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

# Exercise 1

def present_value(cash_flow: float, interest_rate: float, num_yrs: float) -> float:
    """Return the present value of cash_flow expected num_yrs from now
    discounted at interest_rate.

    >>> present_value(110, 0.10, 1)
    100.0
    >>> present_value(121, 0.10, 2)
    100.0
    >>> present_value(134, 0.10, 3)
    100.7
    """
    answer = cash_flow / (1 + interest_rate) ** num_yrs

    return round(answer, 1)

    # PV = CF / (1 + r) ** t

# Define the rest of your functions for Exercises 2-5.

# Exercise 2
def future_value(cash_flow:float, discount_rate:float, years:float) -> float:
    """Returns the future cash value of a present cash flow, discounted a certain number of
    years at an interest rate.
    
>>> future_value(100,0.05,5)
    127.63
>>> future_value(100,0.05,10)
    162.89
>>> future_value(500.5,0.15,2.5)
    709.82
    """
    value = cash_flow * (1 + discount_rate) ** years
    return round(value,2)
print(future_value())

# FV = PV * (1 + r) ** t


# Exercise 3

def total_revenue(price:float, units:float) -> float:
    """Returns the total revenue of a firm given the price 
    and number of units.
    
>>> total_revenue(10,100)
    1000.00   
>>> total_revenue(5.25,40)   
    210
>>> total_revenue(7.34,10.5) 
    77.07  
    """
    revenue = price * units 
    return round(revenue,2)
print(total_revenue(10,100))

# TR = P * Q

# Exercise 4

def total_cost(units:float, x:float, fixed_cost:float) -> float:
    """Returns the total cost of a firm given the fixed 
    cost, a constant variable called x, and number of units.
    
>>> total_cost(10,1,50)
    150.00 
>>> total_cost(25.25,2.5,125.5)   
    1719.41
>>> total_cost(1,0.5,100.5) 
    101.00  
    """
    cost = x * (units ** 2) + fixed_cost
    return round(cost,2)
print(total_cost())


# Exercise 5

def CESutility(x:float, y:float, r:float) -> float:
    """Returns the amount of utility gained from consuming
    good x and good y given the degree to which the two
    goods are complements or subsitutes.
    
>>>CESutility(1,2,5)
   2.01
>>>CESutility(2,2,2)
   2.83
>>>CESutility(.5,2.5,4.25)
   2.5 
    """
    utility = (pow(x,r) + pow(y,r)) ** (1/r)
    return round(utility,2)
print(CESutility())


##################################################
# Run the examples to test these functions
##################################################


# Test the examples and print the results.


print("#" + 50*"-")
print("Testing my Examples for Exercise 1.")
print("#" + 50*"-")
print("Exercise 1, Example 1:")
print("Evaluating present_value(110, 0.10, 1)")
print("Expected: " + str(100.0))
print("Got: " + str(present_value(110, 0.10, 1)))


print("#" + 50*"-")
print("Exercise 1, Example 2:")
print("Evaluating present_value(121, 0.10, 2)")
print("Expected: " + str(100.0))
print("Got: " + str(present_value(121, 0.10, 2)))


print("#" + 50*"-")
print("Exercise 1, Example 3:")
print("Evaluating present_value(132, 0.10, 3)")
print("Expected: " + str(100.7))
print("Got: " + str(present_value(134, 0.10, 3)))


print("#" + 50*"-")
print("Testing my Examples for Exercise 2.")
# Code goes here.

# ...


# Continue with the rest of your examples.
# Test all functions with three examples each.

# Choose good examples that will test interesting cases.
# Make sure they all work correctly.


##################################################
# End
##################################################

