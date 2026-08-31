import cv2
import os
import matplotlib.pyplot as plt
import numpy as np
#function to display images
def show_comparison(original,blur3,blur5,blur7):
  plt.figure(figsize=(12,10))

  #original image
  plt.subplot(2,2,1)
  plt.imshow(original,cmap='gray')
  plt.title('Original Image')
  plt.axis('on')

  #3*3 kernal
  plt.subplot(2,2,2)
  plt.imshow(blur3,cmap='gray')
  plt.title("Average filter(3*3)")
  plt.axis('on')

  #5*5 kernal
  plt.subplot(2,2,3)
  plt.imshow(blur5,cmap='gray')
  plt.title("Average filter(5*5)")
  plt.axis('on')
  #7*7 kernel
  plt.subplot(2,2,4)
  plt.imshow(blur7,cmap='gray')
  plt.title("Average filter(7*7)")
  plt.axis('on')
  plt.tight_layout()
  plt.show()

  #read image in grayscale
image_path=os.path.join(os.path.dirname(__file__), "image.jpg")
img = cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
if img is None:
  print('Error: Could not read image')
else:
  kernel_3_3=np.ones((3,3),np.float32)/9
  kernel_5_5=np.ones((5,5),np.float32)/25
  kernel_7_7=np.ones((7,7),np.float32)/49

  #apply each kernel to the image using 2d convolution
  blur_3_3=cv2.filter2D(img,-1,kernel_3_3)
  blur_5_5=cv2.filter2D(img,-1,kernel_5_5)
  blur_7_7=cv2.filter2D(img,-1,kernel_7_7)

  #display the original and blurred images for comparision
  show_comparison(img,blur_3_3,blur_5_5,blur_7_7)