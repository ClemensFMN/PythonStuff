# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 14:44:49 2024

@author: 700001473
"""

# inspired by https://pytorch.org/tutorials/beginner/nn_tutorial.html
# that's actually a complete model optimizer script
# model is defined in MyNet
# loss function & optimizer are defined below
# we use random training data
# training data is batched & used for training the model (over several epochs

import torch
import torch.nn as nn
from torch.utils.data import TensorDataset, DataLoader


# now define the model by means of a class
# the model takes 3 input values and produces 1 output value (the weighted sum of the 3 inputs + bias)
class MyNet(nn.Module):
    def __init__(self):
        super(MyNet, self).__init__()
        self.layer1 = nn.Linear(3,1)

    def forward(self, x):
        x = self.layer1(x)
        return(x)

loss_fn = torch.nn.MSELoss(reduction='sum')
model = MyNet()
learning_rate = 1e-3
opt = torch.optim.RMSprop(model.parameters(), lr=learning_rate)


# the training data matches the model
# we have 20 observations, each has 3 input values & 1 output value
x_train = torch.rand(20,3)
y_train = torch.rand(20,1)

# we split the training data into batches of size 5
bs = 5
train_ds = TensorDataset(x_train, y_train)
train_dl = DataLoader(train_ds, batch_size=bs, shuffle=True)

epochs = 10

# we iterate epochs times across the training data
# the shuffle=True in the DataLoader above ensures that each batch in each epoch contains different data
# so there is enough "variety" to train the model
for epoch in range(epochs):

    # now we run over all batches & optim the model
    for xb,yb in train_dl:
        # print(xb)
        pred = model(xb)
        loss = loss_fn(pred, yb)
    
        loss.backward()
        opt.step()
        opt.zero_grad()
    
    print(loss_fn(model(xb), yb))


