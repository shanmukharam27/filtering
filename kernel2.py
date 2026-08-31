import matplotlib.pyplot as plt
import numpy as np

# Function to apply average filter from scratch
def average_filter(image, size):
    kernel = np.ones((size, size), dtype=np.float32) / (size * size)

    # Add padding so the kernel can work at image borders
    pad = size // 2
    padded = np.pad(image, pad, mode='edge')

    output = np.zeros_like(image, dtype=np.float32)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            region = padded[i:i + size, j:j + size]
            output[i, j] = np.sum(region * kernel)

    return output.astype(np.uint8)


# Function to display images
def show_comparison(original, blur3, blur5, blur7):

    plt.figure(figsize=(12, 10))

    # Original image
    plt.subplot(2, 2, 1)
    plt.imshow(original, cmap='gray')
    plt.title('Original Image')
    plt.axis('on')

    # 3x3 kernel
    plt.subplot(2, 2, 2)
    plt.imshow(blur3, cmap='gray')
    plt.title('Average Filter (3x3)')
    plt.axis('on')

    # 5x5 kernel
    plt.subplot(2, 2, 3)
    plt.imshow(blur5, cmap='gray')
    plt.title('Average Filter (5x5)')
    plt.axis('on')

    # 7x7 kernel
    plt.subplot(2, 2, 4)
    plt.imshow(blur7, cmap='gray')
    plt.title('Average Filter (7x7)')
    plt.axis('on')

    plt.tight_layout()
    plt.show()


# Read image WITHOUT cv2
img = plt.imread('image.jpg')

# Convert RGB image to grayscale
if len(img.shape) == 3:
    img = np.mean(img[:, :, :3], axis=2)

# Apply average filters
blur_3_3 = average_filter(img, 3)
blur_5_5 = average_filter(img, 5)
blur_7_7 = average_filter(img, 7)

# Display results
show_comparison(img, blur_3_3, blur_5_5, blur_7_7)