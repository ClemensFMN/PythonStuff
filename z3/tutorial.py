# taken from https://github.com/Z3Prover/z3/blob/master/examples/python/tutorial/jupyter/guide.ipynb

from z3 import *

x = Int('x')
y = Int('y')
solve(x > 0, x < 10, y > 0, y < 10, x + y == 10)
