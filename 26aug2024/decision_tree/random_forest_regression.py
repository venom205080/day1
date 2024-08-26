import pandas as pd
import numpy as np
import matplotlib as plt

dataset = pd.read_csv("diabetes_dataset.csv")
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:, -1].values

#split data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# make model
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=100, random_state=0)
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)
# res = pd.concat(y_test, y_pred, axis=1)

#predicted result
a = pd.Series(y_test)
b = pd.Series(y_pred)
res = pd.concat([a,b], axis=1).values
# print(res)

fail_count = 0
for i, j in res:
    if(i!=round(j)):
        fail_count += 1

print(f"pass count is {len(res)-fail_count}")
print(f"fail count is {fail_count}")
# res = regressor.predict(X_test.head(1))
# print(res)

# for i, j in res:
#     if(i!=j):
#         print(i, j)