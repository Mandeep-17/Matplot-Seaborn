#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# # Load the Dataset

# In[2]:


netflix_data = pd.read_csv('netflix1.csv')


# In[3]:


netflix_data


# In[4]:


netflix_data.isnull().sum()


# In[5]:


netflix_data.info()


# In[6]:


netflix_data.describe()


# # Distribution of Show Types (Movies vs. TV Shows)

# In[7]:


netflix_data['type'].value_counts()


# In[8]:


plt.figure(figsize=(8, 8))
netflix_data['type'].value_counts().plot.pie(autopct='%1.1f%%', colors=['#FFC436', '#2E97A7'],shadow=1)
plt.title('Distribution of Show Types',size=17)
plt.show()


# #  Distribution of Release Years

# In[9]:


plt.figure(figsize=(12, 6))
sns.histplot(netflix_data['release_year'], bins=30, kde=True, color='purple')
plt.title('Distribution of Release Years',size=17)
plt.xlabel('Release Year')
plt.ylabel('Count')
plt.show()


# # Top 10 Countries with the Most Shows

# In[10]:


top_countries = netflix_data['country'].value_counts().head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x=top_countries.values, y=top_countries.index, palette='viridis')
plt.title('Top 10 Countries with the Most Shows',size=17)
plt.xlabel('Number of Shows')
plt.ylabel('Country')
plt.show()


# #  Distribution of Ratings

# In[11]:


plt.figure(figsize=(10, 6))
sns.countplot(x='rating', data=netflix_data, palette='Set1')
plt.title('Distribution of Ratings',size=17)
plt.xlabel('Rating')
plt.ylabel('Count')
plt.show()


# #  Duration Distribution

# In[12]:


plt.figure(figsize=(12, 6))
sns.histplot(netflix_data['duration'].str.extract('(\d+)').astype(float), bins=30, kde=True, color='orange')
plt.title('Distribution of Durations',size=17)
plt.xlabel('Duration (minutes)')
plt.ylabel('Count')
plt.show()


# # Top Genres

# In[13]:


genres = netflix_data['listed_in'].str.split(', ', expand=True).stack()

genre_counts = genres.value_counts()

top_genres = genre_counts.head(10)


# In[14]:


plt.figure(figsize=(10, 6))
top_genres.plot(kind='bar', color='green')
plt.title('Top Genres',size=17)
plt.xlabel('Genre')
plt.ylabel('Number of Productions')
plt.xticks(rotation=45, ha='right')
plt.show()


# # Number of Shows Added Each Month

# In[15]:


from datetime import datetime
import calendar


# In[16]:


netflix_data['date_added'] = pd.to_datetime(netflix_data['date_added'])


# In[17]:


netflix_data['added_month'] = netflix_data['date_added'].dt.month


# In[18]:


monthly_counts = netflix_data['added_month'].value_counts().sort_index()


# In[19]:


plt.figure(figsize=(10, 6))
monthly_counts.plot(kind='line', marker='o',color='skyblue', markersize= 8,markerfacecolor='red')
plt.title('Number of Shows Added Each Month')
plt.xlabel('Month')
plt.ylabel('Number of Shows Added')
plt.xticks(range(1, 13), calendar.month_name[1:], rotation=45, ha='right')
plt.tight_layout()
plt.legend()
plt.show()


# In[ ]:





# In[ ]:




