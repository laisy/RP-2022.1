from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn_extra.cluster import KMedoids
from sklearn.neighbors import KNeighborsClassifier

# Load the Iris dataset
iris = load_iris()

# Split the data into training and testing sets using a Stratified Holdout 50/50
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.5, stratify=iris.target)

# Initialize the k-medoids model with k=9
n_clusters = 9
kmedoids = KMedoids(n_clusters=n_clusters, random_state=0)

# Fit the k-medoids model to the training data
kmedoids.fit(X_train)

# Remove non-centroid elements from the test set
X_test_centroids = X_test[kmedoids.medoid_indices_]
y_test_centroids = y_test[kmedoids.medoid_indices_]

# Initialize the 1-NN classifier with Euclidean distance
knn = KNeighborsClassifier(n_neighbors=1)

# Fit the 1-NN classifier to the training data
knn.fit(X_train, y_train)

# Predict the class labels for the centroids in the test set using the 1-NN classifier
y_pred_test = knn.predict(X_test_centroids)

# Calculate the accuracy rate by class on the training set using the 1-NN classifier
y_pred_train = knn.predict(X_train)
accuracy_train_by_class = []
for i in range(3):
    indices = (y_train == i)
    accuracy_train = sum(y_pred_train[indices] == y_train[indices]) / sum(indices)
    accuracy_train_by_class.append(accuracy_train)
print(f"Training accuracy by class: {accuracy_train_by_class}")