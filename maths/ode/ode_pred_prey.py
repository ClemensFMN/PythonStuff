# Solving the predator-prey problem (Lotka-Volterra equations)
# inspired by https://notebook.basthon.fr/?kernel=python3-old&from=examples/python3-lotka-volterra.ipynb

from numpy import *
import matplotlib.pyplot as plt
from scipy import integrate

# Definition of parameters
a = 2.
b = 1.0
c = 1.0
d = 0.333
def dX_dt(X, t=0):
    """ Return the growth rate of fox and rabbit populations. """
    return array([ a*X[0] -   b*X[0]*X[1] ,
                  -c*X[1] +   d*X[0]*X[1] ])


t = linspace(0, 15,  1000)
# X0 = array([5, 0]) # no wolves
# X0 = array([0, 5]) # no rabbits
# X0 = array([3.1, 1.9])
X0 = array([1., 1.])
X = integrate.odeint(dX_dt, X0, t)

# linsol = 2 + 0.5*sin(sqrt(a*c)*t)


rabbits, foxes = X.T
f1 = plt.figure()
plt.plot(t, rabbits, 'r-', label='Rabbits')
plt.plot(t, foxes  , 'b-', label='Foxes')
# plt.plot(t, linsol  , 'k:', label='Linearization')
plt.grid()
plt.legend(loc='best')
plt.xlabel('time')
plt.ylabel('population')
plt.title('Population Evolution')
plt.show()

ymax = 5
xmax = 5
nb_points   = 20                      

x = linspace(0, xmax, nb_points)
y = linspace(0, ymax, nb_points)

X1 , Y1  = meshgrid(x, y)
DX1, DY1 = dX_dt([X1, Y1])
M = (hypot(DX1, DY1))
M[ M == 0] = 1.
DX1 /= M
DY1 /= M

#-------------------------------------------------------
# Drow direction fields, using matplotlib 's quiver function
# I choose to plot normalized arrows and to use colors to give information on
# the growth speed
plt.title('Trajectories and direction fields')
Q = plt.quiver(X1, Y1, DX1, DY1, M, pivot='mid', cmap=plt.cm.jet)
plt.xlabel('Number of rabbits')
plt.ylabel('Number of foxes')
plt.legend()
plt.grid()
plt.xlim(0, xmax)
plt.ylim(0, ymax)
plt.show()

# fixed point at
print(a / b, c / d)

