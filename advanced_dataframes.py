from env import host, user, password
import pandas as pd
import numpy as np
from pydataset import data

###############################################################################################
# Exercises Part I
###############################################################################################

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

'''Very long Errors'''

# # b. Intentionally make an error in your SQL query. What does the error message look like?

'''More long Errors'''

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

###############################################################################################
# Exercises Part II
###############################################################################################
# Copy the users and roles DataFrames from the examples above.

users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})

roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})

merge_right_join = users.merge(roles, left_on='role_id', right_on='id', how='right', indicator=True)
merge_left_join = users.merge(roles, left_on='role_id', right_on='id', how='left', indicator=True)
merge_inner_join = users.merge(roles, left_on='role_id', right_on='id', how='inner', indicator=True)
merge_outer_join = users.merge(roles, left_on='role_id', right_on='id', how='outer', indicator=True)


# What is the result of using a right join on the DataFrames?

print(merge_right_join)

# What is the result of using an outer join on the DataFrames?

print(merge_outer_join)

# What happens if you drop the foreign keys from the DataFrames and try to merge them?

'''I got an error at first, then we I deleted lefton and righton i got empty dataframe'''

# Load the mpg dataset from PyDataset.

mpg = data('mpg')
# Output and read the documentation for the mpg dataset.

data('mpg', show_doc=True)

# How many rows and columns are in the dataset?

print(mpg.shape)

# Check out your column names and perform any cleanup you may want on them.

print(mpg.value_counts())

# Display the summary statistics for the dataset.

print(mpg.describe())

# How many different manufacturers are there?

print(mpg["manufacturer"].value_counts().size)

# How many different models are there?

print(mpg['model'].value_counts().size)

# Create a column named mileage_difference like you did in the DataFrames exercises;
# this column should contain the difference between highway and city mileage for each car.

mpg['mileage_difference'] = mpg.hwy - mpg.cty


# Create a column named average_mileage like you did in the DataFrames exercises;
# this is the mean of the city and highway mileage.

mpg['average_mileage'] = (mpg.hwy + mpg.cty)/2

# Create a new column on the mpg dataset named is_automatic that holds boolean values denoting whether the car has an automatic transmission.

mpg['is_automatic'] = np.where(mpg.trans.str.contains("auto"), True, False)
# Using the mpg dataset, find out which which manufacturer has the best miles per gallon on average?

print(mpg.groupby('manufacturer').average_mileage.max().sort_values(ascending=False).head(1))

# Do automatic or manual cars have better miles per gallon?

auto = mpg.average_mileage[mpg.trans.str.contains("auto")].mean()
manual = mpg.average_mileage[mpg.trans.str.contains("manual")].mean()

print(auto>manual)

###############################################################################################
# Exercises Part III
###############################################################################################
# Use your get_db_url function to help you explore the data from the chipotle database.

def get_db_url(url):
    url = f'mysql+pymysql://{user}:{password}@{host}/{url}'
    return url

# What is the total price for each order?

chip = pd.read_sql('SELECT item_price, order_id  FROM orders', get_db_url("chipotle"))
cleaned_itemprice = chip['item_price'].str.replace("$", "").str.replace(",", "").astype('float')
chip["int_price"] = cleaned_itemprice
print(chip.head())
print(chip.groupby("order_id").int_price.sum())

# What are the most popular 3 items?

chip = pd.read_sql('SELECT item_name, quantity  FROM orders', get_db_url("chipotle"))
print(chip.groupby("item_name").quantity.sum().sort_values(ascending=False).head(3))

# Which item has produced the most revenue?

print(chip.groupby("item_name").quantity.sum().sort_values(ascending=False).idxmax())

# Join the employees and titles DataFrames together.

joined = pd.read_sql("Select title, to_date, from_date From employees JOIN titles\
    ON titles.emp_no  = employees.emp_no Where to_date > now()", get_db_url("employees"))

print(joined)

# For each title, find the hire date of the employee that was hired most recently with that title.

print(joined.groupby("title").from_date.max())

# Write the code necessary to create a cross tabulation of the number of titles by department.
# (Hint: this will involve a combination of SQL code to pull the necessary data and python/pandas
# code to perform the manipulations.)

#Grab all information from all the tables im going to need using SQL
employee = pd.read_sql("Select * From employees", get_db_url())
titles = pd.read_sql("SELECT * FROM titles", get_db_url())
departments = pd.read_sql("SELECT * FROM departments", get_db_url())
dept_emp = pd.read_sql("SELECT * FROM dept_emp", get_db_url())

#Rename the titles and dept_emp to_date/from_date since they have the name column name in their Tables
titles = titles.rename(columns={
    "to_date": "titles_to_date",
    "from_date": "titles_from_date"
})

dept_emp = dept_emp.rename(columns={
    "to_date": "dept_emp_to_date",
    "from_date": "dept_emp_from_date"
})

#Merge all the tables together using inner joins
merged_table = employee.merge(titles, left_on='emp_no', right_on='emp_no', how='inner')
merged_table = merged_table.merge(dept_emp, left_on='emp_no', right_on='emp_no', how='inner')
merged_table = merged_table.merge(departments, left_on='dept_no', right_on='dept_no', how='inner')

#print(merged_table.head())
print(pd.crosstab(merged_table.title, merged_table.dept_name))