#!/usr/bin/env python
# coding: utf-8


#Author:Nichole Etienne 
#Date: Wednesday September 23, 2021
#This code is meant to apply the unsupervised K-means Algorithm to the famous Old Faithful Geyser Dataset


#import the required Libraries
## matplotlib.pyplot: a collection of command style functions that make matplotlib work like MATLAB
#pandas: data analysis tool kit 
#Seaborn: library for making statistical graphics in Python
#warning :ignore warnings
#StandardScaler: for Standardize features
# KMeans: for kmeans clustering 
import matplotlib.pyplot as plt 
import pandas as pd
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings('ignore')
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


# Import the old Faithful Geyser Dataset
data= pd.read_csv('./Desktop/OFData.csv')


# Standardize features by removing the mean and scaling to unit variance
StandardizedData = StandardScaler().fit_transform(data)


#apply kmeans 
kmeansalgorithm = KMeans(n_clusters=2, max_iter=100)
kmeansalgorithm.fit(StandardizedData)
# cluster_centers_ is called the code book and each value returned by predict is the index of the closest code in the code book.
centroids = kmeansalgorithm.cluster_centers_

print (centroids)

# Plot Kmeans Cluster of the Dataset k=2
fig, ax = plt.subplots(figsize=(10, 10))
plt.scatter(StandardizedData[kmeansalgorithm.labels_ == 0, 0], StandardizedData[kmeansalgorithm.labels_ == 0, 1],
            c='purple', label='cluster 1')
plt.scatter(StandardizedData[kmeansalgorithm.labels_ == 1, 0], StandardizedData[kmeansalgorithm.labels_ == 1, 1],
            c='black', label='cluster 2')
plt.scatter(centroids[:, 0], centroids[:, 1], marker='X', s=100,
            c='r', label='centroid')
plt.legend()
plt.xlim([-2.5, 2.5])
plt.ylim([-2.5, 2.5])
plt.xlabel('Duration of the eruption(minutes)', fontsize=12)
plt.ylabel('Waiting time between eruptions (minutes)', fontsize=12)
plt.title('Kmeans Clustering Plot of Old Faithful Geyser, when K=2',  fontsize=18)
ax.set_aspect('equal')

# Run the Elblow Method 

WSS = []
Kvalues = list(range(1, 10))

for k in list_k:
    kmalgorithm = KMeans(n_clusters=k)
    kmalgorithm.fit(StandardizedData)
    WSS.append(kmalgorithm.inertia_)

# Plot The Sum of square erros and the Number of clusters : K 
plt.figure(figsize=(10, 10))
plt.plot(Kvalues, WSS, '-o')
plt.xlabel(r'The number of clusters : K ')
plt.ylabel('The sum of squared distance')
plt.title('The Elbow Method on Old Faithful Geyser',  fontsize=18)


