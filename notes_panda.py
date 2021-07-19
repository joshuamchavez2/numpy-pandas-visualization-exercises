import numpy as np
import pandas as pd

# number_series =pd.Series([100, 43, 26, 17, -17])
# pd_numbers = pd.Series([100, 43, 26, 17, 17])
# letters_series = pd.Series(['a', 'e', 'h', 'd', 'b', 'z'])
# np_numbers = np.array([100, 43, 26, 17, 17])
# string_series = pd.Series([' a a a a ', 'CodeuP', 'StUDenTs'])

# #print(np.shape(np_numbers))
# # print(pd_numbers+1)
# # print(np_numbers+1)
# # print()
# # print()
# # print()
# # print(pd_numbers.index)
# # print(pd_numbers.index.values)
# # print(pd_numbers.values)
# # print(pd_numbers.dtype)
# # print(pd_numbers.size)
# # print(pd_numbers.shape)

# # print(pd_numbers.nlargest(n=1, keep='all'))
# # print(pd_numbers.nsmallest(n=1, keep='all'))

# # print(letters_series.sort_values())
# # print(letters_series.sort_values(ignore_index=True))

# # print(string_series.str.replace(' ', '_'))

# # print((number_series > 0).any())
# # print((number_series > 0).all())

# s = pd.Series(list(range(15)))
# s

# def total_vowels(input_value):
#     count = 0
#     #vowels = ['a', 'e', 'i', 'o', 'u']
#     for value in input_value:
#         if value in 'aeiou':
#             count = count + 1
#     return count

# print(pd.cut(s, 3))
# example = pd.Series(["a", "i","o", "u", "l", 'm'])
# print((example.apply(total_vowels)).sum())






# series = pd.Series(["python", "is", "awesome"])
# last = pd.Series([series[0]])
# series = series.append(last)
# print(list(series[1:series.size]))



series = pd.Series([1, 1, 1, 2, 4, 9])
series = pd.Series([["ant", "ant", "mosquito", "mosquito", "ladybug"], ["juice","ant", "gin"]])
new_series =series.apply(pd.Series).stack().reset_index(drop = True)


print(list(new_series.value_counts()[new_series.value_counts().values > 1].index))


ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([3, 4, 5, 6, 7])
union = pd.Series(np.union1d(ser1, ser2))
intersect = pd.Series(np.intersect1d(ser1, ser2))
notcommonseries = union[~union.isin(intersect)]
print(notcommonseries)
