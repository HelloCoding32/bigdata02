import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


apple = pd.read_csv('APPL_price.csv')

apple['Date'] = pd.to_datetime(apple['Date']) # object -> datetime
apple = apple.set_index('Date') # index를 날짜시간 칼럼으로 대체
apple = apple.reset_index('Date') # index를 날짜시간 칼럼으로 대체
apple['Daily_Return'] = apple['Close'].pct_change() * 100
apple['Price_Change'] = apple['Close'].diff()
apple['High_Low_Range'] = ((apple['High'] - apple['Low'])/apple['Low']) * 100
apple['Volattility'] = apple['Daily_Return'].rolling(window=20).std()

apple['Year'] = apple['Date'].dt.year
yearly_stats = apple.groupby('Year')['Close'].agg(
    [('최고', 'max'),
    ('최저', 'min'),
    ('평균', 'mean'),
    ('개수', 'count'),
     ])
# print(yearly_stats)

apple['Month'] = apple['Date'].dt.month
monthly_stats = apple.groupby('Month')['Close'].mean()
# print(monthly_stats.tail(12))

# 분기별 수익율 분석
apple['Quarter'] = apple['Date'].dt.quarter
quarterly_return = apple.groupby(['Year','Quarter'])['Close'].sum()
# print(quarterly_return)

# 거래량이 많은 날 분석
# print(apple['Volume'])
apple['Volume_Category'] = pd.cut(apple['Volume'],
                                  bins=[0,100000000,300_000_000,5e8,10e9],
                                  labels=['Low','Medium','High','Very High']
                                  )
volume_analysis = apple.groupby(['Volume_Category'])['Close'].agg(['count', 'mean'])

# 최근 2년 데이터
recent_2year = apple[apple['Date'] >= '2020-06-17']

# 가격 100달러 이상
high_price_days = apple[apple['Close'] >= 100]

# 수익율 양수인 날
positive_return = apple[apple['Daily_Return'] > 0]

# 거래량이 상위 5%에 해당하는 날
hi_volume_threashold = apple['Volume'].quantile(0.95)
# print(hi_volume_threashold)
high_volume_days = apple[apple['Volume'] >= hi_volume_threashold]
# print(high_volume_days)

apple_filtered = apple[(apple['Date'] >= '2020-01-01') & (apple['Close'] >= 50) &
                       (apple['Volume'] > 2e8)]
# print(apple_filtered)

print(apple.columns)
plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots(figsize=(14,6))

# ax.plot(apple['Date'], apple['MA_20'],linewidth=2, label='20-day MA',
#         linestyle='--', alpha=0.7)
# plt.show()

ax.plot(apple['Date'], apple['Close'],linewidth=2, label='close price ',
        linestyle='--', alpha=1)
plt.show()