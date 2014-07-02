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

    for data_index, datum in enumerate(data):
        for centroid_index, centroid in enumerate(centroids):
            if centroid_index == 0:
                nearest_centroid = centroid_index
                nearest_distance = ndim_euclidean_distance(datum, centroid)
            else:
                compare_distance = ndim_euclidean_distance(datum, centroid)
                if nearest_distance > compare_distance:
                    nearest_centroid = centroid_index
                    nearest_distance = compare_distance

        centroid_association.append((data_index, nearest_centroid))
    return centroid_association


def random_centroids(k, dimensions):
    """Generate k random centroids  with specified dimensions with
    vals between 0 and 1"""
    centroids = [np.random.rand(dimensions) for _ in range(k)]
    return centroids


def iterated_centroid(data, centroids, centroid_association):
    """Find new centroids given a current association"""

    # initialize empty np.array to be filled - this is way faster than the
    # conversion of lists
    k = len(centroids)
    dimensions = len(centroids[0])
    new_centroids = np.empty((k, dimensions))
    print k
    print dimensions
    print new_centroids

    for i in xrange(k):
        # gather together the associations relevant to the given centroid
        centroid_associations = [association[0] for association in\
                centroid_association if association[1] == i]
        print centroid_associations

        # use these associations to generate a list of associated observations
        associated_data = [datum for j, datum in enumerate(data)\
                if j in centroid_associations]
        print associated_data

        new_centroids[i] = np.mean(associated_data)

    return new_centroids

if __name__ == "__main__":
    pass
