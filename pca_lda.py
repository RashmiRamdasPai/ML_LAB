import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA 


iris=load_iris()
X=iris.data
y=iris.target
print("original data shape was ",X.shape)
pca=PCA(n_components=2)
X_pca=pca.fit_transform(X)
print("Reduced pca shape was ",X_pca.shape)

plt.scatter(X_pca[:,0],X_pca[:,1],c=y)
plt.show()

lda=LDA(n_components=2)
X_lda=lda.fit_transform(X,y)
print("Reduced lda shape",X_lda.shape)
plt.scatter(X_lda[:,0],X_lda[:,1],c=y)
plt.show()
