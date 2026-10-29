import pandas as pd
import numpy as np

data = {'StudentID': [1, 2, 3, 4, 5, 6, 7], 
        'Name': ['Aman', 'Bhavna', 'Chetan', 'Divya', 'Esha', 'Bhavna', 'Farhan'], 
        'Marks': [85.0, np.nan, 78.0, 92.0, np.nan, np.nan, 88.0], 
        'City': ['Pune', 'Mumbai', np.nan, 'Delhi', 'Pune', 'Mumbai', 'Delhi']
            }
df = pd.DataFrame(data)
print(df)   

print("Missing Values: ")
print(df.isnull().sum())    

np.mean_marks = df['Marks'].mean()
df['Marks'].fillna(np.mean_marks, inplace=True)
df['City'].fillna('Unknown', inplace=True)
print("\nDataFrame after handling missing values: ")
print(df)

print("Remove Duplicate Rows:")
df.drop_duplicates(inplace=True)
print(df)

print("Filtering Students with Marks > 80 using loc[]") 
high_scorers = df.loc[df['Marks'] > 80, ['StudentID', 'Name', 'Marks', 'City']]
print(high_scorers)
