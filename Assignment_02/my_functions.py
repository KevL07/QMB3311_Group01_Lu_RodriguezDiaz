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
    #Not sure what this is about. If you knowm feel free to fix it
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

#def



# Exercise 3

#def



# Exercise 4

#def



# Exercise 5

#def



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

