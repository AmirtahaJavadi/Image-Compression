# Image Compression using K-Means Clustering

This project implements an image compression technique using the K-means clustering algorithm. It reduces the number of distinct colors in an image, thereby compressing the image size while maintaining visual fidelity.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Acknowledge](#acknowledgements)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Image compression is a common technique used to reduce the file size of images while preserving quality. In this project, we utilize the K-means clustering algorithm to group pixels in the image based on their colors, allowing us to reduce the total number of colors in the image and thereby compressing it.

## Features

- Reduces image size by clustering similar colors.
- Maintains quality with adjustable number of clusters.
- Supports multiple image formats (JPEG, PNG, etc.).
- Easy-to-use command line interface or GUI (if applicable).

## Technologies Used

- Python 3.x
- NumPy
- OpenCV (or PIL for image processing)
- Matplotlib (for visualization, if applicable)
- scikit-learn (for K-means algorithm)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/image-compression-kmeans.git
   cd image-compression-kmeans
2. Install the required packages:
    ```bash
    pip install -r requirements.txt
## Usage

To use the image compression tool, run the script from the command line with the following syntax:

    pip install -r requirements.txt

## Example

input image:

![example image](https://i.postimg.cc/0jd48n2G/Nikon-1-V3-sample-photo.jpg)

output (using 32 clusters):

![example image(32)](https://i.postimg.cc/k4CFnmVZ/sample2.png)

output (using 16 clusters):

![example image(16)](https://i.postimg.cc/wjtk2F8W/sample1.png)

output (using 8 clusters):

![example image(8)](https://i.postimg.cc/65qV6z39/sample3.png)

output (using 4 clusters):

![example image(4)](https://i.postimg.cc/JnRJf5vC/sample4.png)

## acknowledgements


- [K-Means Clustering](https://en.wikipedia.org/wiki/K-means_clustering) for the algorithm documentation.
- Libraries like NumPy, OpenCV, and scikit-learn for their essential functionalities.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes.
4. Commit your changes (git commit -m 'Add new feature').
5. Push to the branch (git push origin feature-branch).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License

