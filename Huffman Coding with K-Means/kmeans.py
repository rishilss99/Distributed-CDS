from pyspark.sql import SparkSession
from pyspark.ml.clustering import KMeans
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.evaluation import ClusteringEvaluator
from pyspark.sql.functions import udf, array, col
from pyspark.sql.types import ArrayType, DoubleType
from pyspark.ml.linalg import Vectors, VectorUDT
from PIL import Image

import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.image as img

# Create a SparkSession
spark = SparkSession.builder.appName("Color Quantization").getOrCreate()

rdd = spark.sparkContext.parallelize(["img1.jpg"])
rdd = rdd.pipe("./my_program")

for item in rdd.collect():
    print(item)

image_path = img.imread('img1.ppm')
# print the shape of the image by its height, width and channel
print("Height Width Channel: ", image_path.shape)
print("\n")

(h,w,c) = image_path.shape
image_2D = image_path.reshape(h*w,c)


# Convert NumPy array to a DataFrame with a "features" column
df = spark.createDataFrame([(Vectors.dense(row),) for row in image_2D], ["features"])

# Use VectorAssembler to convert the "features" column to a vector column
assembler = VectorAssembler(inputCols=["features"], outputCol="feature_vector")
df = assembler.transform(df)

# Cache the DataFrame for 5 minutes
# Spark cache() and persist() methods are used as optimization techniques to save interim computation results of DataFrame transformations.
df.cache().count()
df.persist()

# Use silhouette score to choose the optimal K
evaluate = ClusteringEvaluator()
silhouette = []
for k in range(2, 11):
    kmeans = KMeans().setK(k).setSeed(1).setFeaturesCol("feature_vector")
    model = kmeans.fit(df)
    predictions = model.transform(df)
    silhouette.append(evaluate.evaluate(predictions))

# Plot the silhouette score
plt.plot(range(2, 11), silhouette)
plt.title("Silhouette Score")
plt.xlabel("Number of Clusters")
plt.ylabel("Silhouette Score")
plt.show()

# Choose the optimal K using the best silhouette score
optimal_k = silhouette.index(max(silhouette)) + 2
print("Optimal K: ", optimal_k)
print("\n")

# Fit the KMeans model
# Give the number of clusters generated by the elbow method
k_means_model = KMeans().setK(optimal_k).setSeed(1)
k_means_model_centers = k_means_model.fit(df)
cluster_labels = k_means_model.fit(df).transform(df).select("prediction").rdd.flatMap(lambda x: x).collect()
centers = k_means_model_centers.clusterCenters()

from collections import Counter
def get_dominant_color(image_path, k=6, image_processing_size = None):
    image = Image.open(image_path)
    if image_processing_size is not None:
        image = image.resize(image_processing_size, Image.ANTIALIAS)
    result = k_means_model.predict(image)
    result_count = Counter(result)
    most_common = result_count.most_common(k)
    dom_color = [centers[i[0]] for i in most_common]
    return dom_color

labels_count = Counter(cluster_labels)
print("No of points in the cluster: ",labels_count)
print("\n")

# Convert the cluser centers to RGB values
centers_rgb = []
for center in centers:
    scaled_center = [int(x) for x in center]
    centers_rgb.append(scaled_center)
print("RGB values of the cluster centers",centers_rgb)
print("\n")

# Assign all the cluster points to the closest cluster center
cluster_points = []
for point in image_2D:
    min_dist = float('inf')
    closest_center = None
    for center in centers:
        dist = np.linalg.norm(point - center)
        if dist < min_dist:
            min_dist = dist
            closest_center = center
    cluster_points.append(closest_center)
cluster_points = np.array(cluster_points)

# Reshape the cluster points array to form the quantized image
quantized_image = np.reshape(cluster_points, (h, w, c))

# Display the original image and the quantized image in the same figure
fig, ax = plt.subplots(1, 2, figsize=(16, 6))
ax[0].imshow(image_path)
ax[0].set_title("Original Image")
ax[1].imshow(quantized_image.astype(np.uint8))
ax[1].set_title("Quantized Image")
plt.show()

# Save the quantized image
plt.imsave("quantized_image_1.jpg", quantized_image.astype(np.uint8))