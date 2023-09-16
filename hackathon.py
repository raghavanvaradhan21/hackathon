#!/usr/bin/env python
# coding: utf-8

# # Happiness EDA

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# # df storers the data of world happiness report from 1960-2018

# In[2]:


df = pd.read_csv(r"C:\Users\ragha\Downloads\world-happiness-report.csv")


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.shape


# In[6]:


df.columns


# In[7]:


df.info()


# # df2021 storers the data of world happiness report for the year 2021

# In[8]:


df2021=pd.read_csv(r"C:\Users\ragha\Downloads\world-happiness-report-2021.csv")


# In[10]:


df2021.head()


# In[11]:


df2021.tail()


# In[12]:


df2021.shape


# In[13]:


df2021.columns


# In[14]:


df2021.info()


# #                                      Visualization & Analysis

# # Number of Countries in a region

# In[93]:


sns.countplot(x="Regional indicator",data=df2021)
plt.xticks(rotation = 75,fontweight="bold")
plt.show()


# # Healthy life expectancy at birth of countries from 2005 to 2020

# In[101]:


fig = px.choropleth(df.sort_values("year"),
                   locations = "Country name",
                   color = "Healthy life expectancy at birth",
                   locationmode = "country names",
                   animation_frame = "year")
fig.show()


# # Insights 1 : Countries in western europe have higher life expectancy and countries in sub-saharan africa have lower life expectancy.

# # Correlation of Happiness

# In[99]:


plt.figure(figsize=(16,9))
sns.heatmap(df2021.corr(), annot=True, linewidth=.5, cmap='YlGnBu', fmt='.2f')
plt.show()


# # The correlation map above visualizes the correlation values between happiness scores and the factors that contribute to happiness score. It shows that there is a direct positive correlation between the Happiness Score of a country and economy and healthy life expectancy.

# # Scatter Plots Showing direct positive correlation between happiness & economy & life expectancy

# In[104]:


fig= px.scatter(df2021, x="Ladder score", y="Logged GDP per capita", color="Ladder score",
               title= "happiness correlation with economy")
fig2 = px.scatter(df2021, x="Ladder score", y="Healthy life expectancy", color="Ladder score",
                 title="happiness correlation with life expectancy")
fig.show()
fig2.show()


# # Top Ten Countries on basis of Happiness score

# In[77]:


df_sorted = df2021.sort_values(by='Ladder score', ascending=False)


# In[78]:


top_10 = df_sorted.head(10)


# In[82]:


plt.figure(figsize=(10, 6))
plt.bar(top_10['Country name'], top_10['Ladder score'])
plt.xlabel('Country name')
plt.ylabel('Ladder score')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()


# # Bottom Ten Countries on basis of Happiness score

# In[80]:


bot_10 = df_sorted.tail(10)


# In[83]:


plt.figure(figsize=(10, 6))
plt.bar(bot_10['Country name'], bot_10['Ladder score'])
plt.xlabel('Country name')
plt.ylabel('Ladder score')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()


# # Happiest and Unhappiest countries in 2021

# In[16]:


df2021_happiest_unhappiest = df2021[(df2021.loc[:, "Ladder score"] > 7.4) | (df2021.loc[:, "Ladder score"] < 3.5)]
sns.barplot(x = "Ladder score", y = "Country name", data=df2021_happiest_unhappiest, palette = "Paired")
plt.title("Happiest and Unhappiest Countries in 2021")
plt.show()


# In[58]:


#FINLAND IS THE HAPPIEST COUNTRY IN 2021
#AFGHANISTAN IS THE UNHAPPIEST COUNTRY IN 2021


# # Relationship between happiness and Income

# In[119]:


fig = px.bar(df, 
                 x = "Log GDP per capita",
                 y = "Life Ladder",
                 animation_frame = "year",
                 animation_group = "Country name",
                 color = "Country name", 
                 hover_name = "Country name")
fig.update_layout(title = "Life Ladder and GDP per capita by Countries for each Year")
fig.show()


# # insights : can be observed that all countries in 2005 are having low income and low happiness compared to 2020 

# # Relationship between happiness and Freedom

# In[114]:


fig = px.bar(df, 
                 x = "Freedom to make life choices",
                 y = "Life Ladder",
                 animation_frame = "year",
                 animation_group = "Country name",
                 color = "Country name", 
                 hover_name = "Country name")
fig.update_layout(title = "Life Ladder and Freedom Comparison by Countries  for each Year")
fig.show()


# # insights : can be observed that all countries are having higher levels of freedom for the year  2020 compared to 2005

# # Relationship between happiness and Corruption

# In[118]:


fig = px.bar(df, 
                 x = "Perceptions of corruption",
                 y = "Life Ladder",
                 animation_frame = "year",
                 animation_group = "Country name",
                 color = "Country name", 
                 hover_name = "Country name")
fig.update_layout(title = "Life Ladder and Corruption by Countries for each Year")
fig.show()


# # insights : the countries having perceptions of corruption of more than 0.6 are more happier

# # Ladder Score Distribution by Regional Indicator

# In[27]:


df2=df2021["Ladder score"]
df2


# In[37]:


plt.figure(figsize = (15,8))
sns.kdeplot(x=df2,hue = df2021["Regional indicator"],fill=True)
plt.show()


# # Ladder score distribution by countries in Map Views

# In[35]:


import plotly.express as px


# In[55]:


fig = px.choropleth(df.sort_values("year"),
                   locations = "Country name",
                   color = "Life Ladder",
                   locationmode = "country names",
                   animation_frame = "year")
fig.show()


# # Most generous and most ungenerous countries in 2021

# In[50]:


df2021_g =df2021[(df2021.loc[:,"Generosity"] > 0.4) | (df2021.loc[:,"Generosity"] < -0.2)]
sns.barplot(x = "Generosity", y = "Country name", data= df2021_g, palette="Paired")
plt.title("Most generous and most generois countries in 2021")
plt.show()


# In[51]:


#INDONESIA IS THE MOST GENEROUS COUNTRY IN 2021
df2021.query("Generosity==0.542")


# In[52]:


#INDONESIA IS THE MOST GENEROUS COUNTRY IN 2021
df2021.query("Generosity==0.542")


# # Relationship Between  Features

# In[57]:


sns.heatmap(df.corr(), annot = True, fmt = ".2f", linewidth = .7)
plt.show()


# # Conclusion

# #  With the exploratory data analysis in this notebook, we can understand that the life ladder has a positive correlation with the variables log gdp per capita, social support, healthy life expectancy at birth, and freedom to make life choices. 
# 
