import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

# 특정 기간동안 미국에서 코로나19 바이러스 확진자 수를 지역으로 나눠 정리한 데이터
usc = pd.read_csv('us_corona.csv')
usc['Date'] = pd.to_datetime(usc['Date']) # object -> datetime
# print(usc.info())
usc = usc.set_index('Date').sort_values('Date') # index -> date and sorted date ascending
# print(usc)

# print(usc['2021-09' : '2021-10']) # slicing
# print(usc.reset_index().set_index('Province/State').sort_index())
usc = usc.reset_index().set_index('Province/State').sort_index()
print(len(usc.index.unique()))