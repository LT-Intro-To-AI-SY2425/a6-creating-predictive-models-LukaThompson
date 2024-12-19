import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Import the data
data = pd.read_csv("part5-unsupervised-learning/customer_data.csv")

# Select features (Annual Income and Spending Score)
x = data[["Annual Income", "Spending Score"]]

# Standardize the data
x_std = StandardScaler().fit_transform(x) 

# Set the value of k
k = 5

# Apply the KMeans algorithm
km = KMeans(n_clusters=k)
km.fit(x_std)

# Get the centroid and label values
centroids = km.cluster_centers_
labels = km.labels_

# Set the size of the graph
plt.figure(figsize=(8, 6))

# Use a for loop to plot the data points in each cluster
for i in range(k):
    cluster = x_std[labels == i]
    plt.scatter(cluster[:, 0], cluster[:, 1], label=f'Cluster {i+1}')

# Plot the centroids
plt.scatter(centroids[:, 0], centroids[:, 1], marker='X', s=100,
            c='r', label='Centroids')

# Show the graph
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.legend()
plt.title("KMeans Clustering of Customers")
plt.show()
