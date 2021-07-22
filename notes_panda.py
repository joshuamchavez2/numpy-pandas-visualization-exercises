from pandas.core import groupby
from pandas.core.reshape.concat import concat
from pandas.core.reshape.merge import merge_ordered
from pydataset import data
import numpy as np
import pandas as pd
from env import host, user, password

def get_db_url(url='employees'):
    url = f'mysql+pymysql://{user}:{password}@{host}/{url}'
    return url

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

