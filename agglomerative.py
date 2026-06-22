import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage,dendrogram
from sklearn.datasets import load_iris

iris=load_iris()
data=iris.data[:6]

def proximity_matrix(data):
  n=data.shape[0]
  pm=np.zeros((n,n))
  for i in range(n):
    for j in range(i+1,n):
      pm[i,j]=np.linalg.norm(data[i]-data[j])
      pm[j,i]=pm[i,j]
  return pm

def plot_dendrogram(data,method):
  linkage_matrix=linkage(data,method=method)
  dendrogram(linkage_matrix)
  plt.title(f"{method}")
  plt.show()
pm=proximity_matrix(data)
print(pm)
plot_dendrogram(data,'single')
plot_dendrogram(data,'complete')
