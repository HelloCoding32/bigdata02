import numpy as np
import pandas as pd
import seaborn as sns

def square(x):
    return x*x
def cube(x):
    return x*x*x

mpg = sns.load_dataset("mpg")
df = pd.DataFrame([
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
], index =[1, 2, 3], columns=['A', 'B', 'C'])
print(df)
print(df.apply(square))
print(df.apply(cube))