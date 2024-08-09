import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values


# dealing with missing data
# way 1 ---> remove those record if you have large data set
# print(dataset.Salary.fillna(dataset.Salary.mean()))

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')  #for strategy we can pass mean , median, most Frequent, constant 
# imputer.fit(X[:, 1:3])
X[: , 1:3] = imputer.fit_transform(X[:, 1:3])  #imputer.transfrom will return the transformed columns and we have to set it back to our original matrix
# can use fit_transform() method to do both tast at once

# encoding categorical data --> turing strings into numerical(binary)
# for X
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
# for transformers we have to pass 3 things what we want to do, what type of encoder, columns on which we want to apply onehotencoding
# remainder means what to do with rest of the columns, "passthrough" means do nothing let them go
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
X = np.array(ct.fit_transform(X))    #ct.fit_transform doesnt return a numpy array , so we have to convert it in 

# for y
# note : whenever there are only 2 categories you can use label encoder
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

# splitting up data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train,  y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

#feature scaling  -->it will put all the feature on the same scale (standardization-> -3 to +3) and (normalization-> 0 to 1)
# we ara gonna use standardization that is using mean and standard deviation 
# formula for standardization x_stand = x-mean(x)/standard deviation(x)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
# note: do not use feature scaling on encoded categorical data
# mention the columns you want to apply feature scaling
X_train[:, 3:] = sc.fit_transform(X_train[:, 3:])
# so what is happening here --> mentioned column ka mean and sd calculate hoga then transfrom method se standardization wale formula se puri column ko standardize kia jaega then scaled data ko waps se main table me dal dia jaega
# feature scaling is only applied to columns 
# note: we need to use the same scaler that we have used in X_train that is why we are not going to call fit method we are just going to call transfrom method, else fit method will create a new scaler according to new test dat
X_test[:, 3:] = sc.transform(X_test[:, 3:])
print(X_test)

 
