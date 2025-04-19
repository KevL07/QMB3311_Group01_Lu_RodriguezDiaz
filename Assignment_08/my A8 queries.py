#!/usr/bin/python
"""
##################################################
# 
# QMB 3311: Python for Business Analytics
# 
# Using Databases with SQLite3
# 
# Joshua Eubanks
# Department of Economics
# College of Business
# University of Central Florida
# 
# April 16, 2023
# 
# Sample Program for Assignment 8
# 
##################################################
"""


##################################################
# Import Modules.
##################################################


import os # To set working directory
import pandas as pd # To read and inspect data


# To estimate linear regression models
import statsmodels.formula.api as sm
import sqlite3



##################################################
# Set Working Directory.
##################################################


# Find out the current directory.
os.getcwd()
# Change to a new directory.
git_path = ''
drive_path = os.getcwd() + '/'  # Add your drive path logic here if needed
os.chdir(drive_path + git_path + 'assignment_08')
# Check that the change was successful.
os.getcwd()


##################################################
### Question 1: A Single Table
##################################################


# a. Create a new database called credit.db.

#--------------------------------------------------
# Code goes here.
con = sqlite3.connect('credit.db')
cur = con.cursor()
#--------------------------------------------------


# b. Read in the applications.csv dataset 
# and store the contents in a data frame 
# called applications in your workspace.

#--------------------------------------------------
applications = pd.read_csv('applications.csv')
#--------------------------------------------------


# Verify the contents of the data frame.
applications.dtypes

# Inspect a few rows of data.
applications.head(3)
applications.tail(3)

# Check the dimensions of the data.
applications.index
applications.columns

# Inspect the keys.
applications[['app_id', 'ssn', 'zip_code']].describe()

# Inspect the continuous variables.
applications[['purchases', 'income', 'credit_limit']].describe()

# Inspect the categorical variable.
applications['homeownership'].value_counts()


# c. Estimate a regression model.

# Fit the regression model.
fmla_str = "purchases ~ income + homeownership + credit_limit"
reg_model_sm = sm.ols(formula = fmla_str, 
                           data = applications).fit()

# Display a summary table of regression results.
print(reg_model_sm.summary())


# d. CREATE a TABLE called Applications with a schema 
# that is appropriate for the variables.

#--------------------------------------------------
cur.execute("DROP TABLE IF EXISTS Applications")
cur.execute('''
    CREATE TABLE Applications (
        app_id INTEGER,
        ssn TEXT,
        zip_code INTEGER,
        income REAL,
        homeownership TEXT,
        purchases REAL,
        credit_limit INTEGER
    )
''')
#--------------------------------------------------

# e. Populate the table Applications with the observations
applications.to_sql('Applications', con, if_exists='append', index=False)

# Retrieve the contents of the table to check.
cur.execute('SELECT * FROM Applications')
for row in cur.fetchall()[1:20]:
 print(row)


##################################################
### Question 2: Two Tables
##################################################


# a. Read in the credit_bureau.csv dataset 
# and store the contents in a data frame 
# called credit_bureau in your workspace.

#--------------------------------------------------
credit_bureau = pd.read_csv('credit_bureau.csv')
#--------------------------------------------------

# Verify the contents of the data frame.
credit_bureau.dtypes

# Inspect a few rows of data.
credit_bureau.head(3)
credit_bureau.tail(3)

# Check the dimensions of the data.
credit_bureau.index
credit_bureau.columns

# Inspect the keys.
credit_bureau[['ssn', 'zip_code']].describe()

# Inspect the continuous variables.
credit_bureau[['fico', 'num_late']].describe()

# Inspect the categorical variables.
credit_bureau[['num_late']].value_counts()
credit_bureau[['past_def']].value_counts()
credit_bureau[['num_bankruptcy']].value_counts()


# b. CREATE a TABLE called CreditBureau with a schema 
# that is appropriate for the variables.

#--------------------------------------------------
cur.execute("DROP TABLE IF EXISTS CreditBureau")
cur.execute('''
    CREATE TABLE CreditBureau (
        ssn TEXT,
        zip_code INTEGER,
        fico INTEGER,
        num_late INTEGER,
        past_def INTEGER,
        num_bankruptcy INTEGER
    )
''')
#--------------------------------------------------


# c. Populate the table CreditBureau 
# with the observations in the data frame credit_bureau.

#--------------------------------------------------
credit_bureau.to_sql('CreditBureau', con, if_exists='append', index=False)
#--------------------------------------------------

# Retrieve the contents of the table to check.
cur.execute('SELECT * FROM CreditBureau')
for row in cur.fetchall()[1:20]:
 print(row)


# d. Join the two tables by ssn and zip code 
# and output the result as a 
# pandas data frame called app_bureau.

#--------------------------------------------------
query2 = '''
    SELECT *
    FROM Applications A
    JOIN CreditBureau C
    ON A.ssn = C.ssn AND A.zip_code = C.zip_code
'''
app_bureau = pd.read_sql_query(query2, con)
#--------------------------------------------------

# Verify the contents of the data frame.
app_bureau.dtypes

# Inspect a few rows of data.
app_bureau.head(3)
app_bureau.tail(3)

# Check the dimensions of the data.
app_bureau.index
app_bureau.columns

# Inspect the keys.
app_bureau[['app_id', 'ssn', 'zip_code']].describe()

# Inspect the continuous variables.
app_bureau[['income', 'purchases', 'credit_limit', 
            'fico']].describe()

# Inspect the categorical variables.
app_bureau[['homeownership']].value_counts()
app_bureau[['num_late']].value_counts()
app_bureau[['past_def']].value_counts()
app_bureau[['num_bankruptcy']].value_counts()


# e. Estimate a regression model.

# Fit the regression model.
fmla_str_app = "purchases ~ income + homeownership + credit_limit"
new_vars_cr = "fico + num_late + past_def + num_bankruptcy"
fmla_str = fmla_str_app + " + " + new_vars_cr

reg_model_sm = sm.ols(formula = fmla_str, 
                           data = app_bureau).fit()

# Display a summary table of regression results.
print(reg_model_sm.summary())



##################################################
### Question 3: Three Tables
##################################################


# a. Read in the demographic.csv dataset 
# and store the contents in a data frame 
# called demographic in your workspace.

#--------------------------------------------------
demographic = pd.read_csv('demographic.csv')
#--------------------------------------------------

# Verify the contents of the data frame.
demographic.dtypes

# Inspect a few rows of data.
demographic.head(3)
demographic.tail(3)

# Check the dimensions of the data.
demographic.index
demographic.columns

# Inspect the key.
demographic[['zip_code']].describe()

# Inspect the continuous variables.
demographic[['avg_income', 'density']].describe()



# b. CREATE a TABLE called Demographic with a schema 
# that is appropriate for the variables.

#--------------------------------------------------
cur.execute("DROP TABLE IF EXISTS Demographic")
cur.execute('''
    CREATE TABLE Demographic (
        zip_code INTEGER,
        avg_income REAL,
        density REAL
    )
''')
#--------------------------------------------------


# c. Populate the table Demographic 
# with the observations in the data frame demographic.

#--------------------------------------------------
demographic.to_sql('Demographic', con, if_exists='append', index=False)
#--------------------------------------------------

# Retrieve the contents of the table to check.
cur.execute('SELECT * FROM Demographic')
for row in cur.fetchall()[1:20]:
 print(row)


# d. Join the new table Demographic to the 
# information from the other two tables by zip code. 
# You can use your query from Question 2 as a nested query.
# Output the result as a 
# pandas data frame called purchase_full.

#--------------------------------------------------
query3 = '''
    SELECT *
    FROM (
        SELECT *
        FROM Applications A
        JOIN CreditBureau C
        ON A.ssn = C.ssn AND A.zip_code = C.zip_code
    ) AS AB
    JOIN Demographic D
    ON AB.zip_code = D.zip_code
'''
purchase_full = pd.read_sql_query(query3, con)
#--------------------------------------------------

# Verify the contents of the data frame.
purchase_full.dtypes

# Inspect a few rows of data.
purchase_full.head(3)
purchase_full.tail(3)

# Check the dimensions of the data.
purchase_full.index
purchase_full.columns

# Inspect the keys.
purchase_full[['app_id', 'ssn', 'zip_code']].describe()

# Inspect the continuous variables.
purchase_full[['income', 'purchases', 'credit_limit',  
            'fico']].describe()
purchase_full[['avg_income', 'density']].describe()

# Inspect the categorical variables.
purchase_full[['homeownership']].value_counts()
purchase_full[['num_late']].value_counts()
purchase_full[['past_def']].value_counts()
purchase_full[['num_bankruptcy']].value_counts()



# e. Estimate a regression model.

# Fit the regression model.
fmla_str_app = "purchases ~ income + homeownership + credit_limit"
new_vars_cr = "fico + num_late + past_def + num_bankruptcy"
new_vars_dem = "avg_income + density"

fmla_str = fmla_str_app + " + " + new_vars_cr + " + " + new_vars_dem

reg_model_sm = sm.ols(formula = fmla_str, 
                           data = purchase_full).fit()

# Display a summary table of regression results.
print(reg_model_sm.summary())



##################################################
# Commit changes and close the connection
##################################################


# The commit method saves the changes. 
con.commit()


# Close the connection when finished. 
con.close()

# Then we can continue with this file when you have time
# to work on it later.



##################################################
# Extra code snippets
##################################################

# In case things go wrong, you can always drop the table
# and start over:
# cur.execute('DROP TABLE Applications')
# cur.execute('DROP TABLE CreditBureau')
# cur.execute('DROP TABLE Demographic')

# This can get the schema of each of the tables:
# cur.execute("PRAGMA table_info('Applications')").fetchall()
# cur.execute("PRAGMA table_info('CreditBureau')").fetchall()
# cur.execute("PRAGMA table_info('Demographic')").fetchall()
# which states the names of the variables and the data types.



##################################################
# End
##################################################
