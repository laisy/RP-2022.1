import cv2
import numpy as np
 

img = cv2.imread('/home/laisy/Documentos/RP/RP-2022.1/semana 12/imagens/Fig0340(a)(dipxe_text).png', 0)

def highBoost(image,k):
    
    img_saida = image.copy()
    for i in range(1,len(image)-1):
        for j in range(1,len(image[i])-1):
            img_saida[i, j] = image[i, j] + (k * image[i, j])
    borramento = cv2.GaussianBlur(image, (11, 11), 0)   
    img_saida = img_saida - borramento
    return img_saida

high_boost = highBoost(img, 1)
high_boost2 = highBoost(img, 2)
high_boost3 = highBoost(img, 3)
high_boost4 = highBoost(img, 4)
high_boost5 = highBoost(img, 5)
high_boost6 = highBoost(img, 6)
high_boost7 = highBoost(img, 7)
high_boost8 = highBoost(img, 8)
high_boost9 = highBoost(img, 9)
high_boost10 = highBoost(img, 10)
high_boost11 = highBoost(img, 11)
high_boost12 = highBoost(img, 12)
high_boost13 = highBoost(img, 13)
high_boost14 = highBoost(img, 14)
high_boost15 = highBoost(img, 15)
high_boost16 = highBoost(img, 16)
high_boost17 = highBoost(img, 17)
high_boost800 = highBoost(img, 800)
high_boost1000 = highBoost(img, 1000)

cv2.imshow("high_boost_Original", img)

cv2.imshow("high_boost1", high_boost)
cv2.imshow("high_boost2", high_boost2)
cv2.imshow("high_boost3", high_boost3)
cv2.imshow("high_boost4", high_boost4)
cv2.imshow("high_boost5", high_boost5)
cv2.imshow("high_boost6", high_boost6)
cv2.imshow("high_boost7", high_boost7)
cv2.imshow("high_boost8", high_boost8)
cv2.imshow("high_boost9", high_boost9)
cv2.imshow("high_boost10", high_boost10)
cv2.imshow("high_boost11", high_boost11)
cv2.imshow("high_boost12", high_boost12)
cv2.imshow("high_boost13", high_boost13)
cv2.imshow("high_boost16", high_boost16)
cv2.imshow("high_boost17", high_boost17)
cv2.imshow("high_boost800", high_boost800)
cv2.imshow("high_boost1000", high_boost1000)

cv2.imwrite("resultado/high_boost2.png", high_boost)
cv2.imwrite("resultado/high_boost3.png", high_boost2)
cv2.imwrite("resultado/high_boost4.png", high_boost3)
cv2.imwrite("resultado/high_boost5.png", high_boost4)
cv2.imwrite("resultado/high_boost6.png", high_boost5)
cv2.imwrite("resultado/high_boost7.png", high_boost6)
cv2.imwrite("resultado/high_boost8.png", high_boost7)
cv2.imwrite("resultado/high_boost8.png", high_boost8)
cv2.imwrite("resultado/high_boost9.png", high_boost9)
cv2.imwrite("resultado/high_boost10.png", high_boost10)
cv2.imwrite("resultado/high_boost11.png", high_boost11)
cv2.imwrite("resultado/high_boost12.png", high_boost12)
cv2.imwrite("resultado/high_boost13.png", high_boost13)
cv2.imwrite("resultado/high_boost16.png", high_boost16)
cv2.imwrite("resultado/high_boost800.png", high_boost800)

cv2.waitKey(0)
cv2.destroyAllWindows()