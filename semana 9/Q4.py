import cv2
import numpy as np

img1 = cv2.imread(r'c:\Users\David\Desktop\RP-2022.1\semana 9\Imagens\Fig0230(a)(dental_xray).png', cv2.IMREAD_GRAYSCALE) / 255
img2 = cv2.imread(r'c:\Users\David\Desktop\RP-2022.1\semana 9\Imagens\Fig0230(b)(dental_xray_mask)2.png', cv2.IMREAD_GRAYSCALE) / 255

resultado = np.multiply(img1, img2)
cv2.imshow('Product', resultado)
cv2.waitKey(0)
cv2.destroyAllWindows()