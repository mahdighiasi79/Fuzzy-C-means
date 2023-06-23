import random
import pandas as pd
import numpy as np

num_iterations = 100
C = 3
m = 3

df = pd.read_csv("data1.csv")
dimension = len(df.iloc(0)[0])
centroids = np.zeros((C, dimension))


def euclidean_distance(point1, point2):
    distance = point1 - point2
    distance = np.power(distance, 2)
    distance = np.sum(distance, keepdims=False)
    distance = pow(distance, 0.5)
    return distance


def belonging(k, i):
    k_th_record = np.array(df.iloc(0)[k])
    i_th_centroid = centroids[i]
    dist_k_i = euclidean_distance(k_th_record, i_th_centroid)

    u_ik = 0
    for center in centroids:
        temp = euclidean_distance(k_th_record, center)
        temp = dist_k_i / temp
        temp = pow(temp, 2 / (1 - m))
        u_ik += temp
    u_ik = 1 / u_ik
    return u_ik


def fuzzy_c_means():
    for i in range(C):
        for j in range(dimension):
            centroids[i][j] = random.random()

    for i in range(num_iterations):
        for c in range(C):
            numerator = 0
            denominator = 0
            for j in range(len(df)):
                record = np.array(df.iloc(0)[j])
                u = belonging(j, c)
                u = pow(u, m)
                numerator += u * record
                denominator += u
            centroids[c] = numerator / denominator


def cluster(k):
    record = np.array(df.iloc(0)[k])
    nearest_center = -1
    lowest_distance = np.inf
    for i in range(C):
        distance = euclidean_distance(centroids[i], record)
        if distance <= lowest_distance:
            lowest_distance = distance
            nearest_center = i
    return nearest_center


if __name__ == '__main__':
    arr1 = np.array([1, 1, 2])
    arr2 = np.array([3, 0, 4])
    arr2 += arr1
    print(arr2)
