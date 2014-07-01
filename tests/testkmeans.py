"""Run tests for the kmeans portion of the kmeans module"""
import kmeans.kmeans as k
import random
import py.test



def test_1dim_distance():
    num1 = random.random()
    num2 = random.random()
    assert k.ndim_euclidean_distance([num1],[num2]) == abs(num1-num2)
