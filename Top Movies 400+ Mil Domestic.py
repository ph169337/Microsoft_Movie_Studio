#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


df = pd.read_csv('bom.movie_gross.csv')


# In[4]:


df.head()


# In[5]:


df.domestic_gross > 4000000


# In[6]:


money_bank = []
for money in df.domestic_gross:
    if money > 400000000: # 400 mil and above
        money_bank.append(money)
        
money_bank


# In[7]:


top_dom_gross = {'Toy story' : 415000000.0,
                "Marvel's The Avengers": 623400000.0,
                 'The Dark Knight Rises' : 448100000.0,
                 'The Hunger Games' : 408000000.0,
                 'Frozen' : 400700000.0,
                 'Iron Man 3' : 409000000.0,
                 'The Hunger Games: Catching Fire' : 424700000.0,
                 'Star Wars: The Force Awakens' : 936700000.0,
                 'Jurassic World' : 652300000.0,
                 'Avengers: Age of Ultron' : 459000000.0,
                 'Captain America: Civil War' : 408100000.0,
                 'Rogue One: A Star Wars Story' : 532200000.0,
                 'Finding Dory' : 486300000.0,
                 'Star Wars: The Last Jedi' : 620200000.0,
                 'Beauty and the BeastJumanji: Welcome to the Jungle' : 504000000.0,
                 'Jumanji: Welcome to the Jungle' : 404500000.0,
                 'Wonder Woman' : 412600000.0,
                 'Avengers: Infinity War' : 678800000.0,
                 'Black Panther' : 700100000.0,
                 'Jurassic World: Fallen Kingdom' :  417700000.0,
                 'Incredibles 2' : 608600000.0}
              


# In[8]:


top_dom_gross


# In[9]:


movies_name = []


# In[10]:


for movie in top_dom_gross:
    movies_name.append(movie)


# In[11]:


movies_name


# In[12]:


money_bank


# In[13]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
plt.title('Movies over 400mil + Domestic')
plt.ylabel('Millions')
plt.xticks(rotation=90)
ax.bar(movies_name, money_bank)
plt.show()


# In[ ]:





# In[ ]:




