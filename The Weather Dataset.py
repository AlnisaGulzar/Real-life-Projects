#!/usr/bin/env python
# coding: utf-8

# #  Working on Real Project with python

# # (A part of Big Data Analysis)

# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# ## The Weather Dataset

# Here, The Weather Dataset is a time-series dataset with per-hour information about the weather conditions at a perticular location. It records Temperature, Der Point Temperature, Relative Humidity, wind speed, Pressure, and Conditions.
# 
# 
# This dataset is availaible as csv file, we are going to analyze this dataset using pandas DataFrame.

# In[11]:


import pandas as pd 


# In[12]:


data = pd.read_csv(r"C:\Users\alnis\Downloads\file.csv")


# In[13]:


data


# # How to Analyze DataFrames ?

# # .head()

# It shows the first N rows in the data (by default, N=5)

# In[14]:


data.head()


# # .shape

# It shows the total no. of rows and no. of columns of the dataframe

# In[15]:


data.shape


# # .index

# The attributes provides the index of the dataframe

# In[16]:


data.index


# # .columns

# it shows the name of each column

# In[17]:


data.columns


# # .dtypes

# it shows the data-types of each column

# In[18]:


data.dtypes


# # .unique()

# In a column, it shows all the unique values. it can be applied on a single colimn only, not on the whole dataframe

# In[21]:


data['Weather'].unique()


# # .nunique()

# It shows the total no. of unique values in each column. It can be applied on single column as well as the whole dataframe.

# In[22]:


data.nunique()


# # .count

# It shows the total no. of non-null values in each column. It can be applied on single column as well as the whole dataframe.

# In[24]:


data.count()


# # .value_counts

# In a column, it shows all the unique values with their count. It can be applied on single column only

# In[29]:


data['Weather'].value_counts()


# # .info()

# Provides basic information about the dataframe.

# In[30]:


data.info()


# # Q) 1. Find all the unique 'Wind Speed' values in the data.

# In[37]:


data.head(2)


# In[38]:


data.nunique()


# In[40]:


data['Wind Speed_km/h'].nunique()


# In[41]:


data['Wind Speed_km/h'].unique()  #Answere


# # Q) 2. Find the number of times when the 'Weather is exactly clear'

# In[42]:


data.head(2)


# In[43]:


# value_counts()
data.Weather.value_counts()


# In[47]:


# Filtering
data.head(2)
data[data.Weather == 'Clear']


# In[49]:


#groupby()
data.head(2)
data.groupby('Weather').get_group('Clear')


# # Q) 3. Find the number of times when the 'Wind Speed was exactly 4 km/h'.

# In[51]:


data.head(2)


# In[53]:


data[data['Wind Speed_km/h'] == 4]


# # Q) 4. Find out all the Null Values in the data.

# In[59]:


data.isnull().sum()


# In[62]:


data.notnull().sum()


# # Q. 5) Rename the column name 'Weather' of the dataframe to 'Weather Condition'.

# In[65]:


data.head(2)


# In[68]:


data.rename(columns={'Weather': 'Weather Condition'}, inplace= True)


# In[69]:


data.head()


# # Q.6) What is the mean 'Visibility' ?

# In[71]:


data.head(2)


# In[72]:


data.Visibility_km.mean()


# # Q.7) What is the Standard Deviation of 'Pressure' in this data?

# In[74]:


data.head(2)


# In[75]:


data.Press_kPa.std()


# # Q.8) What is the Variance of 'Relative Humidity 'in thia data

# In[76]:


data['Rel Hum_%'].var()


# # Q.9) Find all instances when 'Snow' was recorded

# In[80]:


#value_counts()
data['Weather Condition'].value_counts()


# In[82]:


#Filtering
data[data['Weather Condition'] == 'Snow']


# In[86]:


#str.contains
data[data['Weather Condition'].str.contains('Snow')].tail(50)


# # Q.10) Find all the instances when 'When Speed is above 24'and 'Visibility'is 25'.

# In[89]:


data[(data['Wind Speed_km/h'] > 24) &  (data['Visibility_km'] == 25)]


# # Q.11) What is the Mean value of each column against each 'Weather Condition'?

# In[90]:


data.head(2)


# In[96]:


data.groupby('Weather Condition').mean(numeric_only=True)


# # Q. 12 What is the Minimum and Maximum value of each column against each 'Weather Condition'?

# In[97]:


data.groupby('Weather Condition').min()


# In[98]:


data.groupby('Weather Condition').max()


# # Q.13) show all the records where Weather Condition is Fog.

# In[103]:


data[data['Weather Condition'] == 'Fog']


# # Q.14) Find all the instances when 'Weather is Clear' or 'Visibility is above 40'.

# In[105]:


data[(data['Weather Condition']=='Clear') | (data['Visibility_km'] > 40)]


# # Q 15) Find all the instances when:
#     
#     A. 'Weather is Clear' and 'Relative Humidity is greater than 50'
#     
#     or
#     
#     B. 'Visibility is above 40'

# In[107]:


data.head(2)


# In[114]:


data[(data['Weather Condition']== 'Clear')&(data['Rel Hum_%']>50)|(data['Visibility_km']>40)]


# In[ ]:




