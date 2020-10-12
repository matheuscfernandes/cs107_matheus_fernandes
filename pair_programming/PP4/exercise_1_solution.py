import numpy as np

def layer(shape, actv):
    def eval_layer(inputs, weights, bias):
        z = np.dot(inputs, weights) + bias
        z = actv(z)
        return z
    return eval_layer

if __name__ == "__main__":

    N = 100 # Number of input points
    W = 3 # Width of layers
    C = 1 # Number of outputs

    t = np.random.uniform(0.0, 1.0, 100).reshape(1,-1) # Input data

    shape1 = [np.size(t), W] # Size of layer 1
    layer1 = layer(shape1, np.tanh) # Instantiate layer 1
    
    shape2 = [W, C] # Size of layer 2 (it's the output layer here)
    layer2 = layer(shape2, np.tanh) # Instantiate layer 2

    # Random initializations of weights
    w1 = np.random.uniform(-1.0, 1.0, size=shape1)
    b1 = np.random.normal(0.0, 0.1, size=shape1[1])
    
    w2 = np.random.uniform(-1.0, 1.0, size=shape2)
    b2 = np.random.normal(0.0, 0.1, size=shape2[1])

    h1 = layer1(t, w1, b1) # Pass input through layer 1
    h2 = layer2(h1, w2, b2) # Pass output of layer 1 through layer 2

    print(h2)
