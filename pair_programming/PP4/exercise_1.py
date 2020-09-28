#!/usr/bin/env python3

# Sharer: Matheus C. Fernandes
# Coder: Yuxi Liu
# Listener: Xiaolan Ke

import numpy as np

# outer closure function initializing a layer
def layer(shape,actv):
    # inner closure atribute/function to compute the outputs given inputs and activation function
    def node(inputs,weights,bias):
        h_out = actv(np.dot(inputs,weights)+bias)
        return h_out
    return node

# creating the first input to the network
t = np.random.uniform(0.0, 1.0, 100).reshape(1,-1)

# reducing the shape of output
shape1 = [100,50]
shape2 = [50,5]

# calling the closure function, initializing the layer
layer1 = layer(shape1, np.tanh) 
layer2 = layer(shape2, np.tanh) 

# Initialize weights and biases
w1 = np.array([[1]*shape1[0]]*shape1[1]).T
w2 = np.array([[2]*shape2[0]]*shape2[1]).T
b1 = np.array([[2]*shape1[1]])
b2 = np.array([[1]*shape2[1]])

# Run through the network
h1 = layer1(t, w1, b1) # First layer
h2 = layer2(h1, w2, b2) # Last layer