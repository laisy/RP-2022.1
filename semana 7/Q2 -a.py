from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn_extra.cluster import KMedoids

# Load the Iris dataset
iris = load_iris()

# Split the data into training and testing sets using a Stratified Holdout 50/50
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.5, stratify=iris.target)

# Initialize the k-medoids model with k=9
n_clusters = 9
kmedoids = KMedoids(n_clusters=n_clusters, random_state=0)

# Fit the k-medoids model to the training data
kmedoids.fit(X_train)