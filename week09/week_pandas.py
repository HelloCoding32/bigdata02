import pandas as pd

uber = pd.read_csv("Uber.csv")

# print(uber.head(5))
# print(uber.info())
# print(uber.describe())
# print(uber[uber["MILES*"] == 12204.7])
# print(uber[uber["MILES*"] == uber["MILES*"].max()])
# print(uber.tail(5))
uber.drop(1155, inplace=True)
# print(uber.tail(5))
print(uber.describe())