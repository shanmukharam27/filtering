[README (1).md](https://github.com/user-attachments/files/31655535/README.1.md)
# Image Filtering Using 3×3, 5×5 and 7×7 Average Kernels

## 1. Introduction

Image filtering is an important operation in Digital Image Processing
and Computer Vision. A filter uses a small matrix called a **kernel** or
**mask** and moves it across an image to produce a new image.

In this project, the same image is filtered using three average kernels:

-   3 × 3
-   5 × 5
-   7 × 7

Two implementations are provided:

1.  **`kernel1.py`** --- filtering using OpenCV's inbuilt
    `cv2.filter2D()` function.
2.  **`kernel2.py`** --- filtering implemented manually from scratch
    using NumPy operations and nested loops.

The purpose is to understand both the practical OpenCV implementation
and the internal working of kernel-based filtering.

------------------------------------------------------------------------

# 2. Theory of Image Filtering

## What is an Image Kernel?

A kernel is a small matrix of numerical values used to process
neighboring pixels of an image.

For an average filter, all kernel values are equal. The values are
normalized by dividing them by the total number of elements.

### 3 × 3 Average Kernel

\[ K\_{3`\times3`{=tex}} = `\frac{1}{9}`{=tex}
```{=tex}
\begin{bmatrix}
1&1&1\\
1&1&1\\
1&1&1
\end{bmatrix}
```
\]

### 5 × 5 Average Kernel

\[ K\_{5`\times5`{=tex}} = `\frac{1}{25}`{=tex}
```{=tex}
\begin{bmatrix}
1&1&1&1&1\\
1&1&1&1&1\\
1&1&1&1&1\\
1&1&1&1&1\\
1&1&1&1&1
\end{bmatrix}
```
\]

### 7 × 7 Average Kernel

\[ K\_{7`\times7`{=tex}} = `\frac{1}{49}`{=tex}
```{=tex}
\begin{bmatrix}
1&1&1&1&1&1&1\\
1&1&1&1&1&1&1\\
1&1&1&1&1&1&1\\
1&1&1&1&1&1&1\\
1&1&1&1&1&1&1\\
1&1&1&1&1&1&1\\
1&1&1&1&1&1&1
\end{bmatrix}
```
\]

## Why Divide by 9, 25 and 49?

The normalization keeps the output pixel values in approximately the
same intensity range as the original image.

For example, for a 3 × 3 kernel:

\[ 1+1+1+1+1+1+1+1+1=9 \]

Therefore each value is:

\[ `\frac{1}{9}`{=tex} \]

The filtered pixel is effectively the average of the 9 neighboring
pixels.

------------------------------------------------------------------------

# 3. What Does an Average Filter Do?

An average filter replaces each pixel with the average value of its
neighboring pixels.

Conceptually:

\[ Output(i,j)=`\sum `{=tex}(Image Region `\times `{=tex}Kernel) \]

Because neighboring pixels are averaged, sudden changes in intensity are
reduced.

Therefore, average filtering can:

-   Smooth an image
-   Reduce small variations and some noise
-   Blur edges
-   Remove fine details

## Effect of Kernel Size

The larger the kernel, the more neighboring pixels participate in the
calculation.

Therefore:

``` text
3 × 3  → less smoothing
5 × 5  → more smoothing
7 × 7  → strongest smoothing
```

A 7 × 7 filter generally produces a more blurred result than a 3 × 3
filter.

------------------------------------------------------------------------

# 4. Project Structure

``` text
filtering/
├── image.jpg
├── kernel1.py
├── kernel2.py
└── README.md
```

-   `image.jpg` --- input image
-   `kernel1.py` --- OpenCV inbuilt-function implementation
-   `kernel2.py` --- from-scratch implementation
-   `README.md` --- theory and explanation of both implementations

------------------------------------------------------------------------

# 5. Input Image

The input image is:

``` text
image.jpg
```

The image is read and processed as a grayscale image.

A grayscale image contains intensity values rather than separate RGB
color channels.

For the OpenCV implementation, the image is read using:

``` python
img = cv2.imread('image.jpg', 0)
```

In the from-scratch implementation, the image is read using Matplotlib
and converted to grayscale when required.

------------------------------------------------------------------------

# 6. Implementation 1 --- Using OpenCV Inbuilt Function

## File

``` text
kernel1.py
```

This version uses OpenCV's built-in convolution/filtering function:

``` python
cv2.filter2D()
```

## Main Libraries

``` python
import cv2
import matplotlib.pyplot as plt
import numpy as np
```

### OpenCV

`cv2` is used for:

-   Reading the image
-   Applying the filtering operation

### NumPy

`numpy` is used to:

-   Create the kernels
-   Store image data
-   Perform numerical operations

### Matplotlib

`matplotlib.pyplot` is used to display the original and filtered images.

------------------------------------------------------------------------

## Creating the Kernels

The 3 × 3 kernel is created using:

``` python
kernel_3_3 = np.ones((3,3), np.float32) / 9
```

Similarly:

``` python
kernel_5_5 = np.ones((5,5), np.float32) / 25
kernel_7_7 = np.ones((7,7), np.float32) / 49
```

`np.ones()` creates a matrix containing ones.

The division normalizes the kernel.

------------------------------------------------------------------------

## Applying the Filters

The OpenCV function is used as follows:

``` python
blur_3_3 = cv2.filter2D(img, -1, kernel_3_3)
blur_5_5 = cv2.filter2D(img, -1, kernel_5_5)
blur_7_7 = cv2.filter2D(img, -1, kernel_7_7)
```

Here:

-   `img` is the input image.
-   `-1` specifies that the output image should have the same depth as
    the input.
-   The third argument is the kernel.

OpenCV performs the convolution/filtering operation internally.

------------------------------------------------------------------------

## Displaying the Results

The program displays:

``` text
Original Image
3 × 3 Average Filter
5 × 5 Average Filter
7 × 7 Average Filter
```

This makes it possible to compare the effect of different kernel sizes.

------------------------------------------------------------------------

# 7. Implementation 2 --- From Scratch

## File

``` text
kernel2.py
```

This version demonstrates how average filtering works internally without
using:

``` python
cv2.filter2D()
```

Instead, the filtering operation is implemented manually.

------------------------------------------------------------------------

# 8. From-Scratch Filtering Algorithm

The main filtering function follows these steps.

## Step 1 --- Create the Kernel

For a kernel of size `size`:

``` python
kernel = np.ones((size, size), dtype=np.float32) / (size * size)
```

For example:

``` text
size = 3  → 3 × 3 kernel
size = 5  → 5 × 5 kernel
size = 7  → 7 × 7 kernel
```

------------------------------------------------------------------------

## Step 2 --- Calculate Padding

The amount of padding is:

``` python
pad = size // 2
```

Therefore:

``` text
3 × 3 → pad = 1
5 × 5 → pad = 2
7 × 7 → pad = 3
```

Padding is required so that filtering can also be performed at the image
boundaries.

------------------------------------------------------------------------

# 9. Why Padding Is Required

Suppose a 3 × 3 kernel is placed on a pixel at the edge of the image.

There are not enough pixels outside the image to form a complete 3 × 3
region.

Padding solves this problem by adding extra pixels around the image.

In the implementation:

``` python
padded = np.pad(image, pad, mode='edge')
```

The `edge` mode extends the border values.

This allows every pixel to have a complete kernel-sized neighborhood.

------------------------------------------------------------------------

# 10. Creating the Output Image

The output array is created using:

``` python
output = np.zeros_like(image, dtype=np.float32)
```

It initially contains zeros and is gradually filled with the filtered
pixel values.

------------------------------------------------------------------------

# 11. Moving the Kernel Across the Image

Nested loops are used:

``` python
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
```

The outer loop moves through image rows.

The inner loop moves through image columns.

Thus, every pixel is processed.

------------------------------------------------------------------------

# 12. Extracting the Region

For every pixel, a region having the same size as the kernel is
extracted:

``` python
region = padded[i:i + size, j:j + size]
```

For example, if `size = 3`, the selected region is 3 × 3.

If `size = 7`, the selected region is 7 × 7.

------------------------------------------------------------------------

# 13. Multiplication and Summation

The core filtering operation is:

``` python
output[i, j] = np.sum(region * kernel)
```

This performs two operations:

### Element-wise multiplication

Each pixel in the selected region is multiplied by the corresponding
kernel value.

### Summation

All the multiplied values are added together.

Since the kernel contains normalized values, the result is the average
of the neighboring pixels.

------------------------------------------------------------------------

# 14. Converting the Output

After filtering, the result is converted to an 8-bit image:

``` python
return output.astype(np.uint8)
```

This is appropriate for normal grayscale image intensity values.

------------------------------------------------------------------------

# 15. Applying the Three Filters

The same from-scratch function is called three times:

``` python
blur_3_3 = average_filter(img, 3)
blur_5_5 = average_filter(img, 5)
blur_7_7 = average_filter(img, 7)
```

This produces three filtered images.

------------------------------------------------------------------------

# 16. Comparison of Both Implementations

  -----------------------------------------------------------------------
  Feature                 `kernel1.py`            `kernel2.py`
  ----------------------- ----------------------- -----------------------
  Approach                OpenCV inbuilt function From scratch

  Main filtering function `cv2.filter2D()`        Custom
                                                  `average_filter()`

  3 × 3 kernel            Yes                     Yes

  5 × 5 kernel            Yes                     Yes

  7 × 7 kernel            Yes                     Yes

  Pixel loops             Handled internally by   Explicit nested loops
                          OpenCV                  

  Kernel creation         NumPy                   NumPy

  Padding                 Handled by filtering    Explicitly implemented
                          operation               

  Purpose                 Practical               Understanding the
                          implementation          algorithm

  Speed                   Generally faster        Generally slower

  Learning value          Easy to use             Shows internal process
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# 17. Inbuilt vs From-Scratch Concept

The difference can be understood as:

``` text
INBUILT VERSION

Image
  ↓
Create Kernel
  ↓
cv2.filter2D()
  ↓
Filtered Image
```

Whereas:

``` text
FROM-SCRATCH VERSION

Image
  ↓
Create Kernel
  ↓
Pad Image
  ↓
Move Kernel Across Image
  ↓
Extract Region
  ↓
Multiply Region × Kernel
  ↓
Sum Values
  ↓
Store Output Pixel
  ↓
Repeat for All Pixels
  ↓
Filtered Image
```

The second approach exposes the actual operations that an
image-filtering algorithm performs.

------------------------------------------------------------------------

# 18. Expected Output

Both programs display four images for comparison:

``` text
┌─────────────────┬─────────────────┐
│  Original Image │  3 × 3 Filter   │
├─────────────────┼─────────────────┤
│  5 × 5 Filter   │  7 × 7 Filter   │
└─────────────────┴─────────────────┘
```

The expected visual trend is:

``` text
Original
   ↓
3 × 3 → slightly blurred
   ↓
5 × 5 → more blurred
   ↓
7 × 7 → strongly blurred
```

------------------------------------------------------------------------

# 19. Requirements

Install the required Python packages:

``` bash
pip install opencv-python numpy matplotlib
```

For the OpenCV version, `opencv-python` is required.

The from-scratch version uses NumPy and Matplotlib for numerical
processing and visualization.

------------------------------------------------------------------------

# 20. How to Run

Open the terminal in the project folder:

``` text
filtering
```

Run the OpenCV implementation:

``` bash
python kernel1.py
```

Run the from-scratch implementation:

``` bash
python kernel2.py
```

------------------------------------------------------------------------

# 21. Conclusion

This project demonstrates the application of average filtering using 3 ×
3, 5 × 5 and 7 × 7 kernels.

The first implementation uses OpenCV's built-in `cv2.filter2D()`
function, making the filtering process simple and practical.

The second implementation performs the filtering operation manually
using padding, nested loops, region extraction, element-wise
multiplication and summation. This provides a better understanding of
how kernel-based image filtering works internally.

As the kernel size increases from 3 × 3 to 7 × 7, a larger neighborhood
is averaged, resulting in increased smoothing and blurring.

Therefore, the project demonstrates both **how to perform image
filtering efficiently using an inbuilt function** and **how the same
filtering concept can be implemented from scratch**.


Input image for the code 4,5 and 6 codes 
<img width="3840" height="2160" alt="01_forza7_porsche_gt2rs_02_4k_v2_noflag" src="https://github.com/user-attachments/assets/fe23452a-1799-4925-ae51-66ef619c8db7" />
6.py code output
<img width="1536" height="752" alt="Figure_3" src="https://github.com/user-attachments/assets/47b946a9-c40f-4d4f-99fb-4d8ec718ad6b" />
5.py code output
<img width="1536" height="752" alt="Figure_2" src="https://github.com/user-attachments/assets/aea2b0a0-14d4-4720-bc36-179c4a19c1e1" />
4.py code output
<img width="1536" height="752" alt="Figure_1" src="https://github.com/user-attachments/assets/6b7e672b-b76f-447b-adda-57467449336d" />
