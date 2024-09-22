def f(x):
    return(x**2)


def fprime(x):
    return(2*x)

x = 1.0

for n in range(10):
    xnp1 = x - f(x) / fprime(x)
    print(n, xnp1)
    x = xnp1


