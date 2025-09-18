import pandas as pd
import seaborn as sns


print(len(sns.get_dataset_names()))

titanic = sns.load_dataset('titanic')
# print(titanic.head())

# print(titanic.describe())

# print(titanic[titanic['age'] <= 15])

print(titanic.nlargest(5, 'age'))