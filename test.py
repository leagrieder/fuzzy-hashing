import numpy as np
from sklearn.cluster import KMeans

# Define the parameters
p = 0.0329
i = 170
# Create a list to store the calculated values
##results = []

# Loop over the range from 1 to 7
##for i in range(38, 96500):
    # Calculate the value for each i using the given formula
value = (1 - p) ** (i - 1) * p
##results.append(value)

# Calculate the mean of the results
##sum = sum(results)

# Print the results and the mean
##print("Values:", results)
##print("Sum:", sum)
#print(value*100)



def equal_prob_clusters(elements, probabilities, num_clusters):
    # Combine elements and probabilities into a single array
    data = np.column_stack((elements, probabilities))

    # Initialize k-means with the desired number of clusters
    kmeans = KMeans(n_clusters=num_clusters)

    # Fit the model to the data
    kmeans.fit(data)

    # Get the cluster labels for each data point
    labels = kmeans.labels_

    # Initialize clusters dictionary to store elements for each cluster
    clusters = {i: [] for i in range(num_clusters)}

    # Assign elements to clusters based on their labels
    for i, label in enumerate(labels):
        clusters[label].append(data[i])

    # Calculate the sum of probabilities for each cluster
    cluster_sums = {i: sum([point[1] for point in cluster]) for i, cluster in clusters.items()}

    # Sort clusters by their sum of probabilities
    sorted_clusters = sorted(cluster_sums.items(), key=lambda x: x[1])

    # Reorganize clusters to minimize difference in sum of probabilities
    balanced_clusters = [[] for _ in range(num_clusters)]
    for i, (cluster_idx, _) in enumerate(sorted_clusters):
        for point in clusters[cluster_idx]:
            balanced_clusters[i % num_clusters].append(point)

    return balanced_clusters

# Example usage
elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
probabilities = [0.1, 0.2, 0.05, 0.15, 0.1, 0.05, 0.1, 0.1, 0.05, 0.1]
num_clusters = 3

# Initialize lists with the appropriate size
#elements = [0] * 96500
#probabilities = [0] * 96500

# Assign values in the loop
#for i in range(1, 96501):
#    elements[i-1] = i
#    probabilities[i-1] = value


#num_clusters = 16

clusters = equal_prob_clusters(elements, probabilities, num_clusters)
for i, cluster in enumerate(clusters):
    for j in range(len(cluster)):
        print(f"Cluster {i + 1}: {cluster[j][0]}")

clusters = equal_prob_clusters(elements, probabilities, num_clusters)
for i, cluster in enumerate(clusters):
    cluster_sum = sum(element[1] for element in cluster)  # Sum probabilities for the current cluster
    print(f"Cluster {i + 1}: Probability Sum = {cluster_sum}")

