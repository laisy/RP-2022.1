import cv2
import numpy as np
 
img = cv2.imread('/home/laisy/Documentos/RP/RP-2022.1/semana 11/imagens/Fig0335(a)(ckt_board_saltpep_prob_pt05).png', cv2.IMREAD_GRAYSCALE)

figure_size = 3
media_image1 = cv2.blur(img,(figure_size, figure_size))
mediana_image1 = cv2.medianBlur(img, figure_size)

cv2.imshow('3x3 media_q8', media_image1)

cv2.imshow('3x3 mediana_q8', mediana_image1)

cv2.imshow("original", img)

cv2.imwrite('resultado/3x3 media_q8.png', media_image1)

cv2.imwrite('resultado/3x3 mediana_q8.png', mediana_image1)
   
cv2.waitKey(0)
cv2.destroyAllWindows()