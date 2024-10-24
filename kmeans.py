from sklearn.cluster import KMeans
from skimage import io
import matplotlib.pyplot as plt
import numpy as np
image = io.imread("sample.jpg")
# plt.imshow(image)
# plt.axis('off')
# plt.title("Original Image")
# plt.show()
pixels = image.reshape(-1, 3)
k = 8  # You can change this value to see different compression levels
kmeans = KMeans(n_clusters=k)
kmeans.fit(pixels)
compressed_pixels = kmeans.cluster_centers_[kmeans.labels_]
compressed_image = compressed_pixels.reshape(image.shape).astype(np.uint8)
plt.imshow(compressed_image)
plt.axis('off')
plt.title("Compressed Image (K-Means Clustering)")
plt.show()