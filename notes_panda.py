import numpy as np
import pandas as pd

number_series =pd.Series([100, 43, 26, 17, -17])
pd_numbers = pd.Series([100, 43, 26, 17, 17])
letters_series = pd.Series(['a', 'e', 'h', 'd', 'b', 'z'])
np_numbers = np.array([100, 43, 26, 17, 17])
string_series = pd.Series([' a a a a ', 'CodeuP', 'StUDenTs'])

#print(np.shape(np_numbers))
# print(pd_numbers+1)
# print(np_numbers+1)
# print()
# print()
# print()
# print(pd_numbers.index)
# print(pd_numbers.index.values)
# print(pd_numbers.values)
# print(pd_numbers.dtype)
# print(pd_numbers.size)
# print(pd_numbers.shape)

# print(pd_numbers.nlargest(n=1, keep='all'))
# print(pd_numbers.nsmallest(n=1, keep='all'))

# print(letters_series.sort_values())
# print(letters_series.sort_values(ignore_index=True))

print(string_series.str.replace(' ', '_'))

print((number_series > 0).any())
print((number_series > 0).all())