import cv2

image = cv2.imread("fruits.jpg")

print(image.shape)
print(image.size)
print(image.dtype)

#Split images across all 3 channels
b,g,r = cv2.split(image)
image = cv2.merge((b,g,r))

cv2.imshow('Image',image)
cv2.imshow('Blue_Image',b)
cv2.imshow('Red_Image',g)
cv2.imshow('Green_Image',r)
cv2.waitKey(0)
cv2.destroyAllWindows()