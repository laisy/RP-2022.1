import cv2
import numpy as np

def correcao(image):

    for k in range(len(image)):
        for z in range(len(image[k])):
            image[k][z] = np.uint8(image[k][z]/255)

    return np.array(image)

def conversao_de_volta(image):

    for k in range(len(image)):
        for z in range(len(image[k])):
            image[k][z] = np.uint8(image[k][z])

    return np.array(image)

def conversao_de_tipo_entrada(image):
    array_aux = []
    for y in range(len(image)):
        array_aux.append(image[y].tolist())
        for z in range(len(image[y])):
            array_aux[y][z] = (int(image[y][z]))
    
    return array_aux

def multiplicacao_de_imagens(array_aux, img2):
    for p in range(len(array_aux)):
        for u in range(len(array_aux[p])):
            array_aux[p][u] = (array_aux[p][u]) * int(img2[p][u])
    return array_aux

img = cv2.imread('/home/laisy/Documentos/RP/codigos-RP-David/exercício semana 11/imagens/Fig0334(a)(hubble-original).png', cv2.IMREAD_GRAYSCALE)

figure_size = 15
media_image1 = cv2.blur(img,(figure_size, figure_size))

ret, thresh1 = cv2.threshold(media_image1, 64, 255, cv2.THRESH_BINARY)

img_multiplicado = conversao_de_tipo_entrada(img)

img_multiplicado = multiplicacao_de_imagens(img_multiplicado, thresh1)

img_multiplicado = correcao(img_multiplicado)

img_multiplicado = conversao_de_volta(img_multiplicado)

cv2.imshow('15x15 media_q7', media_image1)

cv2.imshow('limiarizacao_q7', thresh1)

cv2.imshow('multiplicacao_q7', img_multiplicado)

cv2.imshow("original", img)

cv2.imwrite('resultado/15x15 media_q7.png', media_image1)

cv2.imwrite('resultado/limiarizacao_q7.png', thresh1)

cv2.imwrite('resultado/multiplicacao_q7.png', img_multiplicado)

   
cv2.waitKey(0)
cv2.destroyAllWindows()