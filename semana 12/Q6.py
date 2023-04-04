import cv2
import numpy as np
 
img = cv2.imread("/home/laisy/Documentos/RP/RP-2022.1/semana 12/imagens/Fig1016(a)(building_original).png", 0)

cv2.imshow("building_original", img)

sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

sobel = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

media5x5 = cv2.blur(img, (5,5))

sobelx2 = cv2.Sobel(media5x5,cv2.CV_64F,1,0,ksize=5)
sobely2 = cv2.Sobel(media5x5,cv2.CV_64F,0,1,ksize=5)

sobel_media_filter = cv2.addWeighted(sobelx2, 0.5, sobely2, 0.5, 0)

t, limiar80a = cv2.threshold(sobel, 80, 255, cv2.THRESH_BINARY)
t, limiar80b = cv2.threshold(sobel_media_filter, 80, 255, cv2.THRESH_BINARY)

cv2.imshow("building_x", sobel)
cv2.imshow("building_5x5", sobel_media_filter)
cv2.imshow("building_limiar80a", limiar80a)
cv2.imshow("building_limiar80b", limiar80b)

cv2.imwrite("RP-2022.1/semana 12/resultado/building_x.png", sobel)
cv2.imwrite("RP-2022.1/semana 12/resultado/building_5x5.png", sobel_media_filter)
cv2.imwrite("RP-2022.1/semana 12/resultado/building_limiar80a.png", limiar80a)
cv2.imwrite("RP-2022.1/semana 12/resultado/building_limiar80b.png", limiar80b)

cv2.waitKey(0)
cv2.destroyAllWindows()