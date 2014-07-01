#!/usr/bin/env python
"""kmeans cluster algorithm and various helper functions; implemented
specifically to handle hexoskin result data"""

import numpy as np

MAX_ITERATIONS = 30


def ndim_euclidean_distance(point1, point2):
    """Calculate euclidean distance between two points in n-dimensions.
    This utility is a simple function composition of the form:
    sqrt . sum . matrixSquare . matrixSubtract point1 point2
    in polish notation or, in more familiar notation,
    sqrt((point1[0]-point2[0])^2+(point1[1]-point2[1])^2+...
    (point1[n-1]-point2[n-1]^2))"""
    if type(point1) == 'list':
        pnt1 = point1
    else:
        pnt1 = [point1]

    if type(point2) == 'list':
        pnt2 = point2
    else:
        pnt2 = [point2]

    distance = np.sqrt(np.sum(np.square(np.subtract(pnt1, pnt2))))
    return distance


def should_iter(old_centroids, new_centroids, iterations):
    """Check to see if the iteration bank is empty, if not, compare centroids
    to determine whether or not further iteration is necessary"""
    if iterations >= MAX_ITERATIONS:
        condition = False
    else:
        condition = old_centroids == new_centroids
    return condition


def assign_centroid(data, centroids):
    """Find the nearest centroid from a given list - return a tuple mapping
    the indexes in format (data_point, centroid)"""
    centroid_association = []

    for i, datum in enumerate(data):
        for j, centroid in enumerate(centroids):
            if j == 0:
                nearest_centroid = j
                nearest_distance = ndim_euclidean_distance(datum, centroid)
            else:
                compare_distance = ndim_euclidean_distance(datum, centroid)
                if nearest_distance > compare_distance:
                    nearest_centroid = j
                    nearest_distance = compare_distance

        centroid_association.append((i, nearest_centroid))
    return centroid_association


if __name__ == "__main__":
    pass
