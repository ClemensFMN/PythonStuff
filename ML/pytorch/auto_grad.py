import torch

x = torch.arange(4.0)
print(x)
x.requires_grad_(True)
y = 2 * torch.dot(x, x) # 2 x_1^^2 + 2 x_2^2 + 2 x_3^2 + 2 x_4^2
print(y)

y.backward()
print(x.grad) # [4 x_1 4 x_2 4 x_3 4 x_4]




def f(x):
    # y = 2 * torch.dot(x,x) + torch.sum(x)
    y = 2*x[0]**2 + 3*x[1]
    return(y)

# not sure if we need this...
x.grad.zero_()
x = torch.tensor([1.5, 2.0])
x.requires_grad_(True)
print(x)
y = f(x)
print(y)

y.backward()
print(x.grad) # [4 x[0], 3]

