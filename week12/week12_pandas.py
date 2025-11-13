import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats


s = pd.Series([1,np.nan,3, np.nan,5,6,np.nan,np.nan,9])
print(s)
# 내삽(보관) interpolate
print(s.interpolate(method='spline', order=1,limit=2 ,limit_direction='both'))