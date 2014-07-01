import numpy as np

MAX_ITERATIONS = 30

def ndim_euclidean_distance(point1, point2):
    """Calculate euclidean distance between two points in n-dimensions.
    This utility function is a simple function composition of the form:
    sqrt . sum . matrixSquare . matrixSubtract point1 point2
    or, in more familiar notation,
    sqrt((point1[0]-point2[0])^2+(point1[1]-point2[1])^2+...
    (point1[n-1]-point2[n-1]^2))"""
    distance = np.sqrt(np.sum(np.square(np.subtract(point1, point2))))
    return distance

def should_iter(old_centroids, new_centroids, iterations):
    """Check to see if the iteration bank is empty, if not, compare centroids
    to determine whether or not further iteration is necessary"""
    if iterations >= MAX_ITERATIONS:
        condition = False
    else:
        condition = old_centroids == new_centroids
    return condition


