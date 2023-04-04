import cv2
import numpy as np
 
img = cv2.imread('/home/laisy/Documentos/RP/RP-2022.1/semana 11/imagens/Fig0333(a)(test_pattern_blurring_orig).png', cv2.IMREAD_GRAYSCALE)

figure_size = 3
new_image = cv2.blur(img,(figure_size, figure_size))

figure_size2 = 5
new_image2 = cv2.blur(img,(figure_size2, figure_size2))

figure_size3 = 9
new_image3 = cv2.blur(img,(figure_size3, figure_size3))

figure_size4 = 15
new_image4 = cv2.blur(img,(figure_size4, figure_size4))

figure_size5 = 35
new_image5 = cv2.blur(img,(figure_size5, figure_size5))


cv2.imshow('3x3_q6', new_image)
cv2.imshow('5x5_q6', new_image2)
cv2.imshow('9x9_q6', new_image3)
cv2.imshow('15x15_q6', new_image4)
cv2.imshow('35x35_q6', new_image5)
cv2.imshow("original", img)

cv2.imwrite('resultado/3x3_q6.png', new_image)
cv2.imwrite('resultado/5x5_q6.png', new_image2)
cv2.imwrite('resultado/9x9_q6.png', new_image3)
cv2.imwrite('resultado/35x35_q6.png', new_image5)
cv2.imwrite('resultado/15x15_q6.png', new_image4)
   
cv2.waitKey(0)
cv2.destroyAllWindows()