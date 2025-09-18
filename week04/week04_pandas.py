import numpy as np
import pandas as pd
import seaborn as sns

mpg = sns.load_dataset("mpg")
# print(mpg.isnull().sum())
# print(mpg[mpg['horsepower'].isnull()])
# 결측치 처리 #1
# mpg = mpg.dropna() # mpg.dropna(inplace=True)
# print(mpg[mpg['horsepower'].isnull()])

# 결측치 처리 #2
mpg = mpg.fillna(mpg['horsepower'].mean())
# print(mpg.fillna(mpg['horsepower'].isnull()))
# print(mpg)

# 결측치 처리 #3
mpg.drop(columns=['horsepower'], axis=1, inplace=True)
print(mpg.info())