import numpy as np
import pandas as pd
import seaborn as sns

mpg = sns.load_dataset("mpg")
# print(mpg.isnull().sum())
# print(mpg.isnull())
# print(mpg[mpg['horsepower'].isnull() == True])
# print(mpg[mpg['horsepower'].isnull()])
mpg_nan = mpg[mpg['horsepower'].isnull()]
print(mpg_nan.loc[:,'mpg':'horsepower'])
