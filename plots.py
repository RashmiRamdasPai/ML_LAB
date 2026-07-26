
#Scatter Plot
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
y = iris.target
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Scatter Plot")
plt.show()


#3d Surface plots
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
X = load_iris().data
x = X[:, 2]
y = X[:, 3]
Xg, Yg = np.meshgrid(
    np.linspace(min(x), max(x), 50),
    np.linspace(min(y), max(y), 50)
)
Z = np.sin(Xg) * np.cos(Yg)
ax = plt.axes(projection='3d')
ax.plot_surface(Xg, Yg, Z)
plt.title("3D Surface Plot")
plt.show()


#Contour plot
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
# Load Iris dataset
iris = load_iris()
X = iris.data
# Select 2 features
x = X[:, 2]  # Petal Length
y = X[:, 3]  # Petal Width
# Create grid
xg = np.linspace(x.min(), x.max(), 100)
yg = np.linspace(y.min(), y.max(), 100)
Xg, Yg = np.meshgrid(xg, yg)
# Sample function for contour levels
Z = Xg**2 + Yg**2
# Draw contour plot
plt.contour(Xg, Yg, Z, 10)
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.title("Contour Plot of Iris Features")
plt.show()


#Heatmap
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
# Load Iris dataset
iris = load_iris()
# Create DataFrame
data = pd.DataFrame(iris.data, columns=iris.feature_names)
# Heatmap
sns.heatmap(data.corr(), annot=True)
plt.title("Iris Dataset Heatmap")
plt.show()


#BoxPlot
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
X = load_iris().data
plt.boxplot(X)
plt.title("Box Plot")
plt.show()
