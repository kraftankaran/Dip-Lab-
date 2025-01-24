import cv2
import numpy as np
from matplotlib import pyplot as plt

# 1. Read and display the grayscale image
image_path = "diplab1ka2nd.jpg"  # Make sure the image is in the same folder
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Image not found. Make sure the path is correct.")
else:
    plt.figure("Original Image")
    plt.imshow(image, cmap='gray')
    plt.title("Original Grayscale Image")
    plt.axis("off")

    # 2. Convert to negative
    negative_image = 255 - image
    plt.figure("Negative Image")
    plt.imshow(negative_image, cmap='gray')
    plt.title("Negative Image")
    plt.axis("off")

    # 3. Compute mean and median intensity values
    mean_intensity = np.mean(image)
    median_intensity = np.median(image)
    print(f"Mean Intensity: {mean_intensity}")
    print(f"Median Intensity: {median_intensity}")

    # 4. Threshold the image
    _, binary_image = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY)
    plt.figure("Thresholded Image")
    plt.imshow(binary_image, cmap='gray')
    plt.title("Binary Image (Threshold: 120)")
    plt.axis("off")

    # 5. Normalize intensities to [0.25, 0.75], then stretch to [0, 1]
    normalized_image = cv2.normalize(image, None, alpha=0.25, beta=0.75, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    stretched_image = (normalized_image - 0.25) / 0.5  # Mapping [0.25, 0.75] to [0, 1]
    stretched_image = np.clip(stretched_image, 0, 1)  # Ensure values are within [0, 1]

    plt.figure("Stretched Image")
    plt.imshow(stretched_image, cmap='gray')
    plt.title("Normalized and Stretched Image")
    plt.axis("off")

    # Show all plots
    plt.show()
