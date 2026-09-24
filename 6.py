import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the image in grayscale (using 'r' prefix for the Windows path)
img = cv2.imread(r"C:\Users\nidam\OneDrive\Documents\Desktop\Supervity\01_forza7_porsche_gt2rs_02_4k_v2_noflag.jpg", 0)

if img is None:
    print("Error: Image not found")
else:
    # Set up the plot figure
    plt.figure(figsize=(12, 10))
    
    # Display original image
    plt.subplot(3, 3, 1)
    plt.imshow(img, cmap='gray')
    plt.title("Original Image")
    plt.axis("off")

    # Loop through all 8 bit planes
    for i in range(8):
        # Extract the i-th bit plane: shift bits right by i and perform bitwise AND with 1
        bit_plane = (img >> i) & 1

        # Scale to 0-255 for visualization (0 becomes black, 255 becomes white)
        vis_plane = bit_plane * 255

        # Plotting
        plt.subplot(3, 3, i + 2)  # Position starts from 2
        plt.imshow(vis_plane, cmap='gray')
        plt.title(f"Bit Plane {i}")
        plt.axis("off")

    plt.tight_layout()
    plt.show()