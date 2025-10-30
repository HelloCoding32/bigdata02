import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

s1 = pd.Series([0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1])
print(s1)
sc1 = s1.cumsum() # Cumulative sum
# print(sc1)
# print(s1.mul(sc1)) # multiply
# print(s1.mul(sc1).diff()) # difference (빼기)
# print(s1.mul(sc1).diff().where(lambda n: n>0)) # where
# print(s1.mul(sc1).diff().where(lambda n: n>0).ffill()) # front fill 앞 값을 Nan값에 채우다.
print(s1.mul(sc1).diff().where(lambda n: n>0).ffill().add(sc1, fill_value=0)) # add 0
