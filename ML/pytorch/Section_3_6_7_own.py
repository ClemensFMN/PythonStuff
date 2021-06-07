import torch
from torch import nn
from torch.utils import data
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_classification


# boilerplate start

def accuracy(y_hat, y):  #@save
    """Compute the number of correct predictions."""
    if len(y_hat.shape) > 1 and y_hat.shape[1] > 1:
        y_hat = y_hat.argmax(axis=1)
    cmp = y_hat.type(y.dtype) == y
    return float(cmp.type(y.dtype).sum())


def evaluate_accuracy(net, data_iter):  #@save
    """Compute the accuracy for a model on a dataset."""
    if isinstance(net, torch.nn.Module):
        net.eval()  # Set the model to evaluation mode
    metric = Accumulator(2)  # No. of correct predictions, no. of predictions
    for X, y in data_iter:
        metric.add(accuracy(net(X), y), y.numel())
    return metric[0] / metric[1]




def train_epoch(net, train_iter, loss, updater):  #@save
    """The training loop defined in Chapter 3."""
    # Set the model to training mode
    # if isinstance(net, torch.nn.Module):
    net.train()
    for X, y in train_iter:
        # Compute gradients and update parameters
        y_hat = net(X.float())
        l = loss(y_hat, y)
        # Using PyTorch in-built optimizer & loss criterion
        updater.zero_grad()
        l.backward()
        updater.step()



def train(net, train_iter, loss, num_epochs, updater):  #@save
    """Train a model (defined in Chapter 3)."""
    for epoch in range(num_epochs):
        train_epoch(net, train_iter, loss, updater)


def synthetic_data(num_examples):  #@save
    X, Y = make_classification(n_samples=num_examples, n_features=2, n_redundant=0, n_informative=1,
                             n_clusters_per_class=1)
    return X, Y


def load_array(data_arrays, batch_size, is_train=True):  #@save
    """Construct a PyTorch data iterator."""
    dataset = data.TensorDataset(*data_arrays)
    return data.DataLoader(dataset, batch_size, shuffle=is_train)




# boilerplate end


# we want to classify a 2-d input into 2 classes
# net = nn.Sequential(nn.Linear(2, 2))
net = nn.Sequential(nn.Linear(2, 2), nn.Softmax())


def init_weights(m):
    if type(m) == nn.Linear:
        nn.init.normal_(m.weight, std=0.01)

net.apply(init_weights);


loss = nn.CrossEntropyLoss()


trainer = torch.optim.SGD(net.parameters(), lr=0.1)
# trainer = torch.optim.Adam(net.parameters(), lr=0.001)


batch_size = 10

features, labels = synthetic_data(100)
f = torch.tensor(features)
l = torch.tensor(labels)

data_iter = load_array((f, l), batch_size)


num_epochs = 10
train(net, data_iter, loss, num_epochs, trainer)

# whatever this means
net[0].weight

# try it out
plt.scatter(f[:, 0], f[:, 1], marker='o', c=l, s=25, edgecolor='k')
plt.show()

xpred=torch.tensor([0, -2])
net(xpred.float())


