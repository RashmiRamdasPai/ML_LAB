import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

def mlp(x, w1, b1, w2, b2):

    # Hidden Layer
    hidden = sigmoid(np.dot(x, w1) + b1)

    # Output Layer
    output = sigmoid(np.dot(hidden, w2) + b2)

    return 1 if output >= 0.5 else 0

X = np.array([[0,0],[0,1],[1,0],[1,1]])

# AND Gate
print("AND Gate")

w1 = np.array([[1,1],
               [1,1]])
b1 = np.array([-0.5,-0.5])

w2 = np.array([1,1])
b2 = -1.5

for x in X:
    print(x, "->", mlp(x,w1,b1,w2,b2))

# OR Gate
print("\nOR Gate")

b2 = -0.5

for x in X:
    print(x, "->", mlp(x,w1,b1,w2,b2))

# NOT Gate
print("\nNOT Gate")

X_not = np.array([0,1])

for x in X_not:
    y = sigmoid(-2*x + 1)
    output = 1 if y >= 0.5 else 0
    print(x, "->", output)
print("\nAND-NOT Gate")

#And-Not
for x in X:
    output = 1 if (x[0] == 1 and x[1] == 0) else 0
    print(x, "->", output)

#XOR
print("\nXOR Gate")

for x in X:
    output = 1 if x[0] != x[1] else 0
    print(x, "->", output)
