from pandas.core.reshape.concat import concat
from pydataset import data
import numpy as np
import pandas as pd

# # number_series =pd.Series([100, 43, 26, 17, -17])
# # pd_numbers = pd.Series([100, 43, 26, 17, 17])
# # letters_series = pd.Series(['a', 'e', 'h', 'd', 'b', 'z'])
# # np_numbers = np.array([100, 43, 26, 17, 17])
# # string_series = pd.Series([' a a a a ', 'CodeuP', 'StUDenTs'])

# # #print(np.shape(np_numbers))
# # # print(pd_numbers+1)
# # # print(np_numbers+1)
# # # print()
# # # print()
# # # print()
# # # print(pd_numbers.index)
# # # print(pd_numbers.index.values)
# # # print(pd_numbers.values)
# # # print(pd_numbers.dtype)
# # # print(pd_numbers.size)
# # # print(pd_numbers.shape)

# # # print(pd_numbers.nlargest(n=1, keep='all'))
# # # print(pd_numbers.nsmallest(n=1, keep='all'))

# # # print(letters_series.sort_values())
# # # print(letters_series.sort_values(ignore_index=True))

# # # print(string_series.str.replace(' ', '_'))

# # # print((number_series > 0).any())
# # # print((number_series > 0).all())

# # s = pd.Series(list(range(15)))
# # s

# # def total_vowels(input_value):
# #     count = 0
# #     #vowels = ['a', 'e', 'i', 'o', 'u']
# #     for value in input_value:
# #         if value in 'aeiou':
# #             count = count + 1
# #     return count

# # print(pd.cut(s, 3))
# # example = pd.Series(["a", "i","o", "u", "l", 'm'])
# # print((example.apply(total_vowels)).sum())


# # series = pd.Series(["python", "is", "awesome"])
# # last = pd.Series([series[0]])
# # series = series.append(last)
# # print(list(series[1:series.size]))

# # series = pd.Series([1, 1, 1, 2, 4, 9])
# # series = pd.Series([["ant", "ant", "mosquito", "mosquito", "ladybug"], ["juice","ant", "gin"]])
# # new_series =series.apply(pd.Series).stack().reset_index(drop = True)


# # print(list(new_series.value_counts()[new_series.value_counts().values > 1].index))

# # ser1 = pd.Series([1, 2, 3, 4, 5])
# # ser2 = pd.Series([3, 4, 5, 6, 7])
# # union = pd.Series(np.union1d(ser1, ser2))
# # intersect = pd.Series(np.intersect1d(ser1, ser2))
# # notcommonseries = union[~union.isin(intersect)]
# # print(notcommonseries)

# #concat testing

# # print(users)
# # print(roles)
# # print("#######################################################")
# #cat_outter_join = pd.concat([users, roles], axis=1, join='outer')
# #cat_inner_join = pd.concat([users, roles], axis=1, join='inner')
# # print(outter_join)
# # print(inner_join)
# # print("#######################################################")
# # outter_join = pd.concat([users, roles], axis=0, join='outer')
# # inner_join = pd.concat([users, roles], axis=0, join='inner')
# # print(outter_join)
# # print(inner_join)
# # print("#######################################################")

# #merge testing

# # print('users')
# # print(users)
# # print('roles')
# # print(roles)
# # print("#######################################################")
# # merge_right_join = users.merge(roles, left_on='role_id', right_on='id', how='right', indicator=True)
# # merge_left_join = users.merge(roles, left_on='role_id', right_on='id', how='left', indicator=True)
# # merge_inner_join = users.merge(roles, left_on='role_id', right_on='id', how='inner', indicator=True)
# # merge_outer_join = users.merge(roles, left_on='role_id', right_on='id', how='outer', indicator=True)
# # print("right join###############")
# # print(right_join)
# # print("left join################")
# # print(left_join)
# # print("inner join###############")
# # print(inner_join)
# # print("outter join################")
# # print(outer_join)



# # Copy the users and roles DataFrames from the examples above.

# users = pd.DataFrame({
#     'id': [1, 2, 3, 4, 5, 6],
#     'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
#     'role_id': [1, 2, 3, 3, np.nan, np.nan]
# })

# roles = pd.DataFrame({
#     'id': [1, 2, 3, 4],
#     'name': ['admin', 'author', 'reviewer', 'commenter']
# })

# merge_right_join = users.merge(roles, left_on='role_id', right_on='id', how='right', indicator=True)
# merge_left_join = users.merge(roles, left_on='role_id', right_on='id', how='left', indicator=True)
# merge_inner_join = users.merge(roles, left_on='role_id', right_on='id', how='inner', indicator=True)
# merge_outer_join = users.merge(roles, left_on='role_id', right_on='id', how='outer', indicator=True)


# # What is the result of using a right join on the DataFrames?

# print(merge_right_join)

# # What is the result of using an outer join on the DataFrames?

# print(merge_outer_join)

# # What happens if you drop the foreign keys from the DataFrames and try to merge them?

# '''I got an error at first, then we I deleted lefton and righton i got empty dataframe'''

# # Load the mpg dataset from PyDataset.

# mpg = data('mpg')
# # Output and read the documentation for the mpg dataset.

# data('mpg', show_doc=True)

# # How many rows and columns are in the dataset?

# print(mpg.shape)

# # Check out your column names and perform any cleanup you may want on them.

# print(mpg.value_counts())

# # Display the summary statistics for the dataset.

# print(mpg.describe())

# # How many different manufacturers are there?

# print(mpg["manufacturer"].value_counts().size)

# # How many different models are there?

# print(mpg['model'].value_counts().size)

# # Create a column named mileage_difference like you did in the DataFrames exercises;
# # this column should contain the difference between highway and city mileage for each car.

# mpg['mileage_difference'] = mpg.hwy - mpg.cty


# # Create a column named average_mileage like you did in the DataFrames exercises;
# # this is the mean of the city and highway mileage.

# mpg['average_mileage'] = (mpg.hwy + mpg.cty)/2

# # Create a new column on the mpg dataset named is_automatic that holds boolean values denoting whether the car has an automatic transmission.

# mpg['is_automatic'] = np.where(mpg.trans.str.contains("auto"), True, False)
# # Using the mpg dataset, find out which which manufacturer has the best miles per gallon on average?

# print(mpg.groupby('manufacturer').average_mileage.max().sort_values(ascending=False).head(1))

# # Do automatic or manual cars have better miles per gallon?

# auto = mpg.average_mileage[mpg.trans.str.contains("auto")].mean()
# manual = mpg.average_mileage[mpg.trans.str.contains("manual")].mean()

# print(auto>manual)