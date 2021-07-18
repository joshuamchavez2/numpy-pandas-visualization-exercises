from pandas.core.algorithms import value_counts
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


fruits = ["kiwi", "mango", "strawberry", "pineapple", "gala apple",
        "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi",
        "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]

string_of_letters_list = list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy')
fruits_series = pd.Series(fruits)
letters = pd.Series(string_of_letters_list)


print(fruits_series)
# Determine the number of elements in fruits.

print(fruits_series.count())

# Output only the index from fruits.

print(fruits_series.index.values)

# Output only the values from fruits.

print(fruits_series.values)

# Confirm the data type of the values in fruits.

print(fruits_series.dtype)

# Output only the first five values from fruits. Output the last three values.
# Output two random values from fruits.

print(fruits_series.head(5))
print(fruits_series.tail(3))
print(fruits_series.sample(2))

# Run the .describe() on fruits to see what information it returns when called on a Series with string values.

print(fruits_series.describe())

# Run the code necessary to produce only the unique string values from fruits.

unique_fruits = fruits_series.unique()
print(type(unique_fruits))
print(type(pd.unique(fruits)))

# Determine how many times each unique string value occurs in fruits.

print(fruits_series.value_counts())

# Determine the string value that occurs most frequently in fruits.

print(fruits_series.mode())


# Determine the string value that occurs least frequently in fruits.
 
min_value = min(fruits_series.value_counts())
least_frequent = fruits_series.value_counts() ==1
print(least_frequent[least_frequent])

# Capitalize all the string values in fruits.

print(fruits_series.apply(lambda n: n.capitalize()))
#or
print(fruits_series.str.capitalize())

# Count the letter "a" in all the string values (use string vectorization).

print(fruits_series.str.count('a'))

# Output the number of vowels in each and every string value.

def total_vowels(input_value):
    count = 0
    #vowels = ['a', 'e', 'i', 'o', 'u']
    for value in input_value:
        if value in 'aeiou':
            count = count + 1
    return count

print(fruits_series.apply(total_vowels))

# Write the code to get the longest string value from fruits.


def string_count(input_value):
    return len(input_value)

new_series = fruits_series.apply(string_count)
largest_in_string = new_series.nlargest(n=1, keep="all")
print(largest_in_string.values)

#or

print(fruits_series.apply(lambda x:len(x)).nlargest(n=1, keep="all").values)

# Write the code to get the string values with 5 or more letters in the name.

def string_values(input_value):
    if len(input_value) >=5:
        return True
    else:
        return False

new_series = fruits_series.apply(string_values).values
print(fruits_series[new_series])

# Use the .apply method with a lambda function to find the fruit(s) containing the letter "o" two or more times.

def contains_o(input_value):
    if input_value.count('o') >=2:
        return input_value

print(fruits_series[fruits_series.apply(lambda x : True if x.count('o') >= 2 else False)])

# Write the code to get only the string values containing the substring "berry".


new_series = fruits_series.apply(lambda x : True if 'berry' in x else False)
print(fruits_series[new_series])

# Write the code to get only the string values containing the substring "apple".

new_series = fruits_series.apply(lambda x : True if 'apple' in x else False)
print(fruits_series[new_series])

# Which string value contains the most vowels?

new_series = fruits_series.apply(total_vowels).nlargest(n=1, keep="all")

print(fruits_series.loc[new_series.index[0]])

# Which letter occurs the most frequently in the letters Series?

print(letters.value_counts().nlargest(n=1, keep="all"))

# Which letter occurs the Least frequently?

print(letters.value_counts().nsmallest(n=1, keep="all"))

# How many vowels are in the Series?
vowels = (letters.apply(total_vowels)).sum()
print(vowels)

# How many consonants are in the Series?

print(letters.size - vowels)

# Create a Series that has all of the same letters but uppercased.
uppercase_letters = letters.apply(lambda x: x.upper())
print(uppercase_letters)
# Create a bar plot of the frequencies of the 6 most commonly occuring letters.

frequencies = letters.value_counts().nlargest(n=6, keep='all')

frequencies.plot.bar()

plt.show()

# Use pandas to create a Series named numbers from the following list:


numbers = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])
# What is the data type of the numbers Series?

print(type(numbers))
# How many elements are in the number Series?

print(numbers.size)
# Perform the necessary manipulations by accessing Series attributes
# and methods to convert the numbers Series to a numeric data type.

numbers_float = numbers.str.replace("$", "").str.replace(",", "").astype(float)
print(numbers_float)

# Run the code to discover the maximum value from the Series.

print(numbers_float.nlargest(n=1, keep="all").values[0])

# Run the code to discover the minimum value from the Series.

print(numbers_float.nsmallest(n=1, keep="all").values[0])

# What is the range of the values in the Series?

print(str(numbers_float.nsmallest(n=1, keep="all").values[0]) + "-" + str(numbers_float.nlargest(n=1, keep="all").values[0]))

# Bin the data into 4 equally sized intervals or bins and output how many values fall into each bin.

binned_data = pd.cut(numbers_float, 4, labels=["0 - 1.9M", "1.9M - 2.39M", "2.39 - 3.59",  "3.59M - 4.78M"]).value_counts()

#Plot the binned data in a meaningful way. Be sure to include a title and axis labels.
plt.clf()
binned_data.plot.bar()
plt.title('My Binned Data')
plt.ylabel('Frequency')
plt.xticks(rotation=0)
plt.xlabel('Ranged Values')
plt.show()

# Use pandas to create a Series named exam_scores from the following list:


exam_scores = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])
# How many elements are in the exam_scores Series?

print(exam_scores.size)

# Run the code to discover the minimum, the maximum, the mean, and the median scores for the exam_scores Series.

print(exam_scores.describe())
# Plot the Series in a meaningful way and make sure your chart has a title and axis labels.

binned_exam_scores = pd.cut(exam_scores, bins=[0, 60, 70, 80, 90, 100], labels=["F", "D", "C","B", "A"]).value_counts().sort_values(ascending = False)
plt.clf()
binned_exam_scores.plot.bar()
plt.title('Grades')
plt.ylabel('Frequency')
plt.xticks(rotation=0)
plt.xlabel('Grade')
plt.show()


# Write the code necessary to implement a curve for your exam_grades Series and save this as curved_grades.
# Add the necessary points to the highest grade to make it 100, and add the same number of points to every
# other score in the Series as well.

highest_score = int(exam_scores.nlargest(n=1).values)
print(highest_score)

curved_exam_scores = exam_scores.apply(lambda x: x+ (100-highest_score))
print(curved_exam_scores)

# Use a method to convert each of the numeric values in the curved_grades Series into a categorical value of
# letter grades. For example, 86 should be a 'B' and 95 should be an 'A'. Save this as a Series named letter_grades.

binned_curved_scores = pd.cut(curved_exam_scores, bins=[0, 60, 70, 80, 90, 100], labels=["F", "D", "C","B", "A"]).value_counts()

# Plot your new categorical letter_grades Series in a meaninful way and include a title and axis labels.

plt.clf()
binned_exam_scores.plot.line(legend = True, label='Exam Scores')
binned_curved_scores.plot.line(legend = True, label='Curved Scores')
plt.title('Grades')
plt.ylabel('Frequency')
plt.xlabel('Grade')
plt.show()