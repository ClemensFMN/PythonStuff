# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 11:38:25 2024

@author: 700001473
"""

# https://pytorch.org/tutorials/beginner/introyt/autogradyt_tutorial.html

import torch
import torch.nn as nn            # for torch.nn.Module, the parent object for PyTorch models

# ***********************************
# PyTorch Models & autograd
# ***********************************

# let's try with a simple model first
# y = sum(2*x**2 + 0.6)

x = torch.linspace(0, 5, steps = 6, requires_grad=True)
print(x)

d = 2 * x**2 + 0.6
# y = \sum_{i=0}^5 2 x_i^2 + 0.6
y = d.sum()
print(y)


# calc the gradient, that is dy / dx_i for i=0...5
# analytically, this is (4x_0 4x_1 4x_2 4x_3 4x_4 4x_5)
y.backward()
print(x.grad)


# now define the model by means of a class
# the model takes 3 input values and produces 1 output value (the weighted sum of the 3 inputs + bias)
class MyNet(nn.Module):
    def __init__(self):
        super(MyNet, self).__init__()
        self.layer1 = nn.Linear(3,1)

    def forward(self, x):
        x = self.layer1(x)
        return(x)


model = MyNet()
print(model.layer1.weight)
print(model.layer1.bias)

x = torch.tensor([1.,2.,3.])
y = model(x) # apply the model to the input
print(y)

# in fact, this happens
temp = model.layer1.weight[0,:]*x
print(temp.sum() + model.layer1.bias)

# calc the gradient wrt to the weights 
y.backward()
# this is correct as we have y = \sum_i w_i x_i + b and therefore
# dy / dw_i = x_i
print(model.layer1.weight.grad)

