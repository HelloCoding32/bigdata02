import numpy as np
import pandas as pd
import seaborn as sns

mpg = sns.load_dataset("mpg")
# print(mpg.info())
# print(mpg.head(3))
# print(mpg.tail(3))

# mpg_desc = mpg.sort_values(by=['mpg'], ascending=False)
# print(mpg_desc)

# print(mpg.describe())

# print(mpg[mpg['mpg'] > 40])
print(mpg.query('mpg > 40'))

# print(mpg.drop_duplicates())

df = pd.DataFrame({
    'date' : ['2025-09-11', '2025-09-11', '2025-09-12','2025-09-11'],
    'city' : ['서울','안양','서울','안양'],
    'temp' : [23,22,24,22]
}, index =[1, 2, 3,4])

# print(df.drop_duplicates())

# print(mpg.nlargest(5,'mpg'))
# print(mpg.nsmallest(7   ,'mpg'))
# print(mpg[['displacement','horsepower','weight']])

# print(mpg.iloc[:,2:7])
# print(mpg.loc[:,'displacement':'model_year'])

# print(mpg.filter(regex='p..er'))