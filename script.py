import codecademylib3
import pandas as pd
import numpy as np

# code goes here
diabetes_data = pd.read_csv('diabetes.csv')
print(diabetes_data.head())
print(diabetes_data.shape)
print(diabetes_data.isnull().sum())
print(diabetes_data.describe())
print(diabetes_data.isnull().sum())
print(diabetes_data.dtypes)
print(diabetes_data.Outcome.unique())
no_o = []
for i in diabetes_data.Outcome:
  no_o.append(i.replace('O','0'))

diabetes_data['Outcome'] = no_o
diabetes_data['Outcome'] = pd.to_numeric(diabetes_data['Outcome'])
print(diabetes_data.Outcome.dtype)