from sklearn.cluster import KMeans
from skimage import io
import matplotlib.pyplot as plt
import numpy as np

# Load the image
image = io.imread("sample.jpg")

# Display the original image
# plt.imshow(image)
# plt.axis('off')
# plt.title("Original Image")
# plt.show()

# Reshape the image to be a 2D array of pixels
pixels = image.reshape(-1, 3)

# You can change this value to see different compression levels
k = 8

# Number of colors (clusters)
kmeans = KMeans(n_clusters=k)
kmeans.fit(pixels)

# Replace each pixel value with its corresponding cluster center
compressed_pixels = kmeans.cluster_centers_[kmeans.labels_]

# Reshape back to the original image shape
compressed_image = compressed_pixels.reshape(image.shape).astype(np.uint8)

# Display the compressed image
plt.imshow(compressed_image)
plt.axis('off')
plt.title("Compressed Image (K-Means Clustering)")
plt.show()