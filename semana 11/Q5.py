import cv2
import numpy as np

def otsu(imagem):
    ret, res = cv2.threshold(imagem, 0, 255, cv2.THRESH_OTSU)
    return res
def medianFilter(img):
    return cv2.medianBlur(img,5)

img = cv2.imread(r'C:\Users\David\Desktop\imagens\Fig1036(c)(gaussian_noise_mean_0_std_50_added).png', cv2.IMREAD_GRAYSCALE)
lOtsu = otsu(img)
median = medianFilter(img)
otsuMedian = otsu(median)
cv2.imshow("Original",img)
cv2.imshow("A",lOtsu)
cv2.imshow("B",otsuMedian)
cv2.waitKey()