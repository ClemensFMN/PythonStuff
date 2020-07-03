import matplotlib.pyplot as plt
import collections
import random
import math
import timeit

# convex hull algorithm based on Peter Norvig's Pytudes
# https://github.com/norvig/pytudes/blob/master/ipynb/Convex%20Hull.ipynb

Point = collections.namedtuple('Point', 'x, y')

def Points(n, seed=42):
    "Generate n random points within a 3 x 2 box."
    random.seed((n, seed))
    b = 0.05 # border
    return {Point(random.uniform(b, 3-b), random.uniform(b, 2-b)) 
            for _ in range(n)}

def turn(A, B, C):
    "Is the turn from A->B->C a 'right', 'left', or 'straight' turn?"
    diff = (B.x - A.x) * (C.y - B.y)  -  (B.y - A.y) * (C.x - B.x) 
    return ('right' if diff < 0 else
            'left'  if diff > 0 else
            'straight')


def convex_hull(points):
    "Find the convex hull of a set of points."
    if len(points) <= 3:
        return points
    # Find the two half-hulls and append them, but don't repeat first and last points
    upper = half_hull(sorted(points))
    lower = half_hull(reversed(sorted(points)))
    return upper + lower[1:-1]

def half_hull(sorted_points):
    "Return the half-hull from following points in sorted order."
    # Add each point C in order; remove previous point B if A->B-C is not a left turn.
    hull = []
    for C in sorted_points:
        # if A->B->C is not a left turn ...
        while len(hull) >= 2 and turn(hull[-2], hull[-1], C) != 'left':
            hull.pop() # ... then remove B from hull.
        hull.append(C)
    return hull

def plot_points(points, style='r.', labels=False, closed=False): 
    """Plot a collection of points. Optionally change the line style, label points with numbers, 
    and/or form a closed polygon by closing the line from the last point to the first."""
    if labels:
        for (i, (x, y)) in enumerate(points):
            plt.text(x, y, '  '+str(i))
    if closed:
        points = points + [points[0]]
    plt.plot([p.x for p in points], [p.y for p in points], style, linewidth=2.5)
    plt.axis('scaled'); plt.axis('off')


def plot_convex_hull(points):
    "Find the convex hull of these points, and show a plot."
    hull = convex_hull(points)
    plot_points(points)
    plot_points(hull, 'bs-', closed=True)
    print(len(hull), 'of', len(points), 'points on hull')

Ps = Points(100)

plot_convex_hull(Ps)
plt.show()

RUNS = 100
timeit.timeit("convex_hull(Points(1000))", globals=globals(), number=RUNS) / RUNS
timeit.timeit("convex_hull(Points(10000))", globals=globals(), number=RUNS) / RUNS
