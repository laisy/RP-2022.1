import pandas as pd
from sklearn.cluster import KMeans
import numpy as np

# Load the Iris dataset
iris = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", header=None)
iris.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

# Set the features we want to use for clustering
X = iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]

# Calculate the distance of each example to the closest centroid during each iteration
distance_to_centroids = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42, max_iter=i).fit(X)
    distance = kmeans.transform(X).min(axis=1)
    distance_to_centroids.append(distance)

# Calculate the mean and deviation pattern of the distances for each iteration
mean_pattern = [np.mean(distance) for distance in distance_to_centroids]
deviation_pattern = [np.std(distance) for distance in distance_to_centroids]

# Create a table with the mean and deviation pattern of the distances for each iteration
table = pd.DataFrame({'média': mean_pattern, 'desvio': deviation_pattern}, index=range(1, 11))
print(table)