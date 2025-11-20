import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

# 특정 기간동안 미국에서 코로나19 바이러스 확진자 수를 지역으로 나눠 정리한 데이터
usc = pd.read_csv('us_corona.csv')
usc['Date'] = pd.to_datetime(usc['Date']) # object -> datetime
usc = usc.set_index('Date').sort_values('Date') # index -> date and sorted date ascending
states = usc['Province/State'].unique()[:5]
# print(states)

usc = usc[usc['Province/State'].isin(states)]

# 6개월 단위 그룹으로 5개주(상위) 코로나19 발병 횟수 평균 값
print(usc.groupby([pd.Grouper(freq='6m'), 'Province/State']))
