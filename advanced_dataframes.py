from env import host, user, password
import pandas as pd
import numpy as np

# Run python -m pip install mysqlclient pymysql from your terminal to install the mysql client (any folder is fine)
# cd into your exercises folder for this module and run echo env.py >> .gitignore

# Create a function named get_db_url. It should accept a username, hostname, password, and database name and return a url connection string formatted like in the example at the start of this lesson.
def get_db_url(url):
    url = f'mysql+pymysql://{user}:{password}@{host}/{url}'
    return url

url = f'mysql+pymysql://{user}:{password}@{host}/employees'

employees = pd.read_sql('SELECT * FROM employees LIMIT 5 OFFSET 50', url)

titles = pd.read_sql('SELECT * FROM titles LIMIT 5 OFFSET 50', url)




# Use your function to obtain a connection to the employees database.
employees = pd.read_sql('SELECT * FROM employees', get_db_url("employees"))

titles = pd.read_sql('SELECT * FROM titles', get_db_url("employees"))



# # Once you have successfully run a query:

# # a. Intentionally make a typo in the database url. What kind of error message do you see?

# # Very long Errors

# # b. Intentionally make an error in your SQL query. What does the error message look like?

# # More long Errors

# # Read the employees and titles tables into two separate DataFrames.

print(employees)
print(titles)

# # How many rows and columns do you have in each DataFrame? Is that what you expected?

print(employees.shape)
print(titles.shape)

# # Display the summary statistics for each DataFrame.

print(employees.describe())
print(titles.describe())

# # How many unique titles are in the titles DataFrame?

print(len(titles.title.unique()))

print(type(employees))

# # What is the oldest date in the to_date column?

print(titles.to_date.min())

# # What is the most recent date in the to_date column?

print(titles.to_date.max())