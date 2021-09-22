#!/usr/bin/env python
# coding: utf-8

# In[70]:


#Author:Nichole Etienne 
#Date: Wednesday September 23, 2021
#This code is meant to be the preprocessing for the  unsupervised K-means Algorithm to the famous Old Faithful Geyser Dataset


#import the required Libraries
## matplotlib.pyplot: a collection of command style functions that make matplotlib work like MATLAB
#pandas: data analysis tool kit 
#Seaborn: library for making statistical graphics in Python
import matplotlib.pyplot as plt 
import pandas as pd
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
#ignore warnings 
import warnings
warnings.filterwarnings('ignore')



# Import the Facebook Live Sellers in the old Faithful Geyser Dataset
data= pd.read_csv('./Desktop/OFData.csv')


# the top 5 observations in the dataset 
data.head()


#.info prints information about a DataFrame including the index dtype and columns, non-null values and memory usage
data.info


#return the missing variables within the data set 
data.isnull().sum()


#Since there are no missing , we may proceeed to analysis.
#That is first plotting the raw data 

#plot the raw data 
plt.figure(figsize=(10, 10))
plt.scatter(data.iloc[:, 0], data.iloc[:, 1])
plt.xlabel('duration of the eruption(minutes)', fontsize=12)
plt.ylabel('Waiting time between eruptions (minutes)', fontsize=12)
plt.title('Scattered Plot of Old Faithful Geyser Raw Data', fontsize= 18)







