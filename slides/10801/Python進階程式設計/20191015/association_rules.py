
# coding: utf-8

# In[1]:


import pandas as pd 
from mlxtend.frequent_patterns import apriori 
from mlxtend.frequent_patterns import association_rules 


# In[2]:


df=pd.read_excel('Online Retail.xlsx') 
df.head()


# In[3]:


df['Description'] = df['Description'].str.strip()


# In[4]:


df.dropna(axis=0, subset=['InvoiceNo'], inplace=True) 


# In[5]:


df['InvoiceNo'] = df['InvoiceNo'].astype('str')


# In[6]:


df = df[~df['InvoiceNo'].str.contains('C')] 


# In[41]:


basket = (df[df['Country'] =="France"].groupby(['InvoiceNo', 'Description'])
	['Quantity'].sum().unstack().reset_index().fillna(0).set_index('InvoiceNo'))


# In[42]:


basket.head(10)


# In[27]:


def encode_units(x): 
	if x <= 0: 
		return 0 
	if x >= 1: 
		return 1 


# In[31]:


basket_sets = basket.applymap(encode_units)
basket_sets.drop('POSTAGE', inplace=True, axis=1)


# In[32]:


basket_sets.head(10)


# In[49]:


frequent_itemsets = apriori(basket_sets, min_support=0.08, use_colnames=True)


# In[50]:


frequent_itemsets.head(100)


# In[51]:


rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
rules.head() 


# In[74]:


rules[ (rules['lift'] >= 6) & (rules['confidence'] >= 0.6) & (rules['antecedents'] == frozenset({'SET/20 RED RETROSPOT PAPER NAPKINS'})) ].head()


# In[76]:


rules["antecedent_len"] = rules["antecedents"].apply(lambda x: len(x))
rules


# In[77]:


rules[ (rules['lift'] >= 6) & (rules['confidence'] >= 0.6) & (rules['antecedent_len'] >= 2) ].head()


# In[59]:


basket2 = (df[df['Country'] =="Germany"] 
	.groupby(['InvoiceNo', 'Description'])['Quantity'] 
	.sum().unstack().reset_index().fillna(0) 
	.set_index('InvoiceNo'))


# In[60]:


basket_sets2 = basket2.applymap(encode_units) 
basket_sets2.drop('POSTAGE', inplace=True, axis=1)


# In[61]:


frequent_itemsets2=apriori(basket_sets2,min_support=0.05, use_colnames=True)
rules2= association_rules(frequent_itemsets2, metric="lift", min_threshold=1)


# In[63]:


rules2[ (rules2['lift'] >= 4) & (rules2['confidence'] >= 0.5)].head(10)

