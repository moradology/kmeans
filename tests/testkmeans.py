"""Run tests for the kmeans portion of the kmeans module"""

import kmeans.kmeans.kmeans as k
import numpy as np
import random
import pytest


def test_1dim_distance():
    """See if this contraption works in 1 dimension"""
    num1 = random.random()
    num2 = random.random()
    assert k.ndim_euclidean_distance(num1, num2) == abs(num1-num2)


def test_ndim_distance():
    """Test to see if changing val by 1 does what it ought to do
    convert to float to integer because floating arithmetic makes testing
    analytic functions a mess"""
    rand = random.random
    point1 = [rand(), rand(), rand(), rand(), rand(), rand()]
    point2 = [point1[0]+1] + point1[1:] # just shift x to the right by 1
    assert int(round(k.ndim_euclidean_distance(point1, point2))) == 1


def test_maxiters():
    """ensure the iteration ceiling works"""
    assert k.should_iter([], [], iterations=29) == True
    assert k.should_iter([], [], iterations=30) == False
    assert k.should_iter([], [], iterations=31) == False
