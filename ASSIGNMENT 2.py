#!/usr/bin/env python
# coding: utf-8

# # Extracting the Latitude and Longitude of Canada Ontario
# 

# In[1]:


"""import requests # library to handle requests
import pandas as pd # library for data analsysis
import numpy as np # library to handle data in a vectorized manner
import random # library for random number generation

!conda install -c conda-forge geopy --yes 
from geopy.geocoders import Nominatim # module to convert an address into latitude and longitude values

# libraries for displaying images
from IPython.display import Image 
from IPython.core.display import HTML 
    
# tranforming json file into a pandas dataframe library
from pandas.io.json import json_normalize

!conda install -c conda-forge folium=0.5.0 --yes
import folium # plotting library

print('Folium installed')
print('Libraries imported.')"""


# In[2]:


"""import geocoder # import geocoder

# initialize your variable to None
lat_lng_coords = None

# loop until you get the coordinates
while(lat_lng_coords is None):
  g = geocoder.google('{}, Toronto, Ontario'.format(postal_code))
  lat_lng_coords = g.latlng

latitude = lat_lng_coords[0]
longitude = lat_lng_coords[1]"""


# In[3]:


import pandas as pd # library for data analsysis
import numpy as np # library to handle data in a vectorized manner

link = "http://cocl.us/Geospatial_data"
df1 = pd.read_csv(link)

df1.head()


# In[5]:


df1.shape


# In[6]:


#Changing the column name Postal code to Postcode to merge the two data frames together

df1.columns = ['Postcode','Latitude','Longitude']

cols = df1.columns.tolist()
cols


# In[7]:


link = "https://raw.githubusercontent.com/Shekhar-rv/Coursera_Capstone/master/df_can.csv"
df = pd.read_csv(link,index_col=0)
df.head()


# In[8]:


#MERGING TWO DATAFRAMES TOGETHER

df_new = pd.merge(df, df1, on='Postcode')
df_new.head()


# In[9]:


#SAVE FILE
df_new.to_csv(r'df_final.csv')


# In[ ]:




