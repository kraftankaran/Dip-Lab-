import cv2
import numpy as np
import matplotlib.pyplot as plt

# List of image filenames
image_files = [
    'lab2bone_scint.pgm', 'lab2Brain1.pgm', 'lab2Brain2.pgm', 'lab2Brain3.pgm', 'lab2Brain4.pgm',
    'lab2Brain5.pgm', 'lab2MR.pgm', 'lab2shoulderCR.pgm', 'lab2thyroid_scint.pgm', 'lab2ultrasound (1).pgm',
    'lungs.pgm'
]

# Function to display the list of images
def display_image_list(image_files):
    print("Available images:")
    for i, filename in enumerate(image_files):
        print(f"{i + 1}. {filename}")

# Function to let the user select an image
def select_image(image_files):
    display_image_list(image_files)
    while True:
        try:
            choice = int(input("Enter the number of the image you want to process (1-11): "))
            if 1 <= choice <= 11:
                return image_files[choice - 1]
            else:
                print("Invalid choice. Please enter a number between 1 and 11.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Intensity Averaging
def intensity_averaging(img):
    kernel = np.ones((3, 3), np.float32) / 9
    return cv2.filter2D(img, -1, kernel)

# Inversion
def inversion(img):
    return 255 - img

# Sub-sampling
def subsampling(img, factor=2):
    return img[::factor, ::factor]

# Contrast Stretching
def contrast_stretching(img):
    min_val = np.min(img)
    max_val = np.max(img)
    return (img - min_val) * (255 / (max_val - min_val))

# Log Transform
def log_transform(img):
    c = 255 / np.log(1 + np.max(img))
    return c * np.log(1 + img)

# Power-Law (Gamma) Transform
def gamma_transform(img, gamma=1.0):
    return np.power(img / 255.0, gamma) * 255

# Main program
if __name__ == "__main__":
    # Let the user select an image
    selected_image = select_image(image_files)
    print(f"Selected image: {selected_image}")

    # Read the selected image
    image = cv2.imread(selected_image, cv2.IMREAD_GRAYSCALE)

    # Check if the image was loaded successfully
    if image is None:
        print("Error: Could not load the image. Please check the file path.")
    else:
        # Apply operations
        avg_img = intensity_averaging(image)
        inv_img = inversion(image)
        sub_img = subsampling(image)
        cs_img = contrast_stretching(image)
        log_img = log_transform(image)
        gamma_img = gamma_transform(image, gamma=0.5)

        # Display results
        plt.figure(figsize=(12, 8))
        plt.subplot(2, 3, 1), plt.imshow(avg_img, cmap='gray'), plt.title('Averaging')
        plt.subplot(2, 3, 2), plt.imshow(inv_img, cmap='gray'), plt.title('Inversion')
        plt.subplot(2, 3, 3), plt.imshow(sub_img, cmap='gray'), plt.title('Sub-sampling')
        plt.subplot(2, 3, 4), plt.imshow(cs_img, cmap='gray'), plt.title('Contrast Stretching')
        plt.subplot(2, 3, 5), plt.imshow(log_img, cmap='gray'), plt.title('Log Transform')
        plt.subplot(2, 3, 6), plt.imshow(gamma_img, cmap='gray'), plt.title('Gamma Transform')
        plt.show()