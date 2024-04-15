# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 09:23:06 2024

@author: 700001473
"""

import rebound
import numpy as np
import matplotlib.pyplot as plt


sim = rebound.Simulation()
# sim.start_server(port=1234)

sim.add(m=1.)
# sim.add(m=1e-3, a=1., e=0.1)
sim.add(m=1e-6, x = 1.0, y = 0.0, vx = 0.0, vy = 0.7)

Nout = 1000
# times = np.linspace(0,16.*np.pi,Nout) # 8 years
times = np.linspace(0, 5.0, Nout)
x = np.zeros((sim.N,Nout))
y = np.zeros((sim.N,Nout))


ps = sim.particles
for ti,t in enumerate(times):
    sim.integrate(t)
    for i, p in enumerate(ps):
        x[i][ti] = p.x
        y[i][ti] = p.y


for i in xrange(0,sim.N):
        plt.plot(x[i],y[i])

plt.grid(True)