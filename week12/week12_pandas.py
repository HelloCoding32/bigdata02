import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

usc = pd.read_csv('us_corona.csv')
# print(usc.info())
# print(usc.describe())

usc.fillna('Daelim',inplace=True)
print(usc.query('Admin2 == "Daelim"'))