import cv2

image = cv2.imread('example.jpg')

small = cv2.resize(image, (100, 100))
medium = cv2.resize(image, (300, 300))
large = cv2.resize(image, (500, 500))

cv2.imshow('Small Image', small)
cv2.imshow('Medium Image', medium)
cv2.imshow('Large Image', large)

cv2.imwrite('small_image.jpg', small)
cv2.imwrite('medium_image.jpg', medium)
cv2.imwrite('large_image.jpg', large)

cv2.waitKey(0)

cv2.destroyAllWindows()

print("Images saved successfully!")

print(f"Small Image Dimensions: {small.shape}")
print(f"Medium Image Dimensions: {medium.shape}")
print(f"Large Image Dimensions: {large.shape}")