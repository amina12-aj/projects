#!/usr/bin/env python
# coding: utf-8

# In[118]:



import numpy as np
import pandas as pd


url = pd.read_csv(r"C:\Users\TENECE\Downloads\food.csv", encoding='Latin')
print(url.head(20))


# In[ ]:





# In[78]:


url.describe(include = 'all')


# In[61]:


#total null values
url.isnull().sum()


# In[7]:


#checking duplicate values
url.duplicated().any()


# In[67]:


#total null values of 2016
sum_null = url["Y2016"].isnull().sum()
print(sum_null)
#count_null = url["Y2016"].isnull()
count_null = url["Y2016"].isnull().count()
print(count_null)


# In[70]:


#calculating percentage
percent_missing = url["Y2016"].isnull().sum() * 100 / len(url)
print(percent_missing)


# In[47]:


#replacing null value with most occuring value
#for i in url.columns:
 #url[i].fillna(url[i].mode()[0], inplace=False)
#print(url)


# In[21]:


#aggregate sum of items in 2014 and 2017
url.groupby(['Item']).agg(
     sum_2014 = ('Y2014','sum'),
     sum_2017 = ('Y2017','sum'),
     ).reset_index()


# In[22]:



#mean of year 2015
df_mean = url["Y2015"].mean()
print(df_mean )
#standard deviation of 2015
df_std= url["Y2015"].std()
print(df_std)


# In[ ]:





# In[94]:


#third lowest sum in 2018
lowest_sum = url.groupby('Element')['Y2018'].sum()
sum_low = lowest_sum.sort_values()
print(sum_low[2])
                                    





# In[74]:


#unique countries
unique_countries = url.Area.nunique(dropna = True)
print(unique_countries)


# In[ ]:





# In[18]:


#total sum of production in 2014
sum_prod = url.groupby('Element')['Y2014'].sum()
print(sum_prod[11])


# In[19]:


#highest element in 2018
highest_element= url.groupby('Element')['Y2018'].max()
print(highest_element[-2])


# In[108]:


#calculate highest sum of import
highest_import= url.groupby(['Element'])['Y2014','Y2015'].sum().iloc[7]
print(highest_import)
highest_sum = url.groupby(['Element'])['Y2016','Y2017','Y2018'].sum().iloc[7]
print(highest_sum)
print(highest_sum[1])


# In[115]:


#calculating highest correlation
correlation = url.groupby('Element Code')[['Y2014','Y2015', 'Y2016', 'Y2017', "Y2018"]].corr().unstack().iloc[:,1]
print(correlation)


# In[114]:


#total import quantity in 2018
import_quantity = url.groupby('Area')[['Y2018']].sum().iloc
print(import_quantity)


# In[ ]:





# In[ ]:





# In[ ]:




