import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor

# Download and prepare the data
df = pd.read_csv("lifesatisfaction.csv")
# print(len(df))
# print(df.head(7))
# print(df.info())
# print(df.describe())

X = df[["GDP per capita (USD)"]].values
y = df[["Life satisfaction"]].values
# print(X)
# print(y)

# Visualize the data
# df.plot(kind='scatter', grid=True,x="GDP per capita (USD)", y="Life satisfaction")
# plt.axis([23_500, 62_500, 4, 9])
# plt.show()

# Select a linear model
model1 = LinearRegression()
model2 = KNeighborsRegressor(3)
# Train the model
model1.fit(X, y)
model2.fit(X, y)
# Make a prediction for Cyprus
new_instance = [[31_721.30]] # South Korea GDP per capita in 2020
print(f"Life satisfaction(LinearRegression) : {model1.score(X, y)}")
print(f"Life satisfaction(KNeighborsRegressor) : {model2.score(X, y)}")
print(f"예측된 값: {model1.predict(new_instance)[0][0]:.2f}") # output: [[6.30165767]]
print(f"예측된 값: {model2.predict(new_instance)[0][0]:.2f}") # output: [[5.89940454]]