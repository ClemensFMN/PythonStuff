# cordic in rotation mode for calculating sin / cos
# Inspired by https://en.wikipedia.org/wiki/CORDIC

from math import atan2, sqrt, sin, cos, radians

ITERS = 10
theta_table = [atan2(1, 2**i) for i in range(ITERS)]

def compute_K(n):
    """
    Compute K(n) for n = ITERS. This could also be
    stored as an explicit constant if ITERS above is fixed.
    """
    k = 1.0
    for i in range(n):
        k *= 1 / sqrt(1 + 2 ** (-2 * i))
    return k

def CORDIC(alpha, n):
    K_n = compute_K(n)
    theta = 0.0
    x = 1.0
    y = 0.0
    P2i = 1  # This will be 2**(-i) in the loop below
    for arc_tangent in theta_table:
        sigma = +1 if theta < alpha else -1
        theta += sigma * arc_tangent
        x, y = x - sigma * y * P2i, sigma * P2i * x + y
        P2i /= 2
    return x * K_n, y * K_n

if __name__ == "__main__":
    # calc sin/cos for value beta
    beta = radians(45)
    cos_x, sin_x = CORDIC(beta, ITERS)
    cos_true = cos(beta)
    sin_true = sin(beta)
    print(
        f"Values for beta {beta:.8f} \n CORDIC: cos = {cos_x:.8f}, sin = {sin_x:.8f}\n True:   cos = {cos_true:.8f}, sin = {sin_true:.8f}"
    )

