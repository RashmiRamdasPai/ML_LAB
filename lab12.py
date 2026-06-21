import numpy as np

def perceptron(x, w, b):
    y = np.dot(x, w) + b
    return 1 if y >= 0 else 0

# AND Function
print("AND Gate")
X = np.array([[0,0],[0,1],[1,0],[1,1]])
w = np.array([1,1])
b = -1.5

for x in X:
    print(x, "->", perceptron(x, w, b))

# OR Function
print("\nOR Gate")
b = -0.5

for x in X:
    print(x, "->", perceptron(x, w, b))
