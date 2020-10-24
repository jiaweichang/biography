
# coding: utf-8

# In[1]:


from sklearn import datasets
from sklearn.model_selection import train_test_split  # 切割資料為訓練與測試集
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

loaded_data = datasets.load_boston()


# In[2]:


data_X = loaded_data.data
data_y = loaded_data.target
X_train, X_test, Y_train, Y_test = train_test_split(data_X, data_y, test_size=0.2) 

model = LinearRegression()


# In[3]:


model.fit(X_train, Y_train)

print(model.predict(X_test[:4, :]))

y_pred = model.predict(X_test[:4])


# In[4]:


print(Y_test[:4])


print("MSE:", mean_squared_error(Y_test[:4], y_pred))
