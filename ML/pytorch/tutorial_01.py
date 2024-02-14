# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 11:15:00 2024

@author: 700001473
"""

# https://pytorch.org/tutorials/beginner/introyt/introyt1_tutorial.html
# https://pytorch.org/tutorials/beginner/introyt/tensors_deeper_tutorial.html

import torch


# ***********************************
# PyTorch Tensors
# ***********************************

z = torch.zeros(5, 3)
print(z)
print(z.dtype)


i = torch.ones((5, 3), dtype=torch.int16)
print(i)


torch.manual_seed(1729)
r1 = torch.rand(2, 2)
print('A random tensor:')
print(r1)

r2 = torch.rand(2, 2)
print('\nA different random tensor:')
print(r2) # new values

torch.manual_seed(1729)
r3 = torch.rand(2, 2)
print('\nShould match r1:')
print(r3) # repeats values of r1 because of re-seed

ones = torch.ones(2, 3)
print(ones)

twos = torch.ones(2, 3) * 2 # every element is multiplied by 2
print(twos)

threes = ones + twos       # addition allowed because shapes are similar
print(threes)              # tensors are added element-wise
print(threes.shape)        # this has the same dimensions as input tensors


zeros_like = torch.zeros_like(threes)
ones_like = torch.ones_like(threes)
rand_like = torch.rand_like(threes)
print(zeros_like)
print(ones_like)
print(rand_like)


# create tensors from normal python types
some_constants = torch.tensor([[3.1415926, 2.71828], [1.61803, 0.0072897]])
print(some_constants)

some_integers = torch.tensor((2, 3, 5, 7, 11, 13, 17, 19))
print(some_integers)

more_integers = torch.tensor(((2, 4, 6), [3, 6, 9]))
print(more_integers)


# copy vs clone
a = torch.ones(2, 2)
b = a
c = a.clone()

a[0][1] = 561  # we change a...
print(b)       # ...and b is also altered
print(c)       # ... but NOT c


# squeeze
# imagine a picture with 3 color channels & 5 x 5 pixels
a = torch.rand(3,5,5)
print(a.shape)
print(a)
# now we want a batch -> use unsqueeze
b = a.unsqueeze(0)
print(b.shape)
print(b)


