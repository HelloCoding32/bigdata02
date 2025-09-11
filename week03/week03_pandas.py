import pandas as pd

df1 = pd.DataFrame({'A':[1,2,3], 'B':[4,5,6],'C':[7,8,9]}, index=[1,2,3])

# print(df1)
# print()

df2 = pd.DataFrame([
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
], index =[1, 2, 3], columns=['A', 'B', 'C'])
# print(df2)

df3 = pd.melt(df2).rename(columns={'variable' : 'var', 'value' : 'val'}).query('val  > 5')
# print(df3)



df4 = pd.DataFrame({
    'date' : ['2025-09-11', '2025-09-11', '2025-09-12','2025-09-12'],
    'city' : ['서울','안양','서울','안양'],
    'temp' : [23,22,24,26]
}, index =[1, 2, 3,4])

# print(df4)

df5 = df4.pivot(index='date',columns='city',values='temp')
# print(df5)


df6 = df4.sort_values('temp') # ascending.
df7 = df4.sort_values('temp',ascending=False) # desending.

# print(df6)
# print(df7)

df8 = df4.drop(columns=['date','city']) # drop specific columns
# print(df8)


df9 = df4[df4.temp <= 23]
# print(df9)

df10 = df4.duplicated()
# print(df10)

df11 = df4.sample(n=2) #randomly select n rows
# print(df11)

df12 = df4.nlargest(2, 'temp')
# print(df12)

df13 = df4.head(3)
print(df13)
