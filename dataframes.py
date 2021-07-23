 from matplotlib.pyplot import nipy_spectral
from pandas.core.dtypes.generic import ABCRangeIndex
from pydataset import data
import numpy as np
import pandas as pd

# data('mpg', show_doc=True)
# view the documentation for the dataset
mpg = data('mpg') # load the dataset and store it in a variable

#print(mpg.head())
# All the datasets loaded from the pydataset library will be pandas dataframes.

# Create a column named passing_english that indicates whether each student has a passing grade in english.
np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})

#print(df.head())
# Sort the english grades by the passing_english column. How are duplicates handled?

df['passing_english'] = df.english > 70
#print(df['passing_english'])

# Sort the english grades first by passing_english and then by student name.
# All the students that are failing english should be first, and within the
# students that are failing english they should be ordered alphabetically.
# The same should be true for the students passing english.
# (Hint: you can pass a list to the .sort_values method)

print(df[['passing_english', 'name']].sort_values(by=['passing_english', 'name']))



# Sort the english grades first by passing_english, and then by the actual english grade, similar to how we did in the last step.


print(df[['passing_english', 'english']].sort_values(by=['passing_english', 'english']))

# Calculate each students overall grade and add it as a column on the dataframe. The overall grade is the average of the math, english, and reading grades.


df['overall_grade'] = (df.english + df.math + df.reading)/3

#print(df[['overall_grade']])
# Load the mpg dataset. Read the documentation for the dataset and use it for the following questions:

# How many rows and columns are there?

print(mpg.size)
# What are the data types of each column?

print(mpg.dtypes)
# Summarize the dataframe with .info and .describe

print(mpg.info())

print(mpg.describe())

# Rename the cty column to city.

mpg = mpg.rename(columns={'cty': 'city'})


# Rename the hwy column to highway.

mpg = mpg.rename(columns={'hwy': 'highway'})


# Do any cars have better city mileage than highway mileage?


print(mpg[mpg['city'] > mpg['highway']])

# Create a column named mileage_difference this column should contain the difference between highway and city mileage for each car.

mpg['mileage_difference'] = mpg.highway - mpg.city


# Which car (or cars) has the highest mileage difference?

print(mpg['mileage_difference'].nlargest(n=1, keep='all'))

# Which compact class car has the lowest highway mileage? The best?

#print(mpg[['class', 'highway']].sort_values(by=['highway', 'class'], ascending=False))
print(mpg[['class', 'highway']].where(mpg['class']=='compact').sort_values(by=['highway'], ascending=False).head(1))
print(mpg[['class', 'highway']].where(mpg['class']=='compact').sort_values(by=['highway'], ascending=True).head(1))

# Create a column named average_mileage that is the mean of the city and highway mileage.

mpg['average_mileage'] = (mpg.highway + mpg.city)/2

print(mpg.info())
# Which dodge car has the best average mileage? The worst?

print(mpg[['manufacturer', 'average_mileage']].where(mpg['manufacturer']=='dodge').sort_values(by=['average_mileage'], ascending=False).head(1))
print(mpg[['manufacturer', 'average_mileage']].where(mpg['manufacturer']=='dodge').sort_values(by=['average_mileage'], ascending=True).head(1))

# Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:

mam = data('Mammals')

print(mam.head())

# How many rows and columns are there?

print(mam.size)

# What are the data types?

print(mam.info())

# Summarize the dataframe with .info and .describe

print(mam.info())
print(mam.describe())

# What is the the weight of the fastest animal?

print(mam[['weight', 'speed']].sort_values(by=['speed'], ascending=False).head(1))

# What is the overal percentage of specials?

print(((mam['specials']).sum()/(mam['specials'].size)) *100)

# How many animals are hoppers that are above the median speed? What percentage is this?

#print((mam['speed']).median())

speed_median = (mam['speed']).median()



print(mam[['hoppers', 'speed']].where((mam['speed']>(mam['speed']).median()) & (mam['hoppers']==True)).\
sort_values(by=['speed'], ascending=False).dropna().count())





