import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('data.csv')

print(data.head())

X = data[['AT', 'V', 'AP', 'RH']]
print(X.head())

y = data[['PE']]
print(y.head())

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

from sklearn.linear_model import LinearRegression
linreg = LinearRegression()
linreg.fit(X_train, y_train)
y_pred = linreg.predict(X_test)

from sklearn import metrics
print("MSE:",metrics.mean_squared_error(y_test, y_pred))
