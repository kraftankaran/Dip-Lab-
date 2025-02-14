Image Processing Operations

Description

This Python script allows users to apply various image processing operations on a set of grayscale medical images stored in PGM format. Users can select an image and apply transformations such as intensity averaging, inversion, subsampling, contrast stretching, log transformation, and gamma transformation. The results are displayed using Matplotlib.

Features

Intensity Averaging: Smooths the image using a 3x3 averaging filter.

Inversion: Inverts the pixel values (negative of the image).

Sub-sampling: Reduces the image size by selecting every nth pixel.

Contrast Stretching: Normalizes pixel values to enhance contrast.

Log Transform: Enhances details in darker regions.

Power-Law (Gamma) Transform: Adjusts image brightness based on a gamma value.

Requirements

Make sure you have the following dependencies installed:

Python 3.x

OpenCV (cv2)

NumPy

Matplotlib

You can install the required libraries using:

pip install opencv-python numpy matplotlib

Usage

Place the script in the same directory as your image files.

Run the script:

python script.py

Select an image by entering the corresponding number from the displayed list.

The script will apply the transformations and display the processed images in a 2x3 grid.

Image File List

The script processes the following PGM images:

lab2bone_scint.pgm

lab2Brain1.pgm

lab2Brain2.pgm

lab2Brain3.pgm

lab2Brain4.pgm

lab2Brain5.pgm

lab2MR.pgm

lab2shoulderCR.pgm

lab2thyroid_scint.pgm

lab2ultrasound (1).pgm

lungs.pgm

Functions

display_image_list(image_files)

Displays the available images.

select_image(image_files)

Allows the user to select an image from the list.

intensity_averaging(img)

Applies an averaging filter to smooth the image.

inversion(img)

Inverts the image.

subsampling(img, factor=2)

Reduces the image size by selecting every nth pixel.

contrast_stretching(img)

Enhances the contrast of the image.

log_transform(img)

Applies log transformation to enhance darker regions.

gamma_transform(img, gamma=1.0)

Adjusts image brightness using gamma correction.

Output

The script displays six processed images:

Averaged Image

Inverted Image

Sub-sampled Image

Contrast Stretched Image

Log Transformed Image

Gamma Transformed Image

