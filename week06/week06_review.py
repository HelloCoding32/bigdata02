import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('titanic')
# plt.figure(figsize=(8, 4))
# sns.histplot(data=df, x="age", bins=16, kde=True)
# plt.title("Age Distrubution of Passengers")
# plt.ylabel('Frequency')
# plt.xlabel('Age')
# plt.tight_layout()
# plt.show()

# plt.figure(figsize=(8, 4))
# sns.histplot(data=df, x="survived")
# plt.title("suvivors VS Non-survivors", fontsize=14)
# plt.xlabel('Survive(0:No, 1:Yes)')
# plt.ylabel('Count')
# plt.tight_layout()
# plt.show()

plt.figure(figsize=(8, 4))
sns.countplot(data=df, x="sex", hue="survived")
plt.title("Passenger Count by Class", fontsize=14)
plt.xlabel('class ')
plt.ylabel('Count')
plt.show()