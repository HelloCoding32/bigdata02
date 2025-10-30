import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 다음주 apple 주가 데이터셋 하기 라고 말하기

wh = pd.read_csv('wh.csv')
# print(wh.describe())
sns.scatterplot(x='Weight',y='Height',data=wh)
plt.show()