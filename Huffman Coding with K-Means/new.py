from PIL import Image
import matplotlib.image as img
import matplotlib.pyplot as plt

image = img.imread('img1.ppm')
# print the shape of the image by its height, width and channel

print("Height Width Channel: ", image.shape)

# Display the image using imshow()
plt.imshow(image)

# Show the plot
plt.show()

image_path = img.imread('img1.jpg')
# print the shape of the image by its height, width and channel
print("Height Width Channel: ", image_path.shape)
print("\n")

(h,w,c) = image_path.shape
image_2D = image_path.reshape(h*w,c)

# Create a SparkSession
spark = SparkSession.builder.appName("Color Quantization").getOrCreate()

rdd = spark.sparkContext.parallelize(["img1.jpg"])
rdd = rdd.pipe("./my_program")

for item in rdd.collect():
    print(item)
