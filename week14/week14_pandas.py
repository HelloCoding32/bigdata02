import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pi = pd.read_csv('product_inspection.csv')
# print(pi.info())
# print(pi.describe())

pi['date'] = pd.to_datetime(pi['date'])
# print(pi.info())
# print(pi[pi['inspection_step'] == 'B'])
# print(pi['inspection_step'].unique())
# print(pi.groupby('inspection_step')['value'].mean())
# print(pi.groupby('inspection_step')['value'].describe())

# 새로운 특성 추가
pi['standard1'] = pi.groupby('inspection_step')['value'].transform(lambda x: (x - x.mean())/ x.std())
# print(pi.info())
# print(pi.tail(5))
# print(pi.groupby('inspection_step')['value'].mean() == 0)

# print(pi[pi['standard1'] < 0])

temp = pi.sort_values(['inspection_step','date']).drop_duplicates(['inspection_step'])
# print(temp)
temp = temp.set_index('inspection_step')['value']
# print(temp)

pi = pi.set_index('inspection_step')
# print(pi)

pi['standard2'] = pi['value'] - temp
# print(pi['standard2'])

pi = pi.reset_index()
print(pi)