import pandas as pd
import seaborn as sns
from scipy.stats import linregress
import matplotlib.pyplot as plt

uber = pd.read_csv("Uber.csv")
uber['START_DATE*'] = pd.to_datetime(uber['START_DATE*'], errors='coerce')
uber['END_DATE*'] = pd.to_datetime(uber['END_DATE*'])
uber.drop(1155, inplace=True)
uber['DURATION*'] = (uber['END_DATE*'] - uber['START_DATE*']).dt.total_seconds() / 60
slope, intercept, r, _, _ = linregress(uber['MILES*'], uber['DURATION*'])
print(slope)
print(intercept)
print(r)


sns.regplot(x='MILES*', y='DURATION*', data=uber, line_kws={'label': f'y={slope:.2f}, R^2={r:.2f}'})
plt.legend()
plt.show()
