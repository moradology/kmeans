"""Run tests for the kmeans portion of the kmeans module"""

import kmeans.kmeans.kmeans as kmeans
import numpy as np
import random


def test_1dim_distance():
    """See if this contraption works in 1 dimension"""
    num1 = random.random()
    num2 = random.random()
    assert kmeans.ndim_euclidean_distance(num1, num2) == abs(num1-num2)


def test_ndim_distance():
    """Test to see if changing val by 1 does what it ought to do
    convert to float to integer because floating arithmetic makes testing
    analytic functions a mess"""
    rand = random.random
    point1 = [rand(), rand(), rand(), rand(), rand(), rand()]
    point2 = [point1[0]+1] + point1[1:] # just shift x to the right by 1
    assert int(round(kmeans.ndim_euclidean_distance(point1, point2))) == 1


def test_maxiters():
    """ensure the iteration ceiling works"""
  #  assert kmeans.should_iter([], [], iterations=29) == True
    assert kmeans.should_iter([], [], iterations=30) == False
    assert kmeans.should_iter([], [], iterations=31) == False


def test_random_centroid_dimensions():
    """ensure the correct number of dimensions"""
    dimensions = random.randrange(1, 100)
    k = random.randrange(1, 100)
    centroids = kmeans.random_centroids(k, dimensions)
    for centroid in centroids:
        assert len(centroid) == dimensions


def test_iterated_centroid():
    """ensure that the average across each dimension is returned"""
    new_centroid = kmeans.iterated_centroid([[1, 1, 1], [2, 2, 2]],\
            [[100, 200, 300]], [(0, 0), (1, 0)])
    np.testing.assert_allclose(new_centroid, np.array([[1.5, 1.5, 1.5]]),\
            rtol=1e-5)

