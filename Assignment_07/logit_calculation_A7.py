# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 3311: Python for Business Analytics
#
# Computing Logistic Regression Coefficients
#
# Joshua Eubanks
# Department of Economics
# College of Business Administration
# University of Central Florida
#
##################################################
"""

import os
import pandas as pd
import statsmodels.api as sm
import numpy as np
from scipy.optimize import minimize

##################################################
# Set Working Directory
##################################################

git_path = 'C:\\Users\\anace\\OneDrive - University of Central Florida\\GitHub\\QMB3311_Group01_Lu_RodriguezDiaz'
os.chdir(git_path + '\\Assignment_07')

##################################################
# Load Data
##################################################

credit = pd.read_csv('credit_data.csv')

##################################################
# Inspect Data
##################################################

credit['default'].value_counts()
credit[['bmaxrate', 'amount', 'close', 'bankcardutil']].describe()
credit[['AA', 'A', 'B', 'C']].describe()

##################################################
# Logistic Regression with Statsmodels
##################################################

y = credit['default']
credit['Intercept'] = 1
X_cols = credit.columns[[10, 1]]  # Intercept, bmaxrate
X = credit[X_cols]

logit_model_sm = sm.Logit(y, X)
logit_model_fit_sm = logit_model_sm.fit()

print("\n--- Statsmodels Logistic Regression Coefficients ---")
print(logit_model_fit_sm.params)
print(logit_model_fit_sm.summary())

##################################################
# Likelihood and Gradient Tests
##################################################

import my_logit_A7 as my_logit

X_single = credit[credit.columns[1]]  # Only bmaxrate

print("\n--- Testing Likelihood Function ---")
beta = logit_model_fit_sm.params
print(my_logit.logit_like_sum_opt(beta, y, X_single))

print("\n--- Testing Gradient Function ---")
print(my_logit.logit_like_grad(beta, y, X_single))

##################################################
# Optimization Methods
##################################################

beta_0 = np.zeros(len(logit_model_fit_sm.params))

# Nelder-Mead
soln_nm = minimize(
    my_logit.logit_like_sum_opt,
    beta_0,
    args=(y.tolist(), X_single.tolist()),
    method='nelder-mead',
    options={'xtol': 1e-8, 'disp': True, 'maxiter': 1000}
)

print("\n--- Nelder-Mead Results ---")
print(soln_nm.x)
print(logit_model_fit_sm.params)
print(soln_nm.fun)
print(my_logit.logit_like_sum_opt(soln_nm.x, y, X_single))

# Powell (DFP)
soln_dfp = minimize(
    my_logit.logit_like_sum_opt,
    beta_0,
    args=(y.tolist(), X_single.tolist()),
    method='powell',
    options={'xtol': 1e-8, 'disp': True, 'maxiter': 1000}
)

print("\n--- Powell (DFP) Results ---")
print(soln_dfp.x)
print(logit_model_fit_sm.params)
print(soln_dfp.fun)
print(my_logit.logit_like_sum_opt(soln_dfp.x, y, X_single))

# BFGS without gradient
soln_bfgs = minimize(
    my_logit.logit_like_sum_opt,
    beta_0,
    args=(y.tolist(), X_single.tolist()),
    method='BFGS',
    options={'gtol': 1e-8, 'disp': True, 'maxiter': 1000}
)

print("\n--- BFGS (No Gradient) Results ---")
print(soln_bfgs.x)
print(logit_model_fit_sm.params)
print(soln_bfgs.fun)
print(my_logit.logit_like_sum_opt(soln_bfgs.x, y, X_single))

# BFGS with gradient
soln_bfgs_jac = minimize(
    my_logit.logit_like_sum_opt,
    beta_0,
    args=(y.tolist(), X_single.tolist()),
    method='BFGS',
    jac=my_logit.logit_like_grad,
    options={'gtol': 1e-8, 'disp': True, 'maxiter': 1000}
)

print("\n--- BFGS (With Gradient) Results ---")
print(soln_bfgs_jac.x)
print(logit_model_fit_sm.params)
print(soln_bfgs_jac.fun)
print(my_logit.logit_like_sum_opt(soln_bfgs_jac.x, y, X_single))

##################################################
# End
##################################################
