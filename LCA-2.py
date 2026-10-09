#Q1- NumPy using sort function

import numpy as np

text = np.array([2, 3, 4, 1])
text = np.sort(text)[::-1]
print(text)

#Q2 - Accept two strings and concatenate

str1 = input("Enter your first name: ")
str2 = input("Enter your last name: ")
str_final = str1 + str2
print("Your full name is:", str_final)
