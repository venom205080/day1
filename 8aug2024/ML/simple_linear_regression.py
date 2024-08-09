import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# importing data
# Salary_dataset.csv
# Mobile-Price-Prediction-cleaned_data.csv
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, 0].values
y = dataset.iloc[:, -1].values

# splitting data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/5, random_state = 0)
X_train = X_train.reshape(-1,1)
X_test = X_test.reshape(-1,1)
# # train model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
# note: this fitting model required 2d array we need to reshape X to 2d array
regressor.fit(X_train, y_train)

# # predict data
y_pred = regressor.predict(X_test)
# # print(y_pred)

# plotting graph
plt.scatter(X_train, y_train, color = 'red', marker="+")
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# print(X_train.shape)
# print(y.shape)

