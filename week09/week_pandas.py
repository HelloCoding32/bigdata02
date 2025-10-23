import pandas as pd

uber = pd.read_csv("Uber.csv")
# uber['START_DATE*'] = pd.to_datetime(uber['START_DATE*'])
# print(uber)

uber['START_DATE*'] = pd.to_datetime(uber['START_DATE*'], errors='coerce')
uber['END_DATE*'] = pd.to_datetime(uber['END_DATE*'])

uber.drop(1155, inplace=True)
# print(uber['END_DATE*'].unique())
# print(uber[uber['MILES*'] == uber['MILES*'].max()])

# print(uber['PURPOSE*'].value_counts())
# print(uber['PURPOSE*'].isna().sum())


# uber['DURATION*'] = (uber['END_DATE*'] - uber['START_DATE*'])
uber['DURATION*'] = (uber['END_DATE*'] - uber['START_DATE*']).dt.total_seconds() / 60
# print(uber['DURATION*'])
print(uber.info())