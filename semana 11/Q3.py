import cv2
import numpy as np
from matplotlib import pyplot as plt

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
    img,nImg = cv2.threshold(img,T0,255, cv2.THRESH_BINARY) 
    print(f"Limiar: {T}")
    return nImg

def otsu(im):
    [hist, _] = np.histogram(im, bins=256, range=(0, 255))
    hist = 1.0*hist/np.sum(hist)

    val_max = -999
    thr = -1
    for t in range(1,255):
        q1 = np.sum(hist[:t])
        q2 = np.sum(hist[t:])
        m1 = np.sum(np.array([i for i in range(t)])*hist[:t])/q1
        m2 = np.sum(np.array([i for i in range(t,256)])*hist[t:])/q2
        val = q1*(1-q1)*np.power(m1-m2,2)
        if val_max < val:
            val_max = val
            thr = t

    print("Limiar: {}".format(thr))

    f = plt.figure(1)
    plt.imshow(im, cmap = 'gray')
    f.show()
    g = plt.figure(2)
    plt.imshow(im > thr, cmap = 'gray')
    g.show()
    g.savefig('otsu.png')
    input()

img = cv2.imread(r'C:\Users\David\Desktop\imagens\Fig1039(a)(polymersomes).png', cv2.IMREAD_GRAYSCALE)
lSimples = limiar(img)

cv2.imshow("Original", img)
cv2.imshow("Limiar", lSimples)
cv2.imwrite("Limiar.png",lSimples)

cv2.waitKey(0)
cv2.destroyAllWindows()

otsu(img)
#variancia ponderada