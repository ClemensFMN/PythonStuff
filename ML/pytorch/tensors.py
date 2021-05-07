import torch
import numpy as np


# data = [[1, 2],[3, 4]]
data = np.linspace(0,10,11)
x_data = torch.tensor(data)
print(x_data)


rv = torch.normal(0.0, 1.0, (10,1))
print(rv)



tensor = torch.ones(4, 4)
print('First row: ',tensor[0])
print('First column: ', tensor[:, 0])
print('Last column:', tensor[..., -1])
tensor[:,1] = 0
print(tensor)

