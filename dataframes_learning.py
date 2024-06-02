#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install pip-autoremove')


# In[ ]:





# In[4]:


import pandas


# In[5]:


get_ipython().system('pip-autoremove pandas -y')


# In[9]:


get_ipython().system('pip install pandas')


# In[11]:


import pandas as pd
df = pd.read_csv("C:\\Users\\new\\Downloads\\world_population.csv",)


# In[12]:


df


# In[13]:


df.info()


# In[14]:


df.shape


# In[15]:


df.head(10)


# In[21]:


df[df['Rank']>=200]


# In[22]:


df[df['Country'].str.contains('City')]


# In[24]:


spec_countries=['Andorra','Tuvalu']
df[df['Country'].isin(spec_countries)]


# In[30]:


df.filter(items = ['Continent','CCA3']).sort_values(by=['Continent'])


# In[29]:


df[df['Rank']<10].sort_values(by=['Continent','Country'])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




