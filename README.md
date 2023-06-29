# Fuzzy-C-means
In this project, we aim to cluster some generated data points.
We have used C-means clustering algorithm for our task which works based on Fuzzy logic.
In C-meas algorithm, each data point belongs to all of the culsters. But the degree of belongings differe.
We determine the degree of belonging of a given data point to a given cluster based on its proximity to the cluster center and compare it with its proximity to other cluster centers.

The following steps represent the algorithm:
1- At first, we determine cluster centers randomly.
2- Then we will determine the belonging degree of each point to each of the clusters.
3- Finally, we will update the cluster centers based on the calculated belonging degrees of each point.
The three above steps will be repeated in a loop until the clusters become stable. (say 100 times)

For evaluation of the clustering task, we used the sum of squared distances between data points and cluster centers.

For finding the optimal number of clusters for each dataset, we used the Elbow method.

The following charts illustrate the loss function quantity with respect to the number of clusters for each dataset.
The Elbow point has been determined by a red circle.
The clustered data points have also been plotted. (the data points in the second dataset have four dimensions. So, plotting them is not possible.

The first dataset:

![image](https://github.com/mahdighiasi79/Fuzzy-C-means/assets/51015907/4881a66d-84b3-4978-8dae-7d222376b0c9)
![image](https://github.com/mahdighiasi79/Fuzzy-C-means/assets/51015907/c1d5fdcb-5c05-450f-9d37-a9a0c115eb7c)


The second dataset:

![image](https://github.com/mahdighiasi79/Fuzzy-C-means/assets/51015907/ad10d8a2-b571-4505-a517-a3fc9b79b2fa)


The third dataset:

![image](https://github.com/mahdighiasi79/Fuzzy-C-means/assets/51015907/79df3583-16b3-4ae6-a820-2be994e98e10)
![image](https://github.com/mahdighiasi79/Fuzzy-C-means/assets/51015907/e29b29e0-5f70-45c7-b1c1-b3eeb007d28b)


The fourth dataset:

![image](https://github.com/mahdighiasi79/Fuzzy-C-means/assets/51015907/6df83577-452d-4ff8-8bd3-7ff80f529fec)
![image](https://github.com/mahdighiasi79/Fuzzy-C-means/assets/51015907/98c1845b-a685-4edc-a458-fe06ff9babfd)








