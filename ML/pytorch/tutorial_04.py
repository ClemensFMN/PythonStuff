# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 14:41:00 2024

@author: 700001473
"""

import torch
from torch.utils.data import TensorDataset, DataLoader


x_train = torch.linspace(-3, 3, 20)
y_train = 0.4 + x_train - 1.5*x_train**2 + 1*x_train**3

bs = 5

train_ds = TensorDataset(x_train, y_train)
# the shuffle=True ensures that the data is taken non-sequentially
train_dl = DataLoader(train_ds, batch_size=bs, shuffle=True)


for xb,yb in train_dl:
    print(xb, yb)
