import seaborn as sns
import matplotlib.pyplot as plt


df = sns.load_dataset('titanic')
print(df.groupby("sex")["survived"].mean())

plt.figure(figsize=(8, 4))
sns.countplot(data=df, x="sex", hue="survived")
plt.legend(loc='upper right', title="Survived",labels=["no","yes"])
plt.title("Survival status by Gender", fontsize=14)
plt.xlabel('sex')
plt.ylabel('Count')
plt.show()
