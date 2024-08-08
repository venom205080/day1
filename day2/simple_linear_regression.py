import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# importing data
# Salary_dataset.csv
# Mobile-Price-Prediction-cleaned_data.csv
dataset = pd.read_csv('advertising.csv')
x = dataset["TV"].values
y = dataset["Sales"].values

# splitting data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 1/5, random_state = 0)

# train model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# predict data
y_pred = regressor.predict(X_test)
print(y_pred)

# plotting graph
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# print(x)
# print(y)

