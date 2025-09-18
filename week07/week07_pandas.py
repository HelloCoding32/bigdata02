import pandas as pd

df = pd.read_csv('savant_data.csv')
# print(df['player_name'])
df_new = df[['player_id','player_name','total_pitches','velocity','hrs','so','bb']]
print(df_new.query('player_name == "Ohtani, Shohei"'))
print(df_new[df_new['player_name'] == 'Ohtani, Shohei'])