import numpy as np
import cv2

def limiar(img):
    T0 = img.flatten().mean()
    T = 0
    dT = 1
    while(abs(T0 - T) >= dT):
        a = img[np.where(img > T0)]
        b = img[img <= T0]
        ma = np.mean(a)
        mb = np.mean(b)
        T = (ma + mb) / 2
        T0 = T
    Im,nImg = cv2.threshold(img,T0,255, cv2.THRESH_BINARY) 
    return nImg

img = cv2.imread(r'C:\Users\David\Desktop\imagens\Fig1038(a)(noisy_fingerprint).png', cv2.IMREAD_GRAYSCALE)
# img = cv2.imread('../imagens/Fig0320(1)(top_left).png',0)
nImg = limiar(img)
cv2.imshow("Original", img)
cv2.imshow("Limiar", nImg)

cv2.waitKey(0)
cv2.destroyAllWindows()
