from pandas.io.parsers import count_empty_vals
import numpy as np
import pandas as pd


fruits = ["kiwi", "mango", "strawberry", "pineapple", "gala apple",
        "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi",
        "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]


fruits_series = pd.Series(fruits)


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