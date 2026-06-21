import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Step 1: Standardize the data
scaler = StandardScaler()
X_std = scaler.fit_transform(X)

# Step 2: Compute covariance matrix
cov_matrix = np.cov(X_std.T)

# Step 3: Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

# Step 4: Sort eigenvalues and eigenvectors
sorted_index = np.argsort(eigenvalues)[::-1]
sorted_eigenvalues = eigenvalues[sorted_index]
sorted_eigenvectors = eigenvectors[:, sorted_index]

# Step 5: Select first 2 principal components
n_components = 2
principal_components = sorted_eigenvectors[:, :n_components]

# Step 6: Transform the data
X_pca = X_std.dot(principal_components)

print("Original Shape:", X.shape)
print("Reduced Shape:", X_pca.shape)
print("\nFirst 5 PCA-transformed samples:")
print(X_pca[:5])

# Step 7: Scatter Plot
plt.figure(figsize=(8, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis')

plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA of Iris Dataset")
plt.colorbar(label="Flower Class")
plt.grid(True)
plt.show()
