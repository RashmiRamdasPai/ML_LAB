import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Load Glass dataset
glass_df = pd.read_csv(r"C:\Users\Tripti\OneDrive\Documents\Downloads\archive (1)\glass.csv")

# Create input (X) and output (y)
X = glass_df.drop('Type', axis=1)
y = glass_df['Type']

# Split dataset into 70% training and 30% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# -------------------------------
# Manual Distance Functions
# -------------------------------

def euclidean_distance(x, y):
    return np.sqrt(np.sum((x - y) ** 2))

def manhattan_distance(x, y):
    return np.sum(np.abs(x - y))

# Distance metrics to be used
distance_metrics = [
    ("Euclidean", euclidean_distance),
    ("Manhattan", manhattan_distance)
]

# Run KNN for both distance metrics
for name, metric in distance_metrics:

    # Create KNN model with K = 3
    knn = KNeighborsClassifier(
        n_neighbors=3,
        metric=metric,
        algorithm='brute'
    )

    # Train the model
    knn.fit(X_train, y_train)

    # Predict test data
    y_pred = knn.predict(X_test)

    # Calculate accuracy
    acc = accuracy_score(y_test, y_pred)

    # Generate confusion matrix
    cm = confusion_matrix(y_test, y_pred)

    # Display results
    print(f"\n--- KNN with {name} Distance ---")
    print("Accuracy:", round(acc * 100, 4), "%")
    print("Confusion Matrix:")
    print(cm)
