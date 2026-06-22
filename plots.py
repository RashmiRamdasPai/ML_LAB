#3d Scatter plot
import numpy as np
import matplotlib.pyplot as plt

# Generate data
x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)

# Create figure
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

# Scatter Plot
ax.scatter(x, y, z)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("3D Scatter Plot")

plt.show()

#3d Surface plots
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create grid data
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x, y)

# Calculate Z values
Z = np.sin(np.sqrt(X**2 + Y**2))

# Create 3D Surface Plot
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z, cmap='viridis')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Surface Plot')

plt.show()

#Contour plot
import numpy as np
import matplotlib.pyplot as plt

# Create grid data
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x, y)

# Calculate Z values
Z = np.sin(np.sqrt(X**2 + Y**2))

# Create figure
fig = plt.figure(figsize=(8,6))

# Contour Plot
plt.contour(X, Y, Z, cmap='viridis')

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Contour Plot")
plt.colorbar()

plt.show()

#Heatmap
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import pandas as pd

# Load Iris dataset
iris = load_iris()

# Create DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Create figure
fig = plt.figure(figsize=(8,6))

# Heat Map
sns.heatmap(df.corr(), annot=True, cmap='viridis')

plt.title("Heat Map of Iris Dataset")
plt.show()

#BoxPlot
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import pandas as pd

# Load Iris dataset
iris = load_iris()

# Create DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Create figure
fig = plt.figure(figsize=(8,6))

# Box Plot
sns.boxplot(data=df)

plt.title("Box Plot of Iris Dataset")
plt.show()
