import numpy as np
import pandas as pd
import seaborn as sns

mpg = sns.load_dataset("mpg")
# print(mpg.value_counts())

df = pd.DataFrame({
    'city': ['seoul','anyang','incheon','seoul','seoul','anyang'],
    'name': ['tom','Jerry','kim','park','park','lee']},
    index=[1,2,3,4,5,6])

# print(df)
# print(df.value_counts())
print(df['city'].nunique())