import sympy as sym


x, y = sym.symbols('x y')


expr = x + 2*y

print(expr)


expr2 = expr**2

print(sym.expand(expr2))

expr3 = x**2 - 4
res = sym.solve(expr3, x)
print(res)


