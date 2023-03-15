import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load the Iris dataset
iris = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", header=None)
iris.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

# Set the features we want to use for clustering
X = iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]

# Set the number of clusters
k = 5

# Fit the k-means algorithm to the data
kmeans = KMeans(n_clusters=k, random_state=42).fit(X)

# Add a column to the Iris dataframe with the predicted cluster label for each sample
iris['cluster'] = kmeans.predict(X)

# Group the data by the predicted cluster labels and compute the count of each class for each group
groups = iris.groupby(['cluster', 'class']).size().reset_index(name='count')

# Plot a bar graph for each group
for i in range(k):
    fig, ax = plt.subplots(figsize=(6, 4))
    group_data = groups[groups['cluster']==i]
    ax.bar(group_data['class'], group_data['count'])
    ax.set_title(f'Agrupamento {i}')
    ax.set_xlabel('Classe')
    ax.set_ylabel('Quantidade')
    plt.show()