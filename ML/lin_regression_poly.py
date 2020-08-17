#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 14:26:04 2019

@author: clnovak
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression



N = 10

X = 2 * np.random.rand(N, 1)
y = 4 + 3 * X + 0.1*X**2 + np.random.randn(N, 1)

# plt.plot(X,y,'r+')

poly_features = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly_features.transform(X)

lin_reg = LinearRegression()
lin_reg.fit(X_poly, y)

print(lin_reg.intercept_, lin_reg.coef_)

#ypred = lin_reg.intercept_ + X*lin_reg.coef_

#plt.plot(X, y, 'r+', X, ypred, '-go')
