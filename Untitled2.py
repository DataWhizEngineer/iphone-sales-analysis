#!/usr/bin/env python
# coding: utf-8

# I phone sales analysis

# In[1]:


import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


# In[2]:


data = pd.read_csv('apple_products.csv')


# In[3]:


data


# In[4]:


data.isnull().sum()


# In[5]:


data.describe()


# Top 10 iphone sales analysis in india

# In[18]:


Highest_ratings = data.sort_values(by=['Star Rating'],ascending= False)
Highest_ratings = Highest_ratings.head(10)
Highest_ratings['Product Name']


# In[22]:


xaxis=Highest_ratings['Product Name'].value_counts()
labels=xaxis.index


# In[24]:


yaxis=Highest_ratings['Number Of Ratings']

fig = px.bar(Highest_ratings,x=labels,y=yaxis,title='Number of ratings per highest rated iphones')
fig.show()


# In[25]:


yaxis=Highest_ratings['Number Of Reviews']

fig = px.bar(Highest_ratings,x=labels,y=yaxis,title='Number of review per highest rated iphones')
fig.show()


# In[47]:


r_fig = px.scatter(data_frame=data ,x='Number Of Ratings',y='Sale Price',size='Discount Percentage'
                  ,trendline='ols',title='Relationship between sale price and number of ratings'
                  )
r_fig.show()


# In[42]:


r_fig = px.scatter(data_frame=data ,x='Number Of Ratings',y='Discount Percentage',size='Sale Price'
                  ,trendline='ols',title='Relationship between Discount Percentage and number of ratings')
r_fig.show()  


# Some of the takeaways from this analysis about the sales of iPhone in India are:
APPLE iPhone 8 Plus (Gold, 64 GB) was the most appreciated iPhone in India
iPhones with lower sale prices are sold more in India
iPhones with high discounts are sold more in India
# In[ ]:




