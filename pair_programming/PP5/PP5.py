#!/usr/bin/env python3

# Sharer: Matheus C. Fernandes, Manana Hakobyan, Jim Zhang
# Coder: Manana Hakobyan, Jim Zhang, Matheus C. Fernandes
# Listener: Jim Zhang, Matheus C. Fernandes, Manana Hakobyan

import numpy as np


class Layer():

    def __init__(self, shape, actv):
        self.shape = shape
        self.actv = actv
        self.w = np.random.uniform(0,1,shape[0]*shape[1]).reshape(shape)
        self.b = np.random.uniform(shape[1])
        

    def forward(self,inputs):
        h_out = self.actv(np.dot(inputs,self.w)+self.b)
        return h_out

    def __str__(self):
        return f'''Layer with activation {self.actv} and shape {self.shape}'''

    def __repr__(self):
        class_name=type(self).__name__
        return "{}({},{})".format(class_name,self.shape[0],self.shape[1])
        

    def __eq__(self, other):
        return (self.shape == other.shape and self.actv == other.actv)

inputs = np.random.uniform(0.0, 1.0, 100).reshape(1,-1)

actv= np.tanh
shape1 = [100,50]
shape2 = [50,5]
inputs = np.random.uniform(0.0, 1.0, 100).reshape(1,-1)

layer1 = Layer(shape1, actv)
layer2 = Layer(shape2, actv)

print(layer1)
print(layer1==layer2)

h1 = layer1.forward(inputs)
h2 = layer2.forward(h1)
    

