import cv2
import numpy as np

img1 = cv2.imread(r'c:\Users\David\Desktop\RP-2022.1\semana 9\Fig0230(a)(dental_xray).png', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(r'c:\Users\David\Desktop\RP-2022.1\semana 9\Fig0230(b)(dental_xray_mask).png', cv2.IMREAD_GRAYSCALE)

resultado = np.zeros_like(img1)
cv2.imshow('Product', img1)
cv2.waitKey(3)
cv2.imshow('Product', img2)

for i in range(img1.shape[0]):
    for j in range(img1.shape[1]):
        resultado[i,j] = np.sqrt((img1[i,j] * img2[i,j]))

cv2.imshow('Product', aux)
cv2.waitKey(0)
cv2.destroyAllWindows()