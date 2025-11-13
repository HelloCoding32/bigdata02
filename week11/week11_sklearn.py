import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from joblib.parallel import default_parallel_config
from sklearn.datasets import load_diabetes, load_breast_cancer

cancer = load_breast_cancer()
# print(cancer)
# print(cancer.target)  # 0 : 악성, 1 : 양성
df_cancer = pd.DataFrame(cancer.data, columns=cancer.feature_names)
df_cancer['target'] = cancer.target
# print(df_cancer.tail(3))
# print(df_cancer.info())

plt.figure(figsize = (10,6))
sns.boxplot(x='target', y='mean radius', data=df_cancer)
plt.title('Mean radius of diabetes (0: Malignant, 1: Benign)')
plt.xlabel('Target')
plt.ylabel('Mean radius')
plt.show()