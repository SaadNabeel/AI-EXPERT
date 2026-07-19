import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('example.jpg')

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.imshow(image_rgb)
plt.title("Original Image")
plt.show()

(h, w) = image.shape[:2]

center = (w // 2, h // 2)

M = cv2.getRotationMatrix2D(center, 90, 1.0)

rotated = cv2.warpAffine(image, M, (w, h))

rotated_rgb = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)

plt.imshow(rotated_rgb)
plt.title("Rotated Image")
plt.show()

cropped = image[100:300, 100:300]

cropped_rgb = cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB)

plt.imshow(cropped_rgb)
plt.title("Cropped Image")
plt.show()

brightness_matrix = np.ones(image.shape, dtype="uint8") * 40

bright_image = cv2.add(image, brightness_matrix)

bright_rgb = cv2.cvtColor(bright_image, cv2.COLOR_BGR2RGB)

plt.imshow(bright_rgb)
plt.title("Brighter Image")
plt.show()

print("Original Dimensions:", image.shape)
print("Rotated Dimensions:", rotated.shape)
print("Cropped Dimensions:", cropped.shape)
print("Brightened Dimensions:", bright_image.shape)