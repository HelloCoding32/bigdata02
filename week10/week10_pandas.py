import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

german = pd.read_csv('german.csv')
print()
print(pd.qcut(german['Age'], q=8).reset_index().groupby('Age').size())