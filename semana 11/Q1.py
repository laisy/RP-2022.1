import cv2
import numpy as np
from matplotlib import pyplot as plt

def generate_histogram(img:np.ndarray):
	hist,bins = np.histogram(img.flatten(),256,[0,256])

	plt.hist(img.flatten(),256,[0,256], color = 'r')
	plt.xlim([0,256])
	plt.show()
	
	return hist

img = cv2.imread(r'C:\Users\David\Desktop\imagens\Fig0320(1)(top_left).png', cv2.IMREAD_GRAYSCALE)
generate_histogram(img)
cv2.imshow("Antes",img)
cv2.waitKey()

img = cv2.equalizeHist(img)
generate_histogram(img)
cv2.imshow("Depois",img)
cv2.waitKey()

img = cv2.imread(r'C:\Users\David\Desktop\imagens\Fig0320(2)(2nd_from_top).png', cv2.IMREAD_GRAYSCALE)
generate_histogram(img)
cv2.imshow("Antes",img)
cv2.waitKey()

img = cv2.equalizeHist(img)
generate_histogram(img)
cv2.imshow("Depois",img)
cv2.waitKey()

img = cv2.imread(r'C:\Users\David\Desktop\imagens\Fig0320(3)(third_from_top).png', cv2.IMREAD_GRAYSCALE)
generate_histogram(img)
cv2.imshow("Antes",img)
cv2.waitKey()

img = cv2.equalizeHist(img)
generate_histogram(img)
cv2.imshow("Depois",img)
cv2.waitKey()

img = cv2.imread(r'C:\Users\David\Desktop\imagens\Fig0320(4)(bottom_left).png', cv2.IMREAD_GRAYSCALE)
generate_histogram(img)
cv2.imshow("Antes",img)
cv2.waitKey()

img = cv2.equalizeHist(img)
generate_histogram(img)
cv2.imshow("Depois",img)
cv2.waitKey()

img = cv2.imread(r'C:\Users\David\Desktop\imagens\Fig0323(a)(mars_moon_phobos).png', cv2.IMREAD_GRAYSCALE)
generate_histogram(img)
cv2.imshow("Antes",img)
cv2.waitKey()

img = cv2.equalizeHist(img)
generate_histogram(img)
cv2.imshow("Depois",img)
cv2.waitKey()

img = cv2.imread(r'C:\Users\David\Desktop\imagens\Fig0309(a)(washed_out_aerial_image).png', cv2.IMREAD_GRAYSCALE)
generate_histogram(img)
cv2.imshow("Antes",img)
cv2.waitKey()

img = cv2.equalizeHist(img)
generate_histogram(img)
cv2.imshow("Depois",img)
cv2.waitKey()

img = cv2.imread(r'C:\Users\David\Desktop\imagens\Fig0308(a)(fractured_spine).png', cv2.IMREAD_GRAYSCALE)
generate_histogram(img)
cv2.imshow("Antes",img)
cv2.waitKey()

img = cv2.equalizeHist(img)
generate_histogram(img)
cv2.imshow("Depois",img)
cv2.waitKey()