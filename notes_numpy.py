
import numpy as np
import pandas as pd

#This is a scratch pad to run random code and leave notes

""" Create block comment:  Shift + Option + A  """
""" Copy a line of code down: Shift + Option + Down """
""" Move by word:  Option + L or R"""
""" Move entire line upward or downward:  Option + Up or Down """
""" Highlight by word: Option + Shift """
""" Newline from anywhere:  Command + Enter """
""" Insert multiple cursor on select lines:  Option + Click """
""" Insert multiple cursors on hightlighted lines:  Shift + Alt + I"""
""" Highlight all occurance of a word:  Command + Shift + L """
""" Highlight next occurance of a word Command + D"""
""" Go to bottom of the page:  Command + Down """
""" Go to top of the page:  Command + up """
""" Delete a line:  Shift + Command + K """
""" Select line:  Command + L """





# a = np.array([1, 2, 3])

# matrix = np.array([[1, 2, 3],
#                    [4, 5, 6],
#                    [7, 8, 9]])

# print(matrix)
# print()

# # print(a[0])

# # print(matrix[0])

# # print(matrix[1, 1])

# print(matrix[1:, :2])
# print()
# print()
# print(matrix[2:, :2])

# should_include_elements = [True, False, True]
# print()
# print()
# print()
# print(should_include_elements)
# print(a)
# print(a[should_include_elements])

original_array = np.array([1, 2, 3, 4, 5])
#print(original_array + 1)

my_array = np.array([-3, 0, 3, 16])

# print(f'my_array      == {my_array}')
# print(f'my_array - 5  == {my_array - 5}')
# print(f'my_array * 4  == {my_array * 4}')
# print(f'my_array / 2  == {my_array / 2}')
# print(f'my_array ** 2 == {my_array ** 2}')
# print(f'my_array % 2  == {my_array % 2}')
# print()
# print()
# print()
my_array = np.array([-3, 0, 3, 16])

# print('my_array       == {}'.format(my_array))
# print('my_array == -3 == {}'.format(my_array == -3))
# print('my_array >= 0  == {}'.format(my_array >= 0))
# print('my_array < 10  == {}'.format(my_array < 10))

#print("this is the original data")
# print(my_array)
# print()
# print("check which is is even")
# step_1 = my_array % 2
# print("even results")
# print(step_1)
# step_2 = step_1 == 0
# print(step_2)
# step_3 = my_array[step_2]

# print(step_3)

# x = np.arange(15)

# print(x)

# print(np.zeros((2, 3)))
# print(np.zeros((4, 3)))
# print(np.full((2,4), 20))
# print(np.linspace(1, 20, 100))

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# How many even positive numbers are there?

mean = a.mean()
std = a.std()
b = (a-mean)/std
print(b)

a_centered = np.mean(a) - a
print(a_centered)
a_zscore = a_centered / np.std(a)
print(a_zscore)