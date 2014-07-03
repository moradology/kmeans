#!/usr/bin/env python
"""kmeans cluster algorithm and various helper functions; implemented
specifically to handle hexoskin result data"""

import numpy as np

ITER_LIMIT = 30


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
    if iterations >= ITER_LIMIT:
        condition = False
    else:
        condition = not np.allclose(old_centroids, new_centroids, rtol=1e-40)
        '''print 'old'
        print old_centroids
        print 'new'
        print new_centroids
        print np.allclose(old_centroids, new_centroids, rtol=1e-40)'''
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
    k = np.size(centroids, 0)
    dimensions = np.size(centroids, 1)
    new_centroids = np.empty((k, dimensions))
    #print new_centroids

    for i in xrange(k):
        # gather together the associations relevant to the given centroid
        centroid_associations = [association[0] for association in\
                centroid_association if association[1] == i]

        # use these associations to generate a list of associated observations
        associated_data = [datum for j, datum in enumerate(data)\
                if j in centroid_associations]

        if associated_data != []:
            new_centroids[i] = np.mean(associated_data, 0)
        else:
            new_centroids[i] = np.mean(data, 0)

    return new_centroids


def kmeans(k, data):
    """carry out the kmeans algorithm"""
    # initial state of centroids (random)
    dimensions = np.size(data, 1)
    new_centroids = random_centroids(k, dimensions)

    iterations = 0
    old_centroids = np.empty((k, dimensions))

    while should_iter(old_centroids, new_centroids, iterations):
        #print "iterating..."
        old_centroids = new_centroids
        iterations = iterations + 1

        centroid_mapping = assign_centroid(data, new_centroids)
        new_centroids = iterated_centroid(data, old_centroids,\
                centroid_mapping)

    print new_centroids
    return new_centroids



if __name__ == "__main__":
    pass
