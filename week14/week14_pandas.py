import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pr = pd.read_csv('product.csv')
# print(pr.info())
# print(pr.head())
# print(pr.tail())
# print(pr.describe())
# print(pr['operator'].unique())
# print(pr['process'].unique())
# print(pr['factory'].unique())

pr['path'] = pr.groupby('product_id')['operator'].transform(
    lambda x : '_'.join(x)
)
# print(pr.head(6))
# print(pr.tail(6))

pr['path'] = pr['factory'] + '_' + pr['path']
# print(pr.head(6))
pr = pr.drop_duplicates('product_id')
# print(pr)
pr = pr[['date','product_id','passfail','path']]
print(pr)
print(pr.groupby('passfail')['path'].value_counts())