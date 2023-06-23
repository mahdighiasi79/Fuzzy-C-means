import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random

num_iterations = 100
C = 3
m = 4

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


def cost():
    j = 0
    for k in range(len(df)):
        for i in range(C):
            j += pow(belonging(k, i), m) * euclidean_distance(centroids[i], np.array(df.iloc(0)[k]))
    return j


if __name__ == '__main__':
    # prev_cost = 1
    # for p in range(2, 10):
    #     for q in range(1, 10):
    #         m = p
    #         C = q
    #         centroids = np.zeros((C, dimension))
    #         fuzzy_c_means()
    #         print("m:", m, "  C:", C)
    #         new_cost = cost()
    #         change_percentage = (1 - (new_cost / prev_cost)) * 100
    #         print("change:", change_percentage, "%")
    #         prev_cost = new_cost
    #         print("///////////////////")

    # costs = []
    # for q in range(1, 10):
    #     C = q
    #     centroids = np.zeros((C, dimension))
    #     fuzzy_c_means()
    #     costs.append(cost())
    #
    # costs = np.array(costs)
    # plt.plot(costs, marker='o')
    # plt.show()

    # first dataset
    C = 2
    m = 4
    centroids = np.zeros((C, dimension))
    fuzzy_c_means()
    clusters = []
    for p in range(len(df)):
        clusters.append(cluster(p))

    cluster1_x = []
    cluster2_x = []
    cluster3_x = []
    cluster1_y = []
    cluster2_y = []
    cluster3_y = []
    for p in range(len(df)):
        if clusters[p] == 0:
            cluster1_x.append(df.iloc(0)[p][0])
            cluster1_y.append(df.iloc(0)[p][1])
        elif clusters[p] == 1:
            cluster2_x.append(df.iloc(0)[p][0])
            cluster2_y.append(df.iloc(0)[p][1])
        else:
            cluster3_x.append(df.iloc(0)[p][0])
            cluster3_y.append(df.iloc(0)[p][1])
    cluster1_x = np.array(cluster1_x)
    cluster2_x = np.array(cluster2_x)
    cluster3_x = np.array(cluster3_x)
    cluster1_y = np.array(cluster1_y)
    cluster2_y = np.array(cluster2_y)
    cluster3_y = np.array(cluster3_y)

    plt.scatter(cluster1_x, cluster1_y, color="red")
    plt.scatter(cluster2_x, cluster2_y, color="blue")
    plt.scatter(cluster3_x, cluster3_y, color="green")
    plt.show()
