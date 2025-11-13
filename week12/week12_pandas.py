import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 다음주 apple 주가 데이터셋 하기 라고 말하기

wh = pd.read_csv('wh.csv')
# print(wh.describe())
# print(wh.query('Weight > 350'))
# new_wh = wh.query('Weight < 390')
# print(new_wh.info())

criteria = wh['Weight'].quantile(0.9999) # 99.99% 이상인 데이터 지점
print(criteria) # 약 255.9 파운드
print(round(criteria,1)) # 255.9 소수점 1번째 자리
new_wh = wh[wh['Weight'] < criteria]
print(new_wh.info())