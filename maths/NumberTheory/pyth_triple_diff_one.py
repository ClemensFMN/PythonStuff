from sympy import solve, symbols

s, t = symbols('s t')

# sol = solve(s**2 - 2*s*t - t**2 - 1, s)
# print(sol)

sol = solve(2*s**2 + 2*s + 1 - t**2, s)
print(sol)

