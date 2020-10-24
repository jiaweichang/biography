
# coding: utf-8

# In[1]:


#  ---導入模塊---
from sklearn import datasets 
from sklearn.model_selection import train_test_split
import pandas as pd


# In[2]:


# ---資料處理---
wine = datasets.load_wine() # 載入SKlearn內建資料集
print(wine) 


# In[3]:


wine_data = wine.data # 定義資料特徵
wine_target = wine.target # 定義資料標籤
# print(pd.DataFrame(wine.data))
# 印出資料特徵查看
# print(pd.DataFrame(wine.target))
# 印出資料標籤查看
x_train, x_test, y_train, y_test = train_test_split(wine_data, wine_target, test_size = 0.2)
# 使用"train_test_spit"將數據分成訓練和測試兩類,test_size = 0.2,代表測試數據佔20%


# In[4]:


from sklearn.neighbors import KNeighborsClassifier


# In[5]:


kNN = KNeighborsClassifier()


# In[6]:


kNN.fit(x_train, y_train)


# In[7]:


print(kNN.predict(x_test))


# In[8]:


print(y_test)

