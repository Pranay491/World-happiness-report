#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


sns.set_style('darkgrid')
plt.rcParams['font.size']=15
plt.rcParams['figure.figsize']=(10,7)
plt.rcParams['figure.facecolor']='#FFE584'


# In[26]:


data = pd.read_csv(r'C:\Users\OCT\Downloads\world-happiness-report-2021.csv')


# In[27]:


data.head()


# In[28]:


data.describe()


# In[29]:


data.info()


# In[30]:


data_columns = ['Country name','Regional indicator','Ladder score','Logged GDP per capita','Social support','Healthy life expectancy','Freedom to make life choices','Generosity','Perceptions of corruption']


# In[54]:


data = data[data_columns].copy()


# In[59]:


happy_df = data.rename({'Country name':'country_name', 'Regional indicator':'regional_indicator', 'Logged GDP per capita':'logged_gdp_per_capita', 'Social support':'social_support', 'Healthy life expectancy':'healthy_life_expectancy', 'Freedom to make life choices':'freedom_to_make_life_choices', 'Generosity':'generosity', 'Perceptions of corruption':'perceptions_of_corruption', 'Ladder score':'ladder_score'}, axis=1)


# In[60]:


happy_df.head()


# In[49]:


happy_df.isnull().sum()


# # Plot Between Happiness And GDP

# In[61]:


plt.rcParams['figure.figsize']=(15,7)
plt.title('Plot Between Ladder Score And GDP')
sns.scatterplot(x = happy_df.logged_gdp_per_capita, y=happy_df.ladder_score,hue=happy_df.regional_indicator,s=200);
plt.legend(loc='upper left',fontsize='10')
plt.xlabel('Ladder Score')
plt.ylabel('GDP Per Capita')


# In[62]:


gdp_region = happy_df.groupby('regional_indicator')['logged_gdp_per_capita'].sum()
gdp_region


# In[63]:


gdp_region.plot.pie(autopct = '%1.1f%%')
plt.title('GDP By Region')
plt.ylabel('')


# # Total Countries

# In[65]:


total_country = happy_df.groupby('regional_indicator')[['country_name']].count()
print(total_country)


# # Correlation Map

# In[69]:


cor = happy_df.corr(method= "pearson")
f,ax = plt.subplots(figsize = (10,5))
sns.heatmap(cor,mask=np.zeros_like(cor,dtype=np.bool),cmap = "Oranges",square = True ,ax=ax)


# # Corruption In Regions

# In[71]:


corruption = happy_df.groupby('regional_indicator')[['perceptions_of_corruption']].mean()
corruption


# In[74]:


plt.rcParams['figure.figsize']=(12,8)
plt.title('Perception Of corruption In Various Regions')
plt.xlabel('Regions',fontsize = 15)
plt.ylabel('Corruption Index',fontsize = 15)
plt.xticks(rotation = 30, ha = 'right')
plt.bar(corruption.index,corruption.perceptions_of_corruption)


# In[75]:


top_10 = happy_df.head(10)
bottom_10 = happy_df.tail(10)


# In[80]:


fig,axes = plt.subplots(1,2,figsize=(16,6))
plt.tight_layout(pad = 2)
xlabels = top_10.country_name
axes[0].set_title('Top 10 Happiest Countries Life Expectancy')
axes[0].set_xticklabels(xlabels,rotation=45,ha='right')
sns.barplot(x=top_10.country_name,y=top_10.healthy_life_expectancy,ax=axes[0])
axes[0].set_xlabel('Country Names')
axes[0].set_ylabel('Life Expectancy')

xlabels = bottom_10.country_name
axes[1].set_title('Bottom 10 Happiest Countries Life Expectancy')
axes[1].set_xticklabels(xlabels,rotation=45,ha='right')
sns.barplot(x=bottom_10.country_name,y=bottom_10.healthy_life_expectancy,ax=axes[1])
axes[1].set_xlabel('Country Names')
axes[1].set_ylabel('Life Expectancy')


# In[84]:


plt.rcParams['figure.figsize']=(15,7)
sns.scatterplot(x=happy_df.freedom_to_make_life_choices,y=happy_df.ladder_score,hue=happy_df.regional_indicator,s=300)
plt.legend(loc='upper left',fontsize='12')
plt.xlabel('Freedom To Make Life Choices')
plt.ylabel('Ladder Score')


# In[85]:


country = happy_df.sort_values(by = 'perceptions_of_corruption').head(10)
plt.rcParams['figure.figsize']=(12,6)
plt.title('Countries With Most Perception Of Corruption')
plt.xlabel('Country',fontsize=13)
plt.ylabel('Corruption Index',fontsize=13)
plt.xticks(rotation=30,ha='right')
plt.bar(country.country_name,country.perceptions_of_corruption)


# In[86]:


country = happy_df.sort_values(by = 'perceptions_of_corruption').tail(10)
plt.rcParams['figure.figsize']=(12,6)
plt.title('Countries With Most Perception Of Corruption')
plt.xlabel('Country',fontsize=13)
plt.ylabel('Corruption Index',fontsize=13)
plt.xticks(rotation=30,ha='right')
plt.bar(country.country_name,country.perceptions_of_corruption)


# # Corruption Vs Happiness

# In[91]:


plt.rcParams['figure.figsize']=(15,7)
sns.scatterplot(x=happy_df.ladder_score,y=happy_df.perceptions_of_corruption,hue=happy_df.regional_indicator,s=300)
plt.legend(loc='lower left',fontsize='14')
plt.xlabel('Ladder/Happiness Score')
plt.ylabel('Corruption')


# In[ ]:




